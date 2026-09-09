## 05_Data_or_Sample_Input

### Sample Data
`sample_traffic.csv` is a small synthetic sample (300 rows) that mimics the structure of standard NIDS benchmark datasets (columns similar to NSL-KDD/CICIDS-style features: duration, protocol_type, service, src_bytes, dst_bytes, flag, count, srv_count, label). It exists only to demonstrate that the preprocessing and baseline training pipeline in `04_Source_Code/` runs correctly end-to-end. It is **not** used for reporting any research findings.

### Full Benchmark Datasets (to be used for actual evaluation)
The full datasets are **not included** in this repository due to file size and in some cases redistribution restrictions. They must be downloaded directly from their official sources:

| Dataset | Description | Official Source |
| :--- | :--- | :--- |
| CICIDS2017 | Realistic modern benign + attack traffic (DoS, DDoS, Brute Force, Infiltration, etc.), developed by the Canadian Institute for Cybersecurity | https://www.unb.ca/cic/datasets/ids-2017.html |
| NSL-KDD | Improved/cleaned version of the classic KDD Cup 99 dataset, widely used as an intrusion detection benchmark | https://www.unb.ca/cic/datasets/nsl.html |
| UNSW-NB15 | Hybrid of real modern normal activities and synthetic contemporary attack behaviours | https://research.unsw.edu.au/projects/unsw-nb15-dataset |

### Intended Use
For RO2/RO3, the preprocessing pipeline (`04_Source_Code/preprocess.py`) will be pointed at one or more of the above datasets (downloaded locally, not committed to GitHub) using the `--input` argument, e.g.:
```bash
python preprocess.py --input /path/to/NSL-KDD/KDDTrain+.csv --label-col label
