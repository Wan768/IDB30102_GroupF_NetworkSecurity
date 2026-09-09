# 04_Source_Code

## Status
This folder contains working preliminary code demonstrating the intended preprocessing and baseline classification pipeline described in Chapter 3 of the Research Proposal. Per lecturer clarification, a complete/final system is not required at this stage — these scripts are illustrative of technical feasibility and direction only.

## Contents
- `preprocess.py` — loads, cleans, encodes and scales network traffic data; splits into train/test sets.
- `train_baseline_model.py` — trains a Random Forest baseline classifier and outputs accuracy/precision/recall/F1/inference-time metrics.
- `requirements.txt` — Python dependencies.

## How to Run
1. `pip install -r requirements.txt`
2. `python preprocess.py --input ../05_Data_or_Sample_Input/sample_traffic.csv --label-col label`
3. `python train_baseline_model.py`

## Attribution
These scripts are original work written by the group for this research proposal. They use the following open-source Python libraries (not modified or redistributed, only imported as dependencies):
- **scikit-learn** (BSD 3-Clause License) — https://scikit-learn.org
- **pandas** (BSD 3-Clause License) — https://pandas.pydata.org
- **numpy** (BSD 3-Clause License) — https://numpy.org

No third-party source code has been copied or adapted into these scripts.
