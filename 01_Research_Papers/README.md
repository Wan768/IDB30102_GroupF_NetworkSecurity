# Research Papers Summary

## Theme 1: Machine Learning and Tree-Based NIDS

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


### Paper 2
| Item | Required Information |
| --- | --- |
| **Paper Title** | Design of Network Intrusion Detection System Based on Data Mining|
| **Author(s)** | Meng Zhang|
| **Year** | 2022|
| **Research Problem** | Traditional intrusion detection systems struggle with high computational requirements and detection delays when mining large-scale network traffic data. |
| **Method / Technique** | Data mining classification algorithms evaluated and compared against conventional IDS approaches. |
| **Dataset / Tools** | KDD CUP99 dataset.|
| **Main Findings** | The system demonstrated significant advantages in classification accuracy, false alarm rate reduction, and detection processing speed compared to standard algorithms. |
| **Limitation** | Evaluation was restricted to a limited comparison with only four other types of IDS algorithms and utilized an outdated benchmark dataset. |
| **Relevance to Proposed Research** | Serves as a baseline reference for evaluating traditional data mining and feature extraction techniques against modern lightweight ML/DL architectures. |
| **Citation (APA 7th)** | Zhang, M. (2022). Design of network intrusion detection system based on data mining. *2022 International Conference on Electronics and Devices, Computational Science (ICEDCS)*, 460–463. [https://doi.org/10.1109/ICEDCS57299.2022.9997039](https://www.google.com/search?q=https://doi.org/10.1109/ICEDCS57299.2022.9997039)<br> |
| **License** | IEEE / Standard Academic License |

### Paper 3
| Item | Required Information |
| --- | --- |
| **Paper Title** | Anomaly Detection IDS for Detecting DoS Attacks in IoT Networks Based on Machine Learning Algorithms |
| **Author(s)** | Esra Altulaihan, Mohammad A. Almaiah, Ahmad Aljughaiman |
| **Year** | 2024 |
| **Research Problem** | Efficiently detecting Denial of Service (DoS) attacks targeting IoT networks with minimal processing delay. |
| **Method / Technique** | Supervised machine learning algorithms (Decision Tree, Random Forest, etc.) combined with feature selection pipelines. |
| **Dataset / Tools** | IoTID20 dataset. |
| **Main Findings** | Decision Tree and Random Forest classifiers delivered the highest accuracy and execution speed for DoS traffic profiling. |
| **Limitation** | Focused on standard supervised machine learning methods without addressing complex non-linear attack vectors or hybrid architectures. |
| **Relevance to Proposed Research** | Confirms feature selection effectiveness prior to model ingestion, supporting tree-based feature selection approaches. |
| **Citation (APA 7th)** | Altulaihan, E., Almaiah, M. A., & Aljughaiman, A. (2024). Anomaly detection IDS for detecting DoS attacks in IoT networks based on machine learning algorithms. *Sensors*, 24(2), 713. [https://doi.org/10.3390/s24020713](https://www.google.com/search?q=https://doi.org/10.3390/s24020713)<br> |
| **License** | CC BY 4.0 — open access |

### Paper 4
| Item | Required Information |
| --- | --- |
| **Paper Title** | A Lightweight Model for DDoS Attack Detection Using Machine Learning Techniques |
| **Author(s)** | Sapna Sadhwani, B. Manibalan, R. Muthalagu, P. M. Pawar |
| **Year** | 2023 |
| **Research Problem** | High computational overhead associated with identifying Distributed Denial of Service (DDoS) attacks in resource-constrained IoT systems. |
| **Method / Technique** | Machine learning classification pipeline incorporating data scaling, normalization, and feature selection. |
| **Dataset / Tools** | TON-IoT and BoT-IoT datasets. |
| **Main Findings** | Random Forest and Naïve Bayes classifiers achieved high accuracy while keeping execution times low across IoT datasets. |
| **Limitation** | Struggles with extreme class imbalance and deployment within constrained real-time edge environments. |
| **Relevance to Proposed Research** | Emphasizes feature scaling and attribute selection to achieve low inference latency. |
| **Citation (APA 7th)** | Sadhwani, S., Manibalan, B., Muthalagu, R., & Pawar, P. M. (2023). A lightweight model for DDoS attack detection using machine learning techniques. *Applied Sciences*, 13(17), 9937. [https://doi.org/10.3390/app13179937](https://www.google.com/search?q=https://doi.org/10.3390/app13179937)<br> |
| **License** | CC BY 4.0 — open access |

### Paper 5
| Item | Required Information |
| --- | --- |
| **Paper Title** | Reinforcing Network Security: Network Attack Detection Using Random Grove Blend in Weighted MLP Layers |
| **Author(s)** | Adel Binbusayyis |
| **Year** | 2024 |
| **Research Problem** | Improving classification accuracy and managing large traffic datasets while preventing neural network overfitting. |
| **Method / Technique** | Random Grove Blend incorporating weight weave layers into a Weighted Multi-Layer Perceptron (MLP) ensemble. |
| **Dataset / Tools** | UNSW-NB15 benchmark dataset and Scapy-generated real-time traffic streams. |
| **Main Findings** | Achieved 98% classification accuracy across complex attack categories while enhancing overall training efficiency. |
| **Limitation** | Practical implementation and validation within live operational production networks were not demonstrated. |
| **Relevance to Proposed Research** | Illustrates effective feature integration and ensembling strategies for multi-layered network intrusion classification. |
| **Citation (APA 7th)** | Binbusayyis, A. (2024). Reinforcing network security: Network attack detection using random grove blend in weighted MLP layers. *Mathematics*, 12(11), 1720. [https://doi.org/10.3390/math12111720](https://doi.org/10.3390/math12111720)<br> |

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

### Paper 3

| Item | Required Information |
| --- | --- |
| **Paper Title** | Algorithm Optimization and Implementation of a Multi-Layer Network Intrusion Detection System |
| **Author(s)** | Haotian Zhang, Jian Ma, Xi Li |
| **Year** | 2024 |
| **Research Problem** | Single-layer detection architectures face severe throughput bottlenecks and latency spikes during high-speed network traffic analysis. |
| **Method / Technique** | Multi-layered NIDS architecture implementing a 256MB Ring Buffer caching mechanism based on multithreading. |
| **Dataset / Tools** | CICIDS2019 dataset and a self-built test dataset. |
| **Main Findings** | The multi-layered NIDS significantly outperformed traditional single-tier solutions across all key evaluation metrics, including Accuracy, Recall, and F1-Score. |
| **Limitation** | The experimental validation did not incorporate live simulated attack testing in real-world deployment conditions. |
| **Relevance to Proposed Research** | Highlights the importance of multi-stage processing and caching to reduce system latency, supporting low-latency hybrid pipeline designs. |
| **Citation (APA 7th)** | Zhang, H., Ma, J., & Li, X. (2024). Algorithm optimization and implementation of a multi-layer network intrusion detection system. *2024 International Conference on Computing, Robotics and System Sciences (ICRSS)*, 239–243. [https://doi.org/10.1109/ICRSS63816.2024.10859124](https://www.google.com/search?q=https://doi.org/10.1109/ICRSS63816.2024.10859124)<br> |
| **License** | IEEE / Standard Academic License |

### Paper 4

| Item | Required Information |
| --- | --- |
| **Paper Title** | Residual Dense Optimization-Based Multi-Attention Transformer to Detect Network Intrusion against Cyber Attacks |
| **Author(s)** | Majid H. Alsulami |
| **Year** | 2024 |
| **Research Problem** | Conventional deep learning models struggle to capture fine-grained feature representations across diverse attack types in high-dimensional network traffic. |
| **Method / Technique** | Residual Dense Optimization-Based Multi-Attention Transformer architecture. |
| **Dataset / Tools** | UNSW-NB15 and CICIDS2017 datasets. |
| **Main Findings** | Outperformed conventional DL models across Accuracy, Precision, Recall, and F1-score. |
| **Limitation** | Requires significant computational resources, heavy memory overhead, and extensive hyperparameter tuning. |
| **Relevance to Proposed Research** | Demonstrates the detection potential of deep learning while emphasizing the necessity for lighter, low-overhead models like Shallow 1D-CNNs for constrained environments. |
| **Citation (APA 7th)** | Alsulami, M. H. (2024). Residual dense optimization-based multi-attention transformer to detect network intrusion against cyber attacks. *Applied Sciences*, 14(17), 7763. https://www.mdpi.com/2076-3417/14/17/7763<br> |
| **License** | CC BY 4.0 — open access |

### Paper 5

| Item | Required Information |
| --- | --- |
| **Paper Title** | DRL-GAN: A Hybrid Approach for Binary and Multiclass Network Intrusion Detection |
| **Author(s)** | Caroline Strickland, Mohamed Zakar, Chirantan Saha, Seyedali Soltani Nejad, Nazneen Tasnim, Daniel J. Lizotte, Anwar Haque |
| **Year** | 2024 |
| **Research Problem** | Severe class imbalance in network security datasets leads to high false negative rates for rare attack types. |
| **Method / Technique** | DRL-GAN (Deep Reinforcement Learning + Generative Adversarial Networks) hybrid framework for synthetic sample generation and multi-class detection. |
| **Dataset / Tools** | CICIDS2017 and benchmark IDS datasets. |
| **Main Findings** | Substantially improved classification accuracy, recall, and F1-score for minority and rare attack classes. |
| **Limitation** | Detection performance is highly dependent on the quality and distribution of generated synthetic samples. |
| **Relevance to Proposed Research** | Addresses dataset imbalance challenges in multi-class network intrusion detection, providing guidance on feature scaling and data preprocessing steps. |
| **Citation (APA 7th)** | Strickland, C., Zakar, M., Saha, C., Soltani Nejad, S., Tasnim, N., Lizotte, D. J., & Haque, A. (2024). DRL-GAN: A hybrid approach for binary and multiclass network intrusion detection. *Sensors*, 24(9), 2746. https://www.mdpi.com/1424-8220/24/9/2746 |
| **License** | CC BY 4.0 — open access |

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

## Theme 4: Optimization and Feature Reduction Strategies

### Paper 1
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | TTANAD: Test-Time Augmentation for Network Anomaly Detection |
| **Author(s)** | Seffi Cohen, Niv Goldshlager, Bracha Shapira, Lior Rokach |
| **Year** | 2023 |
| **Research Problem** | Existing machine learning-based Network Intrusion Detection Systems (NIDS) primarily focus on modifying detector models, while modern cyber threats successfully evade detection, highlighting the need to address detection limitations from the data side during inference. |
| **Method / Technique** | TTANAD — a novel framework utilizing test-time augmentation that leverages the temporal characteristics of network traffic data to produce temporal test-time augmentations, creating multiple inference viewpoints across diverse anomaly detection algorithms without requiring model retraining. |
| **Dataset / Tools** | CIC-IDS2017, CSE-CIC-IDS2018, and UNSW-NB15 benchmark datasets. |
| **Main Findings** | Demonstrated that TTANAD outperforms standard baselines across all evaluated benchmark datasets and tested anomaly detection algorithms based on the Area Under the Receiver Operating Characteristic (AUC) metric. |
| **Limitation** | Relies on generating appropriate temporal windows and requires additional computational overhead during the inference phase due to multi-instance predictions. |
| **Relevance to Proposed Research** | Directly supports Theme 4 (Optimization and Feature Reduction Strategies) by showing how test-time data augmentation and temporal feature aggregation optimize detection performance and robustness without altering underlying architectures. |
| **Citation (APA 7th)** | Cohen, S., Goldshlager, N., Shapira, B., & Rokach, L. (2023). TTANAD: Test-time augmentation for network anomaly detection. *Entropy*, 25(5), 820. https://doi.org/10.3390/e25050820 |
| **License** | CC BY 4.0 — Open access, creative commons attribution permitted. |

### Paper 2
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Improved Intrusion Detection Based on Hybrid Deep Learning Models and Federated Learning |
| **Author(s)** | Jia Huang, Zhen Chen, Sheng-Zheng Liu, Hao Zhang, Hai-Xia Long |
| **Year** | 2024 |
| **Research Problem** | Industrial Internet of Things (IIoT) devices face critical network security threats, while limited local data resources and data privacy regulations hinder effective centralized machine learning training for intrusion detection systems. |
| **Method / Technique** | DVACNN-Fed — a federated learning framework integrating Deep Variational Autoencoders (DVA) for data privacy and feature protection with Convolutional Neural Networks and Attention mechanisms (CNN-Attention) for robust intrusion classification across distributed IIoT nodes. |
| **Dataset / Tools** | TON-IoT and BoT-IoT benchmark datasets; implemented using Python and deep learning frameworks to simulate distributed federated learning client nodes. |
| **Main Findings** | Demonstrated that the proposed federated learning hybrid model significantly improves detection accuracy, precision, and false-positive rate compared to traditional local training methods and standard baseline models while protecting user data privacy. |
| **Limitation** | Communication overhead introduced by frequent model updates across multiple distributed nodes in the federated network, and potential vulnerability to malicious client poisoning attacks if node validation is relaxed. |
| **Relevance to Proposed Research** | Directly supports research objectives involving distributed network optimization, privacy-preserving feature learning, and hybrid deep learning architectures for modern industrial IoT environments. |
| **Citation (APA 7th)** | Huang, J., Chen, Z., Liu, S.-Z., Zhang, H., & Long, H.-X. (2024). Improved intrusion detection based on hybrid deep learning models and federated learning. *Sensors*, 24(12), 4002. https://doi.org/10.3390/s24124002 |
| **License** | CC BY 4.0 — open access, creative commons attribution permitted |

### Paper 3
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | A Federated Network Intrusion Detection System with Multi-Branch Network and Vertical Blocking Aggregation |
| **Author(s)** | Yunhui Wang, Weichu Zheng, Zifei Liu, Jinyan Wang, Hongjian Shi, Mingyu Gu, Yicheng Di |
| **Year** | 2023 |
| **Research Problem** | Distributed networks and Internet of Things (IoT) nodes face severe intrusion threats while traditional centralized intrusion detection models compromise data privacy and encounter high communication bottlenecks during model aggregation. |
| **Method / Technique** | A federated network intrusion detection system combining a multi-branch neural network architecture for local feature extraction with a vertical blocking aggregation algorithm (FedVB) to optimize parameter transmission and secure global model convergence. |
| **Dataset / Tools** | Benchmark network traffic datasets including CICIDS2017 and UNSW-NB15; implemented in Python utilizing distributed simulation frameworks. |
| **Main Findings** | Proved that the multi-branch network combined with vertical blocking aggregation effectively reduces communication overhead and improves global detection accuracy compared to standard federated averaging approaches. |
| **Limitation** | Increased local computational complexity due to multi-branch feature processing, and sensitivity to non-IID (Independent and Identically Distributed) data imbalances across distributed clients. |
| **Relevance to Proposed Research** | Directly supports Theme 4 (Optimization and Feature Reduction Strategies) by presenting an optimized aggregation and multi-branch network strategy that minimizes communication overhead and computational redundancy in distributed NIDS environments. |
| **Citation (APA 7th)** | Wang, Y., Zheng, W., Liu, Z., Wang, J., Shi, H., Gu, M., & Di, Y. (2023). A federated network intrusion detection system with multi-branch network and vertical blocking aggregation. *Electronics*, 12(19), 4049. https://doi.org/10.3390/electronics12194049 |
| **License** | CC BY 4.0 — open access, creative commons attribution permitted |

### Paper 4
| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Feature Engineering and Model Optimization Based Classification Method for Network Intrusion Detection |
| **Author(s)** | Yujie Zhang, Zebin Wang |
| **Year** | 2023 |
| **Research Problem** | Traditional machine learning models face constraints in handling high-dimensional network traffic data and imbalanced class distributions, where redundant information and rare attack classes undermine classification accuracy. |
| **Method / Technique** | An integrated classification method combining a feature engineering approach via mutual information maximum correlation minimum redundancy (mRMR) feature selection and Synthetic Minority Over-sampling Technique (SMOTE), coupled with the Optuna method to fine-tune CatBoost classifier hyperparameters. |
| **Dataset / Tools** | NSL-KDD, UNSW-NB15, and CIC-IDS2017 benchmark datasets. |
| **Main Findings** | Demonstrated through binary and multi-class classification experiments that the proposed feature engineering and hyperparameter optimization approach outperforms traditional methods in accuracy, recall, precision, and F-value. |
| **Limitation** | Requires extensive preprocessing and computational search overhead during feature selection and hyperparameter optimization phases. |
| **Relevance to Proposed Research** | Directly supports Theme 4 (Optimization and Feature Reduction Strategies) by utilizing mRMR feature selection and optimization techniques to handle high-dimensional traffic data and class imbalance. |
| **Citation (APA 7th)** | Zhang, Y., & Wang, Z. (2023). Feature engineering and model optimization based classification method for network intrusion detection. *Applied Sciences*, 13(16), 9363. https://doi.org/10.3390/app13169363 |
| **License** | CC BY 4.0 — Open access, creative commons attribution permitted. |
