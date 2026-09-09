"""
preprocess.py
-------------
Preliminary data preprocessing script for the proposed Lightweight Hybrid
ML/DL Intrusion Detection System (Group F).

This script demonstrates the intended preprocessing pipeline described in
Chapter 3 of the Research Proposal:
  1. Load raw network traffic data (CSV format, e.g., NSL-KDD / CICIDS2017 style)
  2. Clean missing/duplicate records
  3. Encode categorical features (one-hot encoding)
  4. Normalise numeric features (standard scaling)
  5. Split into train/test sets
  6. Save the processed arrays for use by train_baseline_model.py

NOTE: This is a preliminary/prototype-stage script as required by the
Assignment 2 brief. It is written to run on the small sample file in
05_Data_or_Sample_Input/sample_traffic.csv, and is designed to also work
on the full benchmark datasets (CICIDS2017 / NSL-KDD / UNSW-NB15) once
downloaded from their official sources (see 05_Data_or_Sample_Input/README.md).
"""

import argparse
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV traffic dataset."""
    df = pd.read_csv(path)
    print(f"[INFO] Loaded {path} -> shape={df.shape}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates and rows with missing values (per Chapter 3.6)."""
    before = len(df)
    df = df.drop_duplicates()
    df = df.dropna()
    print(f"[INFO] Cleaned data: {before} -> {len(df)} rows")
    return df


def encode_and_scale(df: pd.DataFrame, label_col: str):
    """One-hot encode categorical features and standard-scale numeric features."""
    y_raw = df[label_col]
    X = df.drop(columns=[label_col])

    cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
    if cat_cols:
        X = pd.get_dummies(X, columns=cat_cols)
        print(f"[INFO] One-hot encoded categorical columns: {cat_cols}")

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y_raw)
    print(f"[INFO] Encoded labels: {dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))}")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, list(X.columns), label_encoder


def main():
    parser = argparse.ArgumentParser(description="Preprocess network traffic data for NIDS prototype.")
    parser.add_argument("--input", default="../05_Data_or_Sample_Input/sample_traffic.csv",
                         help="Path to input CSV file")
    parser.add_argument("--label-col", default="label", help="Name of the label column")
    parser.add_argument("--output-dir", default="./processed", help="Where to save processed arrays")
    parser.add_argument("--test-size", type=float, default=0.2)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    df = load_data(args.input)
    df = clean_data(df)
    X, y, feature_names, label_encoder = encode_and_scale(df, args.label_col)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=42, stratify=y
    )

    np.save(os.path.join(args.output_dir, "X_train.npy"), X_train)
    np.save(os.path.join(args.output_dir, "X_test.npy"), X_test)
    np.save(os.path.join(args.output_dir, "y_train.npy"), y_train)
    np.save(os.path.join(args.output_dir, "y_test.npy"), y_test)

    print(f"[DONE] Train shape: {X_train.shape}, Test shape: {X_test.shape}")
    print(f"[DONE] Processed arrays saved to {args.output_dir}/")


if __name__ == "__main__":
    main()
