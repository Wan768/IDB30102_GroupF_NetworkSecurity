# IDB30102_GroupF_NetworkSecurity

**Research Title:** Design of a Lightweight Hybrid Machine Learning/Deep Learning Intrusion Detection System for Resource Constrained Networks

**Group Number:** Group F 

## Group Members and Student IDs
* Shahril Iskandar Bin Sharizan (52215125627)
* Wan Abdul Khaliq Bin Abdul Wahab (52215125764)
* Wan Ahmad Naqeeb Bin Wan Mohd Nazmi (52215125617)
* Wan Harith Fahmi Bin Wan Mohd Nur Muzaaliff (52215125705)

**Assigned Research Area:** Network Security & Intrusion Detection Systems (NIDS)

## Research Problem
1. Although deep learning based intrusion detection models are very accurate, their large computational cost makes them unsuitable for real time deployment on networks with limited resources.
2. In environments with limited resources, lightweight machine learning classifiers can be less effective to identify complex and uncommon attack patterns which lowers detection reliability.

**Research Aim:** To create, develop and assess a lightweight hybrid machine learning and deep learning intrusion detection model that balances between computational efficiency and detection accuracy for implementation in network environments with limited resources.

## THREE (3) Research Objectives
1. **RO1:** To examine current deep learning and machine learning methods for network intrusion detection together with the datasets and evaluation metrics associated with them.
2. **RO2:** To create a hybrid ML-DL intrusion detection model that is lightweight and appropriate for constrained networks.
3. **RO3:** To evaluate the proposed model's detection performance and computational effectiveness in comparison to well-known baseline classifiers using benchmark datasets

**Brief Description of the Proposed Solution:** The study designs a hybrid architecture combining a LightGBM feature selection stage with a shallow 1D-CNN deep learning component to reduce computational overhead while maintaining high threat detection accuracy in resource-constrained networks.

**Selected Research Methodology & Development Model:** Design Science Research (DSR) methodology supported by a Prototyping development model.

## Proposed Evaluation Plan
* **Baseline:** Standalone Random Forest (representing lightweight ML) and CNN-LSTM (representing resource-intensive deep learning).
* **Dataset / Test Environment:** Public benchmark datasets including CICIDS2017, NSL-KDD and UNSW-NB15 tested in an offline experimental environment.
* **Metrics:** Accuracy, Precision, Recall, F1-score, False Positive Rate (FPR) and Inference Time.

**Proposed System Architecture:** Ingestion -> Data Pre-processing Layer -> Lightweight Feature-Selection Stage (LightGBM) -> Deep-Learning Component (Shallow 1D-CNN) -> Classification Layer.

## Description of Technical Components in Repository
* `01_Research_Papers/`: Contains categorized literature review papers and summary tables.
* `02_Literature_Review/`: Synthesis materials and related analysis.
* `03_Architecture_and_Flowchart/`: System architecture diagrams and flowcharts.
* `04_Source_Code/`: Prototype implementation files and scripts.
* `05_Data_or_Sample_Input/`: Sample datasets or input logs for testing.
* `06_Results_or_Expected_Output/`: Performance logs and evaluation metric outputs.
* `07_References/`: Documentation references.

**Expected Tools & Technologies:** Python, Scikit-learn, LightGBM, TensorFlow/Keras or PyTorch, CICIDS2017/NSL-KDD/UNSW-NB15 datasets.

## Instructions for Executing Preliminary Code
1. Clone the repository: `git clone https://github.com/Wan768/IDB30102_GroupF_NetworkSecurity.git`
2. Navigate to `04_Source_Code/` and install dependencies: `pip install -r requirements.txt`
3. Run the preliminary script to execute data preprocessing and feature selection.
