# Applied Computer Vision Portfolio

This page summarizes selected engineering projects that complement my current research work in video understanding and behavioural analysis.

> Some original projects were completed in industrial settings. Public descriptions focus on transferable engineering work and intentionally omit proprietary customer data, production assets, credentials, trained production models, and internal deployment details.

## 1. Industrial Vision: Quality Control, Segmentation & Counting

**Repository:** [industrial-vision-quality-control](https://github.com/Rostom-Ben-Abdallah/industrial-vision-quality-control)

This repository now contains short demo videos and public-safe implementations for three applied vision systems.

### Bottle segmentation, counting & cap-quality inspection

**Goal:** segment and track bottles, count each object once, associate cap detections and classify bottle quality.

**Public project:** [bottle-cap-inspection](https://github.com/Rostom-Ben-Abdallah/industrial-vision-quality-control/tree/main/projects/bottle-cap-inspection)

Key ideas:

- YOLO instance segmentation;
- persistent tracking with BoT-SORT;
- line-crossing count by track ID;
- bottle/cap association;
- expected cap-colour validation;
- OK / NG decisions;
- throughput, latency and yield overlays.

### Laser-marking quality control

**Goal:** detect and reject visual defects on laser-marked parts under production constraints.

**Public project:** [laser-marking-quality-control](https://github.com/Rostom-Ben-Abdallah/industrial-vision-quality-control/tree/main/projects/laser-marking-quality-control)

What I worked on:

- industrial-camera vision pipeline from acquisition to decision;
- YOLO-based region / object detection;
- OpenCV geometry and position validation;
- colour-difference / DeltaE2000 checks;
- OCR-oriented readability checks;
- GPU deployment and latency optimization;
- industrial stop / acknowledgement / restart logic.

The public code provides a configurable OCR + expected-position + CIEDE2000 inspection pipeline and structured PASS/FAIL reporting.

### Medication segmentation & counting

**Goal:** detect, segment, track and count medication packages / objects reliably while avoiding duplicate counts.

**Public project page:** [medication-counting](https://github.com/Rostom-Ben-Abdallah/industrial-vision-quality-control/tree/main/projects/medication-counting)

What I worked on:

- on-site video collection;
- polygon dataset annotation;
- YOLOv11-seg fine-tuning;
- ByteTrack tracking;
- ROI crossing / counting logic;
- hysteresis and ID filters;
- PyQt operator interface;
- annotated-video and Excel result export.

The demo is public; original deployment code, customer configuration, weights and production data remain private.

### Engineering lesson

A production vision system must produce a repeatable **event or decision**, not merely a bounding box. Tracking state, temporal logic, validation rules, latency and operator workflow are often as important as raw detector accuracy.

---

## 2. Multi-Camera Recognition and IN/OUT Analytics

**Repository:** [multicamera-tracking-reid](https://github.com/Rostom-Ben-Abdallah/multicamera-tracking-reid)

**Goal:** analyse doorway traffic using multiple cameras while preserving identity through difficult viewpoints and occlusion.

### Technical ideas

- YOLO person detection;
- multi-object tracking;
- OSNet-style re-identification;
- face embeddings with InsightFace;
- ROI and event-state logic;
- identity filtering and temporal persistence;
- real-time camera integration.

### Engineering lesson

Identity is a temporal systems problem. Detection, tracking, recognition, state transitions and uncertainty handling must work together to avoid duplicate or incorrect events.

---

## 3. SafeVision — Multi-Camera Safety Perception

**Repository:** [safevision-multicamera-vision](https://github.com/Rostom-Ben-Abdallah/safevision-multicamera-vision)

A multi-camera safety-monitoring prototype combining:

- YOLO object detection and tracking;
- pose / fall reasoning;
- face-landmark / local-region analysis;
- real-time event logic;
- WebSocket alert streaming;
- augmented-reality visualization.

This project demonstrates end-to-end integration from camera perception to a downstream interactive client.

---

## 4. Edge AI Poultry Counting

**Goal:** count poultry on a production line using a compact vision stack suitable for edge hardware.

### What I worked on

- dataset creation and annotation;
- YOLO detection;
- BoT-SORT tracking;
- IN/OUT event logic;
- ONNX export;
- Raspberry Pi 4 evaluation;
- latency / FPS optimization;
- MariaDB logging for KPI reporting.

### Engineering lesson

Model accuracy, computational budget and event-level reliability must be balanced when deploying computer vision on constrained hardware.

---

## 5. Robot Vision + LLM Teleoperation

**Repository:** [robot-vision-llm-teleop](https://github.com/Rostom-Ben-Abdallah/robot-vision-llm-teleop)

A ROS 2 experiment combining natural-language commands, TurtleBot3 simulation, YOLO-based scene understanding and local LLM inference.

This project reflects my broader interest in moving from passive visual recognition toward intelligent systems that use perception to reason and act.

---

## Common themes across my work

Across research and industrial projects, I repeatedly work on the full chain:

```text
Data collection
   -> annotation
   -> model training / benchmarking
   -> detection / segmentation
   -> tracking / identity
   -> temporal logic
   -> decision or behaviour output
   -> visualization / operator review
   -> deployment
```

My strongest research interests are therefore not limited to one detector architecture. I am especially interested in **video understanding, tracking, re-identification, action recognition, multimodal perception, robotic perception, and reliable real-world deployment**.

---

**Rostom Ben Abdallah**  
Industrial Computer Engineering · Computer Vision / Visual AI
