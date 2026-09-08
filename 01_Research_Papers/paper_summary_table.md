# Research Papers Summary

## Theme: Deep Learning & Hybrid Architectures 

### Paper 1
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
| **Citation (APA 7th)** | Hnamte, V., & Hussain, J. (2023). DCNNBiLSTM: An efficient hybrid deep learning-based intrusion detection system. *Telematics and Informatics Reports*, 10, 100053. https://www.sciencedirect.com/science/article/pii/S2772503023000130 |

### Paper 2
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Network Intrusion Detection Based on Feature Image and Deformable Vision Transformer Classification |
| **Author(s)** | Kan He, Wei Zhang, Xuejun Zong, Lian Lian |
| **Year** | 2024 |
| **Research Problem** | Existing NIDS exhibit subpar detection effectiveness against evolving attacks, while traditional deep learning models struggle with long-range dependencies, high computational costs, and severe class imbalance. |
| **Method / Technique** | Deformable Vision Transformer (DE-VIT) — converts 1D network features into 8x8 feature images, applies deformable convolution to expand the receptive field, utilizes a deformable multi-head attention mechanism to focus dynamically on key regions, and employs a Layered Focal (L-Focal) loss function. |
| **Dataset / Tools** | CIC-IDS2017 and UNSW-NB15 datasets; preprocessing via one-hot encoding, cleaning NaN/INF values, normalization, and reshaping into 8x8 image matrices. |
| **Main Findings** | Surpassed DBN-KELM, achieving 99.5% accuracy on CIC-IDS2017 (8.5% improvement) and 97.25% on UNSW-NB15 (9.1% improvement) in binary classification, with strong multi-class performance across imbalanced attack categories. |
| **Limitation** | Performance and precision decrease rapidly in minority categories with very few samples; computational overhead remains higher than lightweight traditional machine learning models. |
| **Relevance to Proposed Research** | Directly supports RO1 and RO2 by demonstrating an alternative vision-based transformation for tabular network traffic and validating attention mechanisms for NIDS feature representation. |
| **Citation (APA 7th)** | He, K., Zhang, W., Zong, X., & Lian, L. (2024). Network intrusion detection based on feature image and deformable vision transformer classification. *IEEE Access*, 12, 44335-44350. https://doi.org/10.1109/ACCESS.2024.3376434 |
