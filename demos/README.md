# Public-Safe Computer Vision Demos

These demos are written specifically for public portfolio use. They reproduce **general engineering ideas** from my research background without using confidential datasets, source code, trained models, annotations, internal paths, unpublished results, or collaborator-owned material.

## `animal_behavior_pipeline_demo.py`

A small synthetic example showing how long-form video observations can be transformed into temporally stable research samples.

### Demonstrated concepts

- noisy per-frame identity evidence
- bounded temporal identity history
- confidence-aware identity stabilization
- per-track temporal windows
- simple motion descriptors
- structured CSV export for downstream modelling

### Run

```bash
python demos/animal_behavior_pipeline_demo.py
```

The script requires only the Python standard library.

### Why this is relevant

In real multi-camera behaviour-analysis systems, a detector's output is only the beginning. Downstream research often needs identity stabilization, temporal context, event extraction, quality filtering and structured data generation before an action-recognition model can be trained reliably.

This demo intentionally keeps those concepts visible and testable without reproducing confidential research implementation.

## Confidentiality statement

The active Mitacs research project described in my portfolio is not open-sourced. Public code here is independently written from scratch for demonstration purposes.
