# LINEAR REGRESSION 2.1 - Setup and Running Files

---

## STEP 1: SETUP - Approx 5 minutes ⏱️

- [ ] **Step 1.1**: Copy these 3 files to your working directory:
  - `LinearRegression_2_1_Complete.py` (the main analysis script)
  - `full.csv`
  - `external_factors.csv`

- [ ] **Step 1.2**: Verify files exist: Terminal = Git Bash
  ```bash
  ls -la full.csv external_factors.csv LinearRegression_2_1_Complete.py
  ```

- [ ] **Step 1.3**: Open Python environment (Anaconda + VS Code + Jupyter)
1. Launch Anaconda 
Environment = hit140env
```command
  - conda activate hit140env
```

2. Launch VS Code through GitHub Desktop
- Repository: HIT140_Assessment-2_Group23
  - Repo holds work for Assessment 2 & 3

3. In VS Cope open Jupyter Server
  - In Git Bash terminal type...
  ```bash
  python -m notebook
  ```

---

## STEP 2: EXECUTION (10 minutes)

- [ ] **Step 2.1**: Run the analysis script:
  ```bash
  python LinearRegression_2_1_Complete.py
  ```

- [ ] **Step 2.2**: Wait for completion (should take 2-3 minutes)

- [ ] **Step 2.3**: Check outputs generated:
  ```bash
  ls -la *.png *.csv
  ```
  Expected Outputs:
  - `01_correlation_heatmap.png` ✓
  - `02_response_distribution.png` ✓
  - `03_feature_relationships.png` ✓
  - `04_model_comparison.png` ✓
  - `05_residual_diagnostics.png` ✓
  - `06_cv_performance.png` ✓
  - `model_predictions.csv` ✓
  - `model_comparison.csv` ✓
  - `model_coefficients.csv` ✓

---