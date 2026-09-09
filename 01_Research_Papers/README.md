# Research Papers Summary

## Theme 1: Deep Learning & Hybrid Architectures 

### Paper 1
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Zero-Touch Network Security (ZTNS): A Network Intrusion Detection System Based on Deep Learning |
| **Author(s)** | Emad-Ul-Haq Qazi, Tanveer Zia, Muhammad Hamza Faheem, Khurram Shahzad, Muhammad Imran, Zeeshan Ahmed |
| **Year** | 2024 |
| **Research Problem** | Emerging zero-touch networks (ZTN) in smart cities autonomously manage massive IoT traffic but face critical security vulnerabilities from stealthy and large-scale attacks (e.g., DDoS, Botnets, Brute Force, Infiltration) without human intervention. |
| **Method / Technique** | DL-NIDS-ZTN — a multi-layer 1D Convolutional Neural Network (CNN) architecture with 5 sequential layers (Conv1D, Dropout, Max-Pooling, Flatten, Dense layers) using ReLU activation and a Sigmoid output classifier for binary classification. |
| **Dataset / Tools** | CSE-CIC-IDS2018 dataset; preprocessing via data cleaning, missing value removal, Chi-square attribute relevance analysis, feature selection down to key flow features, normalization, and a 70:30 train-test split. |
| **Main Findings** | Achieved 99.80% detection accuracy, 99.0% precision, and a test loss of 0.0019 on CICIDS-2018, outperforming prior ensemble and hybrid architectures like Cu-LSTMGRU (98%) and CNN-LSTM (90.88%). |
| **Limitation** | Evaluated solely for binary classification (normal vs. malicious) rather than granular multi-class categorization; evaluated only on a single benchmark dataset without real-world zero-touch network latency measurements. |
| **Relevance to Proposed Research** | Directly supports RO1 and RO2 — demonstrates how standard 1D CNN architectures can achieve near-perfect binary intrusion detection accuracy on modern flow datasets while providing a baseline for network traffic feature selection. |
| **Citation (APA 7th)** | Qazi, E.-U.-H., Zia, T., Faheem, M. H., Shahzad, K., Imran, M., & Ahmed, Z. (2024). Zero-touch network security (ZTNS): A network intrusion detection system based on deep learning. *IEEE Access*, 12, 141625-141639. https://doi.org/10.1109/ACCESS.2024.3466470 |
| **License** | CC BY-NC-ND 4.0 — open access, non-commercial redistribution permitted with attribution |


## Theme 2: Deep Learning & Hybrid Architectures 

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
| **License** | CC BY 4.0 — open access, redistribution permitted with attribution |

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
| **License** | CC BY 4.0 — open access, redistribution permitted with attribution |


## Theme 3:  IoT and Industrial IoT Security

### Paper 1
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Enhanced Intrusion Detection System Using Hybrid-Inspired Algorithms and Conditional Generative Adversarial Networks for Internet of Things Security |
| **Author(s)** | Shahab Wahhab Kareem |
| **Year** | 2025 |
| **Research Problem** | IoT network traffic data is highly complex and severely imbalanced, causing conventional intrusion detection systems to suffer from poor detection accuracy, low minority-class recall, and high false positive rates. |
| **Method / Technique** | A three-stage hybrid IDS framework: (1) Data cleaning, one-hot encoding, and min-max scaling; (2) Dual-discriminator Conditional GAN (CGAN) for high-quality synthetic data generation of underrepresented attack classes; (3) Bio-inspired hybrid feature selection combining Crocodile Hunting Search (CHS), Bee Optimization (BO), and Recursive Feature Elimination (RFE), evaluated across XGBoost, LightGBM, DNN, SVM, and DT classifiers. |
| **Dataset / Tools** | Bot-IoT dataset (TCP/UDP DDoS and normal traffic); implemented using TensorFlow 2.0 on an NVIDIA RTX 3090 GPU. |
| **Main Findings** | The DNN classifier with dual-CGAN and CHS-BO-RFE feature selection achieved the highest performance: 98.7% accuracy, 98.8% precision, 98.6% recall, 98.7% F1-score, 0.992 AUC, and a low False Positive Rate (FPR) of 1.3%, outperforming existing GAN variants like Self-Attention CGAN (96.4%) and Dual-Ensemble CTGAN (95.9%). |
| **Limitation** | High offline training complexity (~45 min for CGAN, ~90 min for feature selection on high-end hardware); batch offline training not yet adapted for real-time dynamic online model updating; evaluated only on the Bot-IoT dataset. |
| **Relevance to Proposed Research** | Directly supports RO1 and RO2 — proves that generative adversarial synthetic data augmentation effectively overcomes class imbalance in network traffic, while demonstrating an advanced meta-heuristic approach for feature subset selection. |
| **Citation (APA 7th)** | Kareem, S. W. (2025). Enhanced intrusion detection system using hybrid-inspired algorithms and conditional generative adversarial networks for Internet of Things security. *Egyptian Informatics Journal*, 31, 100763. https://doi.org/10.1016/j.eij.2025.100763 |
| **License** | CC BY-NC-ND 4.0 — open access, non-commercial redistribution permitted with attribution |

### Paper 2
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Multi-Attack Intrusion Detection System for Software-Defined Internet of Things Network |
| **Author(s)** | Tarcízio Ferrão, Franklin Manene, Adeyemi Abel Ajibesin |
| **Year** | 2023 |
| **Research Problem** | Software-Defined IoT (SDN-IoT) networks are highly susceptible to diverse network intrusions due to centralized control planes, while existing NIDS schemes suffer from high false alarm rates (false positives and false negatives) that disrupt legitimate traffic. |
| **Method / Technique** | Multi-Attack Intrusion Detection System (MAIDS) — a dual-algorithm machine learning framework combining XGBoost and Random Forest (RF) with a decision-fusion mechanism to cross-verify traffic classifications and suppress false alarms, coupled with SHAP (SHapley Additive exPlanations) for feature selection. |
| **Dataset / Tools** | NSL-KDD (108,400 logs) and CICIDS2017 datasets; evaluated across XGBoost, Random Forest, K-Nearest Neighbor (KNN), Support Vector Machine (SVM), and Logistic Regression (LR). |
| **Main Findings** | XGBoost and RF achieved top classification accuracies of 99.96% on CICIDS2017 and 99.81% on NSL-KDD; the MAIDS dual-verification scheme reduced the False Alarm Rate (FAR) by 33.23% (FPR reduced to 0.002% and FNR to 0.021% on CICIDS2017) with rapid testing latencies (0.03s–0.04s). |
| **Limitation** | Evaluated on static offline benchmark PCAP datasets rather than in a dynamic, physical OpenFlow SDN hardware testbed under live high-throughput traffic saturation. |
| **Relevance to Proposed Research** | Directly supports RO1 and RO3 — demonstrates how dual-model consensus mechanisms effectively minimize False Positive and False Negative rates, providing a benchmark for lightweight real-time traffic filtering in programmable networks. |
| **Citation (APA 7th)** | Ferrão, T., Manene, F., & Ajibesin, A. A. (2023). Multi-attack intrusion detection system for software-defined internet of things network. *Computers, Materials & Continua*, 75(3), 4985–5007. https://doi.org/10.32604/cmc.2023.038276 |
| **License** | CC BY 4.0 — open access, redistribution permitted with attribution |

### Paper 3
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Enhancing IoT Network Security Through Deep Learning-Powered Intrusion Detection System |
| **Author(s)** | Shahid Allah Bakhsh, Muhammad Almas Khan, Fawad Ahmed, Mohammed S. Alshehri, Hisham Ali, Jawad Ahmad |
| **Year** | 2023 |
| **Research Problem** | Proliferating IoT networks face severe computational overhead and architectural limitations that prevent conventional intrusion detection systems from effectively mitigating complex, dynamic cyber threats and DDoS attacks. |
| **Method / Technique** | Deep learning-based IDS benchmarking three neural architectures: Feed Forward Neural Networks (FFNN), Long Short-Term Memory (LSTM), and Random Neural Networks (RandNN); feature engineering pipeline uses SMOTE for data balancing and Principal Component Analysis (PCA) for dimensionality reduction. |
| **Dataset / Tools** | CIC-IoT2022 dataset (476,111 records covering 60 profiled IoT devices across DoS floods, Brute Force, and RTSP attacks); processed via CICFlowMeter 4.0, Keras, and scikit-learn on Python 3.10. |
| **Main Findings** | The optimized FFNN model achieved the highest performance with 99.93% accuracy, 99.93% precision, 99.93% recall, and 99.93% F1-score for binary classification, and 98.72% accuracy for multiclass classification; LSTM attained 99.89% binary accuracy, while RandNN achieved 96.42% accuracy with lightweight distributed potential. |
| **Limitation** | Deep learning models require extensive computational resources and prolonged training times (e.g., multiclass FFNN required >10,000s training latency), limiting direct training on resource-constrained edge devices. |
| **Relevance to Proposed Research** | Directly supports RO1, RO2, and RO3 — provides empirical benchmarking across standard neural networks (FFNN vs. LSTM) and demonstrates an effective PCA dimensionality reduction workflow on the modern CIC-IoT2022 traffic benchmark. |
| **Citation (APA 7th)** | Bakhsh, S. A., Khan, M. A., Ahmed, F., Alshehri, M. S., Ali, H., & Ahmad, J. (2023). Enhancing IoT network security through deep learning-powered intrusion detection system. *Internet of Things*, 24, 100936. https://doi.org/10.1016/j.iot.2023.100936 |
| **License** | CC BY 4.0 — open access, redistribution permitted with attribution |

### Paper 4
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Design of Industrial IoT Intrusion Security Detection System Based on LightGBM Feature Algorithm and Multi-layer Perception Network |
| **Author(s)** | Yongsheng Deng |
| **Year** | 2024 |
| **Research Problem** | Industrial Internet of Things (IIoT) and Industrial Control Systems (ICS) face escalating intrusion threats; existing NIDS struggle to maintain a balance between detection accuracy and real-time processing constraints in high-dimensional traffic environments. |
| **Method / Technique** | Hybrid LightGBM and Multi-Layer Perceptron (MLP) — uses LightGBM (Leaf-wise tree growth with depth constraints, GOSS, and EFB) for feature selection and importance threshold filtering (>0.1), integrated with an MLP neural network for nonlinear classification. Compared against Decision Tree, Random Forest, XGBoost, k-NN, and SVM. |
| **Dataset / Tools** | KDD CUP 99, NSL-KDD, and UNSW-NB15 datasets; preprocessing includes Z-score attribute standardization, missing-value imputation, and categorical feature encoding (One-Hot / Label encoding) with an 80:20 train-test split. |
| **Main Findings** | Achieved 96.2% accuracy, 97.4% precision, 95.6% recall, 96.5% F1-score, and an AUC of 0.98, outperforming Decision Trees (90.6% accuracy) and SVM (0.93 AUC) with an acceptable inference latency of 1.01 seconds. |
| **Limitation** | Detection time (1.01 s) is slightly higher than lightweight decision trees (0.23 s); deep MLP architectures risk exponential parameter growth and overfitting if layers are scaled too deep. |
| **Relevance to Proposed Research** | Directly supports RO1 and RO2 — demonstrates an effective tree-based feature selection technique (LightGBM) to reduce dimensionality before feeding data into neural network classifiers for network intrusion detection. |
| **Citation (APA 7th)** | Deng, Y. (2024). Design of industrial IoT intrusion security detection system based on LightGBM feature algorithm and multi-layer perception network. *Journal of Cyber Security and Mobility*, 13(2), 327–348. https://doi.org/10.13052/jcsm2245-1439.1327 |
| **License** | Copyright © 2024 River Publishers — Paywalled / No redistribution permitted (DOI provided in accordance with brief guidelines) |
