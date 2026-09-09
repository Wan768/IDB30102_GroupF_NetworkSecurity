| Framework Module | Core Components & Technologies | Primary Objective |
| --- | --- | --- |
| **Data Ingestion & Pre-processing** | `Scapy`, `Pandas`, `NumPy`, `Scikit-Learn` (`MinMaxScaler`) | Ingest raw PCAP packet streams or benchmark datasets (CICIDS2017, NSL-KDD, UNSW-NB15), clean missing/infinite values, and scale feature values to a $[0, 1]$ range. |
| **Feature Optimization Module** | LightGBM Gini Importance Selector | Compute feature importance scores and select top-$K$ discriminative features (trimming from 70+ down to 15–20 attributes) to reduce processing overhead. |
| **Shallow 1D-CNN Engine** | `PyTorch` / `TensorFlow` (`Conv1D`, `MaxPooling1D`, `Dropout`, `Dense`) | Capture spatial and non-linear attack signatures from 1D feature vectors in a single fast forward pass, keeping memory footprint low. |
| **Classification & Decision Layer** | `Softmax` Activation Layer | Compute multi-class threat probability vectors to classify traffic into Benign, DoS, Botnet, or Brute Force categories. |
| **Evaluation & Benchmarking Framework** | `Scikit-Learn`, Custom Metrics Logger, `psutil` | Benchmark detection Accuracy, Precision, Recall, F1-Score, False Positive Rate (FPR), and per-packet Inference Latency against Random Forest and CNN-LSTM baselines.
|
