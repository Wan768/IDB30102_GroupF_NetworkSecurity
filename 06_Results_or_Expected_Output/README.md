## 06_Results_or_Expected_Output

### Preliminary Pipeline Test Output
`baseline_metrics.json` in this folder is the automatically generated output of running `train_baseline_model.py` on the **synthetic sample data** in `05_Data_or_Sample_Input/`. Its purpose is only to demonstrate that the code pipeline runs end-to-end and produces metrics in the correct format – **it is not a research result** and should not be interpreted as evidence of model performance, since the input data is randomly generated.

### Expected Output (Once Run on Real Benchmark Data)
When the pipeline is run on the full CICIDS2017 / NSL-KDD / UNSW-NB15 datasets (per the Proposed Evaluation Plan, Chapter 3.7 of the Research Proposal), the following outputs are expected:

| Model | Expected Accuracy Range | Expected Inference Time | Notes |
| :--- | :--- | :--- | :--- |
| **Random Forest (lightweight ML baseline)** | $\sim 90\text{--}96\%$ | Very low ($\text{ms}$ range) | Fast but weaker on rare/complex attack classes |
| **CNN-LSTM (deep learning baseline)** | $\sim 97\text{--}99\%+$ | High ($\text{seconds}$ range) | High accuracy, high computational cost |
| **Proposed lightweight hybrid ML/DL model** | Target: within $\sim 1\text{--}2\%$ of DL baseline accuracy | Target: significantly lower than DL baseline | Intended to balance accuracy and efficiency (core contribution of this research) |

### Planned Result Artefacts
* Comparative metrics table (accuracy, precision, recall, F1-score, false positive rate, inference time) across all three models
* Confusion matrices per model
* A bar chart comparing accuracy vs. inference time across models, to visually demonstrate the intended efficiency trade-off improvement

### Evaluation Metrics Used
Accuracy, Precision (macro), Recall (macro), F1-score (macro), False Positive Rate, Training Time, Inference Time – consistent with Chapter 3.7 of the Research Proposal.
