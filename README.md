# Multi-Class Intent Classification via LoRA-Tuned Ministral-3b on Amazon MASSIVE Intent

This repository contains the full codebase and instructions for reproducing the experiments and results described in the accompanying technical report:
**"Multi-Class Intent Classification via LoRA-Tuned Ministral-3b on Amazon Massive Intent"**
Author: Joseph Guedalia

## Overview

This project demonstrates how a LoRA-tuned, instruction-following language model (`Ministral-3b-instruct`) can be adapted for efficient, multi-class intent classification. The system is trained and evaluated on the Amazon MASSIVE Intent dataset using the `mlx-lm` framework, and is fully reproducible on local Apple Silicon hardware.

---

## Table of Contents

* [Project Structure](#project-structure)
* [Requirements](#requirements)
* [Setup Instructions](#setup-instructions)
* [Downloading the Model](#downloading-the-model)
* [Data Preparation](#data-preparation)
* [Running Experiments](#running-experiments)
* [Evaluation and Visualization](#evaluation-and-visualization)
* [Reproducing Paper Results](#reproducing-paper-results)
* [Citation](#citation)

---

## Project Structure

```
.
├── analyze.py                # Label processing/analysis utilities
├── data_pull.py              # Downloads, filters, and splits dataset (run first)
├── embeddings.py             # Label embedding generation for analysis/visualization
├── evaluate.py               # Evaluates model performance on test set
├── experiment.py             # Orchestrates all training runs & evaluation (main entrypoint)
├── requirements.txt          # Python dependencies
├── train.py                  # Script for launching individual model training
├── try.py                    # Example script for manual inference/testing
├── vector_analysis.py        # Generates PCA and dendrogram visualizations
├── download_model.py         # Script to download Ministral-3b-instruct from Hugging Face
├── data/                     # Output folder for processed datasets
│   ├── train.jsonl
│   ├── valid.jsonl
│   └── test.jsonl
├── adapters/                 # Folder for LoRA adapter checkpoints (created after training)
├── results_/                 # Visualizations (PCA plots, dendrograms, etc.)
```

---

## Requirements

* Python 3.9+
* Apple Silicon (recommended for `mlx-lm` local acceleration)
* Required Python packages (see `requirements.txt`):

  * `datasets`
  * `pandas`
  * `scikit-learn`
  * `matplotlib`
  * `sentence-transformers`
  * `huggingface_hub` (for downloading model)
  * `mlx-lm`

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/JLG1234/NLP-Final-Project.git
   ```

2. **Create VirtualEnv:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install requirements:**

   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Install `mlx-lm`:**
   If not included in `requirements.txt`, follow [mlx-lm installation instructions](https://github.com/ml-explore/mlx-lm) for Apple Silicon.

---

## Downloading the Model

Before running experiments, download the `Ministral-3b-instruct` model from Hugging Face:

```bash
pip install huggingface_hub
python3 download_model.py
```

This script will download the model to `./models/Ministral-3b-instruct/`.

---

## Data Preparation

To download, filter, and split the Amazon MASSIVE Intent dataset, run:

```bash
python3 data_pull.py
```

* Outputs processed `train.jsonl`, `valid.jsonl`, and `test.jsonl` to the `data/` directory.

---

## Running Experiments

The main entry point for running and evaluating all experiments is:

```bash
python3 experiment.py
```

* This will train models with all experiment configurations defined in `experiment.py` (or just the best configuration, as specified).
* Training and evaluation logs are saved for each run.
* Adapter checkpoints are saved in the `adapters/` folder.

---

## Evaluation and Visualization

* **Model Evaluation:**
  Each experiment automatically runs `evaluate.py` after training to evaluate on the test set.
* **Label Embedding Analysis:**
  To generate the PCA and dendrogram visualizations shown in the report, run:

  ```bash
  python3 vector_analysis.py
  ```

  Outputs will be saved in the `results_/` directory.

---

## Manual Inference

To test the trained model interactively with your own input, run:

```bash
python3 try.py
```

You will be prompted to enter an utterance, and the model will return the predicted intent label (if found in the valid label set).

---

## Reproducing Paper Results

1. Run `download_model.py` to get the pretrained weights.
2. Run `data_pull.py` to prepare your data.
3. Run `experiment.py` to execute the fine-tuning and evaluation pipeline.
4. For manual runs or ablation studies, use `train.py` and `evaluate.py` directly with desired arguments.
5. For label analysis or figure reproduction, run `vector_analysis.py`.

**Note:**
All experiments use fixed random seeds for reproducibility. Ensure you have sufficient Apple Silicon GPU memory for larger batch sizes and longer training runs.

---

## Citation

If you use this code or report in your research, please cite:

```
@article{guedalia2025intentlora,
  title={Multi-Class Intent Classification via LoRA-Tuned Ministral-3b on Amazon Massive Intent},
  author={Joseph Guedalia},
  year={2025},
  note={Final Project, Baruch College, MTH 4250},
  url={https://github.com/JLG1234/NLP-Final-Project.git}
}
```
