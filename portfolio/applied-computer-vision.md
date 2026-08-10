# Applied Computer Vision Portfolio

This page summarizes selected engineering projects that complement my current research work in video understanding and behavioural analysis.

> Some original projects were completed in industrial settings. Public descriptions focus on the transferable engineering work and intentionally omit proprietary customer data, production assets, credentials, trained production models, and internal deployment details.

## 1. Real-Time Industrial Quality Control

**Goal:** detect and reject visual defects on laser-marked parts under production constraints.

### What I worked on

- industrial-camera vision pipeline from acquisition to decision;
- YOLO-based region / object detection;
- OpenCV validation of geometry and position;
- colour-difference and appearance checks;
- OCR-oriented readability checks;
- GPU deployment and latency optimization;
- integration mindset for industrial stop / acknowledgement / restart logic.

### Engineering lesson

The project required combining learned detection with deterministic validation. A production vision system must produce a reliable decision, not merely a bounding box.

**Repository:** [quality-control](https://github.com/Rostom-Ben-Abdallah/quality-control)

---

## 2. Multi-Camera Recognition and IN/OUT Analytics

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

The original deployment code is not highlighted as a portfolio artifact because it contains environment-specific integration details. The transferable concepts are described here instead.

---

## 3. Real-Time Tracking and Counting for Automated Medication Handling

**Goal:** detect, segment, track and count tablets / vials reliably while avoiding duplicate counts.

### What I worked on

- on-site video collection;
- polygon dataset annotation;
- YOLO segmentation fine-tuning;
- ByteTrack tracking;
- ROI crossing / counting logic;
- hysteresis and ID filters;
- PyQt operator interface;
- annotated-video and Excel result export.

### Engineering lesson

Counting accuracy depends heavily on state logic around the tracker. Robust event logic is often as important as the detector itself.

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

## 5. LLM + Robot Perception Experiment

A public ROS 2 experiment combines natural-language commands, TurtleBot3 simulation, YOLO-based scene understanding and local LLM inference.

**Repository:** [llm_teleop_turtlebot3](https://github.com/Rostom-Ben-Abdallah/llm_teleop_turtlebot3)

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
