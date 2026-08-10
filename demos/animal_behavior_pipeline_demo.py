"""Public-safe demonstration of temporal animal-behaviour event processing.

This file is independently written for portfolio purposes. It does not contain
research data, research code, trained models, private annotations, or internal
infrastructure from any active collaboration.

The goal is to demonstrate three transferable ideas from long-form video AI:
1. stabilize noisy per-frame identity evidence over time;
2. convert track observations into short temporal event windows;
3. export structured samples suitable for downstream action-recognition work.

Input observations here are synthetic. In a real pipeline they would be
produced by detection, tracking, re-identification and/or segmentation models.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Deque, Dict, Iterable, List, Optional, Tuple


@dataclass(frozen=True)
class Observation:
    frame: int
    track_id: int
    identity_hint: Optional[str]
    identity_confidence: float
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass(frozen=True)
class StabilizedObservation:
    frame: int
    track_id: int
    identity: str
    identity_confidence: float
    center_x: float
    center_y: float


class TemporalIdentityStabilizer:
    """Majority-vote identity fusion over a bounded temporal history."""

    def __init__(self, history_size: int = 7, min_hint_confidence: float = 0.55):
        if history_size < 1:
            raise ValueError("history_size must be >= 1")
        self.history_size = history_size
        self.min_hint_confidence = min_hint_confidence
        self._history: Dict[int, Deque[Tuple[str, float]]] = defaultdict(
            lambda: deque(maxlen=self.history_size)
        )

    def update(self, obs: Observation) -> StabilizedObservation:
        if (
            obs.identity_hint
            and obs.identity_confidence >= self.min_hint_confidence
        ):
            self._history[obs.track_id].append(
                (obs.identity_hint, obs.identity_confidence)
            )

        history = list(self._history[obs.track_id])
        if not history:
            identity = "unknown"
            confidence = 0.0
        else:
            counts = Counter(label for label, _ in history)
            identity, votes = counts.most_common(1)[0]
            matching_confidences = [
                conf for label, conf in history if label == identity
            ]
            vote_fraction = votes / len(history)
            mean_confidence = sum(matching_confidences) / len(matching_confidences)
            confidence = vote_fraction * mean_confidence

        center_x = (obs.x1 + obs.x2) / 2.0
        center_y = (obs.y1 + obs.y2) / 2.0

        return StabilizedObservation(
            frame=obs.frame,
            track_id=obs.track_id,
            identity=identity,
            identity_confidence=confidence,
            center_x=center_x,
            center_y=center_y,
        )


def build_temporal_windows(
    observations: Iterable[StabilizedObservation],
    window_frames: int = 5,
) -> List[dict]:
    """Create fixed-length track windows with simple motion descriptors."""

    if window_frames < 2:
        raise ValueError("window_frames must be >= 2")

    by_track: Dict[int, List[StabilizedObservation]] = defaultdict(list)
    for obs in observations:
        by_track[obs.track_id].append(obs)

    windows: List[dict] = []
    for track_id, track_obs in by_track.items():
        track_obs.sort(key=lambda item: item.frame)

        for start in range(0, len(track_obs) - window_frames + 1):
            chunk = track_obs[start : start + window_frames]

            dx = chunk[-1].center_x - chunk[0].center_x
            dy = chunk[-1].center_y - chunk[0].center_y
            displacement = (dx * dx + dy * dy) ** 0.5

            identities = [item.identity for item in chunk if item.identity != "unknown"]
            identity = Counter(identities).most_common(1)[0][0] if identities else "unknown"

            mean_identity_conf = sum(
                item.identity_confidence for item in chunk
            ) / len(chunk)

            windows.append(
                {
                    "track_id": track_id,
                    "identity": identity,
                    "start_frame": chunk[0].frame,
                    "end_frame": chunk[-1].frame,
                    "dx": round(dx, 3),
                    "dy": round(dy, 3),
                    "displacement": round(displacement, 3),
                    "mean_identity_confidence": round(mean_identity_conf, 3),
                }
            )

    return windows


def export_windows_csv(windows: List[dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not windows:
        return

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(windows[0].keys()))
        writer.writeheader()
        writer.writerows(windows)


def synthetic_observations() -> List[Observation]:
    """Generate deterministic observations with intentionally noisy identity hints."""

    hints = [
        ("animal_A", 0.92),
        ("animal_A", 0.81),
        ("animal_B", 0.58),  # noisy frame-level identity
        ("animal_A", 0.88),
        (None, 0.0),          # temporary ambiguity / occlusion
        ("animal_A", 0.90),
        ("animal_A", 0.86),
        ("animal_A", 0.93),
    ]

    observations: List[Observation] = []
    for frame, (hint, confidence) in enumerate(hints, start=100):
        x1 = 200 + 8 * (frame - 100)
        y1 = 150 + 3 * (frame - 100)
        observations.append(
            Observation(
                frame=frame,
                track_id=7,
                identity_hint=hint,
                identity_confidence=confidence,
                x1=x1,
                y1=y1,
                x2=x1 + 90,
                y2=y1 + 120,
            )
        )
    return observations


def main() -> None:
    stabilizer = TemporalIdentityStabilizer(history_size=5)
    stabilized = [stabilizer.update(obs) for obs in synthetic_observations()]

    print("Stabilized observations:")
    for obs in stabilized:
        print(
            f"frame={obs.frame} track={obs.track_id} "
            f"identity={obs.identity:<10} "
            f"confidence={obs.identity_confidence:.3f}"
        )

    windows = build_temporal_windows(stabilized, window_frames=5)

    print("\nTemporal windows:")
    for window in windows:
        print(window)

    output = Path("outputs") / "synthetic_temporal_windows.csv"
    export_windows_csv(windows, output)
    print(f"\nExported {len(windows)} windows to {output}")


if __name__ == "__main__":
    main()
