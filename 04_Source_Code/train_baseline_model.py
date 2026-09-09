"""
train_baseline_model.py
------------------------
Preliminary baseline classifier for the proposed NIDS research (Group F).

This trains a Random Forest classifier — the "lightweight ML baseline"
referenced in Chapter 3.7 (Proposed Evaluation Plan) of the Research
Proposal. It is used as one of two comparison points (the other being a
deep-learning baseline, to be added in a later iteration) against which the
final proposed hybrid ML/DL model will be evaluated.

Run after preprocess.py has generated the processed .npy arrays.
"""

import argparse
import os
import time
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)


def load_processed(data_dir: str):
    X_train = np.load(os.path.join(data_dir, "X_train.npy"))
    X_test = np.load(os.path.join(data_dir, "X_test.npy"))
    y_train = np.load(os.path.join(data_dir, "y_train.npy"))
    y_test = np.load(os.path.join(data_dir, "y_test.npy"))
    return X_train, X_test, y_train, y_test


def main():
    parser = argparse.ArgumentParser(description="Train baseline Random Forest NIDS classifier.")
    parser.add_argument("--data-dir", default="./processed", help="Directory with processed .npy arrays")
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--output", default="../06_Results_or_Expected_Output/baseline_metrics.json")
    args = parser.parse_args()

    X_train, X_test, y_train, y_test = load_processed(args.data_dir)

    model = RandomForestClassifier(n_estimators=args.n_estimators, random_state=42, n_jobs=-1)

    start = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - start

    start = time.time()
    y_pred = model.predict(X_test)
    inference_time = time.time() - start

    metrics = {
        "model": "RandomForest (baseline)",
        "n_estimators": args.n_estimators,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision_macro": precision_score(y_test, y_pred, average="macro", zero_division=0),
        "recall_macro": recall_score(y_test, y_pred, average="macro", zero_division=0),
        "f1_macro": f1_score(y_test, y_pred, average="macro", zero_division=0),
        "train_time_seconds": train_time,
        "inference_time_seconds": inference_time,
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
    }

    print(classification_report(y_test, y_pred, zero_division=0))
    print(f"[RESULT] Accuracy={metrics['accuracy']:.4f}  F1(macro)={metrics['f1_macro']:.4f}  "
          f"Train time={train_time:.2f}s  Inference time={inference_time:.4f}s")

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"[DONE] Metrics saved to {args.output}")


if __name__ == "__main__":
    main()
