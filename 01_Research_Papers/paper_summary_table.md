# Research Papers Summary


## Paper 1
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | DCNNBiLSTM: An Efficient Hybrid Deep Learning-Based Intrusion Detection System |
| **Author(s)** | Vanlalruata Hnamte, Jamal Hussain |
| **Year** | 2023 |
| **Research Problem** | Existing NIDS struggle to detect new/evolving attack patterns; most prior deep-learning IDS studies use outdated or single datasets, limiting real-world reliability. |
| **Method / Technique** | Hybrid DCNNBiLSTM — 1D CNN layers for feature extraction, Bidirectional LSTM for sequence/temporal pattern learning, DNN layers for classification. Compared against standalone DNN, CNN, LSTM and Autoencoder models. |
| **Dataset / Tools** | CICIDS2018 (DDoS-LOIC-UDP-HOIC) and Edge_IIoT datasets; preprocessing via one-hot encoding, standard scaling, and SMOTE (for class imbalance on Edge_IIoT). |
| **Main Findings** | Achieved 100% accuracy on CICIDS2018 and 99.64% accuracy on Edge_IIoT (multiclass classification), outperforming standalone DNN, CNN, LSTM and AE baselines and prior published models. |
| **Limitation** | Higher training/inference time and computational cost than single models due to architectural complexity; not yet tested for real-time deployment or zero-day attack scenarios. |
| **Relevance to Proposed Research** | Directly supports RO1 and RO2 — provides empirical evidence that hybrid CNN+DL architectures outperform single models, but also confirms the accuracy-vs-efficiency trade-off your proposal aims to address with a lightweight hybrid design. |
| **Citation (APA 7th)** | Hnamte, V., & Hussain, J. (2023). DCNNBiLSTM: An efficient hybrid deep learning-based intrusion detection system. *Telematics and Informatics Reports*, 10, 100053. https://doi.org/10.1016/j.teler.2023.100053 |
