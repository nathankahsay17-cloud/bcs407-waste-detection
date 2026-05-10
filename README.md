# AI-Based Smart Waste Detection System for Campus Sustainability

This repository contains the code, selected result files, and supporting materials for the BCS407 Artificial Intelligence project on smart waste detection for campus sustainability monitoring.

## Project Overview

This project focuses on detecting four waste categories using computer vision:

- cardboard
- metal
- paper
- plastic

The system was first developed in Project 1 using YOLOv8n as the baseline model. In Project 2, the baseline was improved through controlled experiments to evaluate different strategies for better detection performance.

## Project 2 Improvement Strategies

The following official experiments were conducted:

1. **Baseline**
   - YOLOv8n on the original Project 1 dataset

2. **Experiment 1 – Model Upgrade**
   - YOLOv8m on the original dataset

3. **Experiment 2 – Dataset Expansion**
   - YOLOv8n on an expanded dataset with additional paper and cardboard images

4. **Final Combined Model**
   - YOLOv8m on the expanded dataset

## Final Official Results

| Run | Strategy | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|---|---|---:|---:|---:|---:|
| Baseline | Project 1 YOLOv8n | 0.8480 | 0.7855 | 0.8686 | 0.7230 |
| Experiment 1 | YOLOv8m | 0.8159 | 0.8070 | 0.8675 | 0.7309 |
| Experiment 2 | Added more paper and cardboard images | 0.8390 | 0.7948 | 0.8857 | 0.7392 |
| Final Combined | YOLOv8m + added more paper/cardboard images | 0.7642 | 0.8431 | 0.8640 | 0.7337 |

**Best overall model:** Experiment 2 (targeted dataset expansion)

## Files Included

- `training_code.py` – baseline training script
- `Prediction.ipynb` – inference / prediction notebook
- `data.yaml` – dataset configuration file
- `results.png` – baseline training results
- `confusion_matrix.png` – baseline confusion matrix
- `experiment_log.csv` – summary of Project 2 runs and results
- `auto_label.py` – OpenCV-based semi-automated labeling script


## Dataset and Trained Model

The dataset and trained model files are hosted externally due to file size limits.

- **Dataset link:** https://drive.google.com/drive/folders/1KM5PWC0Mcpt3G7bqdWoyNpOEuxe37t08?us
p=sharing


## How Labeling Was Done

Labeling was completed using a combination of:

- **LabelImg** for manual annotation and review
- a **Python + OpenCV auto-labeling script** for images containing one main object on a relatively simple background

The script:
1. loads the image
2. converts it to grayscale
3. applies Gaussian blur
4. uses Otsu thresholding
5. detects the largest contour
6. creates a bounding box
7. saves the annotation in YOLO `.txt` format

Generated labels were reviewed and corrected when needed.

## How to Run

### Install dependencies
```bash
pip install ultralytics opencv-python
