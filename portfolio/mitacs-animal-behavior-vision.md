# Research Case Study — Multi-Camera Computer Vision for Animal Behaviour Understanding

## Overview

During my Mitacs research internship at **Université de Moncton**, I have been developing an end-to-end visual AI pipeline for automated behavioural monitoring of vervet monkeys from synchronized video.

The research problem is substantially harder than frame-level object detection. The system must maintain reliable animal identities over time, reason across multiple camera views, handle occlusion and appearance changes, preserve annotation quality, and convert short temporal sequences into behaviour labels suitable for scientific analysis.

> **Confidentiality:** This case study intentionally describes architecture, engineering decisions, and research skills at a high level. Original videos, annotations, trained weights, unpublished metrics, internal source code, infrastructure identifiers, credentials, and collaborator-owned assets are not published.

## Research problem

Given long-form multi-camera video containing multiple visually similar animals, build a reproducible pipeline that can:

1. detect animals reliably;
2. maintain temporal tracks;
3. associate tracks with individual identities;
4. use multiple visual cues when identity is ambiguous;
5. prepare high-quality temporal training examples;
6. classify behaviour from video rather than isolated frames;
7. expose results to human reviewers and downstream behavioural analysis.

## System architecture

```text
Synchronized camera video
          |
          v
   Body / object detection
          |
          v
   Multi-object tracking
          |
          +----------------------+
          |                      |
          v                      v
  Visual identity cues      Segmentation / pose
          |                      |
          +----------+-----------+
                     |
                     v
          Temporal identity fusion
                     |
                     v
       Candidate event extraction
                     |
                     v
       Dataset quality / review
                     |
                     v
       Temporal action recognition
                     |
                     v
      Structured research outputs
```

## My contributions

### Detection and model evaluation

- Built and evaluated modern object-detection pipelines for difficult animal imagery.
- Compared detector families and failure modes instead of relying on a single model.
- Worked with YOLO-family detectors, RF-DETR, GroundingDINO and segmentation-based tools.

### Multi-object tracking and identity

- Integrated tracking and identity logic for long-form video.
- Worked on temporal stabilization to reduce identity switching and short-lived assignment errors.
- Used individual visual cues and cross-camera evidence when a single observation was insufficient.
- Designed conservative handling for ambiguous identity rather than forcing low-confidence labels.

### Dataset engineering

- Built large video-derived datasets and quality-control workflows.
- Prepared temporally aligned behaviour clips for action-recognition experiments.
- Designed review procedures to identify incorrect identity, poor visibility, action mismatch and unsuitable examples.
- Preserved scientifically provided behaviour labels while using AI models only for localization / identity support and review.

### Video-based behaviour recognition

The behaviour-recognition stage treats activity as a **temporal** problem. Short clips are prepared around annotated events so that models can use motion, pose, identity and temporal context instead of inferring behaviour from one frame.

Research directions include:

- temporal video representations;
- action recognition;
- pose-informed behaviour modelling;
- multi-view evidence;
- identity-aware temporal features.

### HPC and reproducible processing

- Used Linux HPC infrastructure and Slurm-based jobs for large-scale processing.
- Built repeatable workflows for detection, tracking, annotation preparation and model benchmarking.
- Worked with GPU-accelerated inference and large video collections where local processing alone is impractical.

### Human-in-the-loop tooling

I also designed tooling for reviewing model outputs and behaviour segments, including workflows for visual verification and structured export. This reflects an important principle of the project: for scientific data, automation should make uncertainty reviewable rather than hide it.

## Technologies used / evaluated

`Python` · `OpenCV` · `PyTorch` · `YOLO` · `RF-DETR` · `GroundingDINO` · `SAM` · `Qwen VLM` · tracking / Re-ID methods · `CUDA` · `Linux` · `Slurm/HPC` · web-based review tooling

## What this project taught me

The main lesson has been that successful applied computer vision is not determined by detector accuracy alone. Real systems require careful work on identity, temporal consistency, dataset quality, uncertainty, reproducibility, evaluation and human review.

This experience is the reason I am particularly interested in graduate research involving:

- animal and human behaviour understanding;
- action recognition and temporal video modelling;
- multi-object / multi-camera tracking;
- re-identification and identity-aware perception;
- multimodal visual reasoning;
- robust perception for real-world scientific and robotic systems.

## Public demonstration strategy

Because the active research project is confidential, any future public code demonstration will reproduce the **general engineering concepts** using independently written code and public or synthetic data. It will not contain research data or implementation copied from the original project.

---

**Rostom Ben Abdallah**  
Mitacs Research Intern — Université de Moncton  
Industrial Computer Engineering — ENET'Com
