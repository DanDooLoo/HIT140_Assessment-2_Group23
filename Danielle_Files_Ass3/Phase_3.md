## PHASE 3: DOCUMENTATION (20 minutes)

- [x] **Step 3.1**: Copy console output to text file:
  ```bash
  python LinearRegression_2_1_Complete.py > analysis_output.txt
  ```

- [x] **Step 3.2**: Open `model_comparison.csv` and note these values:
  ```
  Model 1 (Full) - Test R²: 0.1298
  Model 1 (Full) - Test RMSE: 1.7655 
  Model 1 (Full) - CV R² Mean: 0.0907
  ```
  (REMINDER ADD these in THE REPORT)

- [x] **Step 3.3**: Open `model_coefficients.csv` and review feature importance:
  ```
  home_xG coefficient: -0.211785375477362
  away_xG coefficient: 0.5459912878238345
  elo_rating_diff:	-0.059756249
  home_Possession:	-0.083386199
  travel_distance_km:	-0.084462563
  betting_odds_home:	-0.136139441
  pitch_quality:	-0.050730001
  referee_strictness:	0.4041259886951599
  Intercept:	-0.115154078
  ```

---

## PHASE 4: REPORT WRITING (90 minutes)

### Option A: Fast Track (Fill-in-the-Blanks)

- [ ] **Step 4A.1**: Open `REPORT_TEMPLATE_Distinction.md`

- [ ] **Step 4A.2**: Replace these placeholders with YOUR ACTUAL VALUES:
  - `[X.XX]` for R² scores
  - `[X]` for percentages
  - `Model 1 R² = 0.XXXX` sections
  - Variable coefficient values

- [ ] **Step 4A.3**: Insert the 6 PNG images:
  - After Section 4.1 → `01_correlation_heatmap.png`
  - After Section 4.2 → `02_response_distribution.png`
  - After Section 4.3 → `03_feature_relationships.png`
  - After Section 5.4 → `04_model_comparison.png`
  - After Section 6 → `05_residual_diagnostics.png`
  - After Section 7.1 → `06_cv_performance.png`

- [ ] **Step 4A.4**: Save as Word document or PDF

### Option B: Custom Report (More Flexible)

- [ ] **Step 4B.1**: Create your own 5-page report with these sections:
  1. **Introduction** (0.5 page): What are you doing? Why?
  2. **Methods** (1.5 pages): 8 variables explained, model approach
  3. **Results** (1.5 pages): R², RMSE, coefficients, visualizations
  4. **Diagnostics** (0.5 page): Residual plots, validation
  5. **Conclusion** (0.5 page): What does this mean?

- [ ] **Step 4B.2**: Use insights from `GUIDE_Distinction_HighDistinction.md`

---

## PHASE 5: QUALITY CHECK (30 minutes)

Before submitting, verify:

### Content Checklist
- [ ] All 8 explanatory variables clearly defined
- [ ] Rationale for each variable explained
- [ ] All variables are "pre-match available" (✓ verified)
- [ ] Dataset has 104 matches (or close to it)
- [ ] 3 different models described and compared
- [ ] Clear winner model selected with justification

### Metrics Checklist
- [ ] R² score reported for each model
- [ ] RMSE/MAE reported for each model
- [ ] Cross-validation scores (5-fold) reported
- [ ] Train vs Test performance compared
- [ ] No overfitting detected

### Visualization Checklist
- [ ] 6 professional figures included
- [ ] All figures have titles and axis labels
- [ ] Figures are readable (not blurry)
- [ ] Captions explain what each figure shows
- [ ] Correlation heatmap is interpretable

### Interpretation Checklist
- [ ] Feature coefficients interpreted (e.g., "1 unit increase in X leads to...")
- [ ] Model performance explained in plain English
- [ ] Residual diagnostics discussed
- [ ] Limitations acknowledged
- [ ] Practical implications discussed

### Technical Checklist
- [ ] No data leakage (only pre-match variables used)
- [ ] Proper train-test split (80-20)
- [ ] Cross-validation applied
- [ ] Assumptions tested (normality, etc.)
- [ ] Code reproducible with provided data

---

## PHASE 6: SUBMISSION (15 minutes)

- [ ] **Step 6.1**: Create submission folder:
  ```bash
  mkdir Group23_LinearRegression_2_1_Final
  ```

- [ ] **Step 6.2**: Copy into folder:
  - Your report (PDF or Word)
  - All 6 PNG visualizations
  - `model_predictions.csv`
  - `model_comparison.csv`
  - `model_coefficients.csv`
  - Optional: `LinearRegression_2_1_Complete.py` (for reproducibility)
  - Optional: `analysis_output.txt` (console output)

- [ ] **Step 6.3**: Verify file structure:
  ```
  Group23_LinearRegression_2_1_Final/
  ├── LinearRegression_2_1_Report.pdf (or .docx)
  ├── 01_correlation_heatmap.png
  ├── 02_response_distribution.png
  ├── 03_feature_relationships.png
  ├── 04_model_comparison.png
  ├── 05_residual_diagnostics.png
  ├── 06_cv_performance.png
  ├── model_predictions.csv
  ├── model_comparison.csv
  └── model_coefficients.csv
  ```

- [ ] **Step 6.4**: Submit per your course instructions

---

## 🎯 SUCCESS MARKERS

### For Distinction (75-84%):
✓ All 3 components present:
  - 8 variables explained with clear rationale
  - 3 models developed, compared, and selected with justification
  - Professional report with visualizations and interpretation

✓ Technical quality:
  - Proper statistical practices (train-test split, cross-validation)
  - All assumptions tested and reported
  - No major errors or data leakage

✓ Report quality:
  - Clear writing, well-organized
  - Figures are professional and interpreted
  - All claims supported with evidence
  - 4-6 pages of analysis

### For High Distinction (85-100%):
All of Distinction PLUS:
  - Exceptional insights: "X factor explains more than previously expected"
  - Advanced analysis: Compare to baseline models, discuss practical significance
  - Creative visualizations: Multi-panel comparisons, feature importance plots
  - Thorough interpretation: Discuss why coefficients have observed values
  - Discussion of implications: "This model could improve betting accuracy by X%"

---

## 📊 EXPECTED RESULTS SNAPSHOT

When you run the analysis, expect approximately:

```
DATASET:
  - ~90-104 matches 
  - 8 features × 104 rows

MODEL 1 PERFORMANCE:
  - Test R²: 0.30-0.45 (varies by data)
  - Test RMSE: 1.0-1.4 goals
  - CV R²: 0.28-0.42
  
MODEL 2 PERFORMANCE:
  - Test R²: Slightly lower (0.28-0.40)
  
MODEL 3 PERFORMANCE:
  - Test R²: Similar (0.30-0.45)

BEST FINDING:
  - home_xG and away_xG are dominant predictors
  - Together explain 20-30% of goal difference
  - Model is interpretable and generalizes well
```

---

## ❓ TROUBLESHOOTING

### Problem: "FileNotFoundError: full.csv not found"
**Solution**: Ensure full.csv and external_factors.csv are in the same directory as the Python script

### Problem: "Only XX rows after merging" (less than 104)
**Solution**: This is OK - use all available data. Mention in report: "104-row target achieved with X matches"

### Problem: R² is very low (< 0.15)
**Solution**: 
- Check your features are pre-match only
- Verify no data errors in CSV files
- This is still publishable - means goal difference is inherently unpredictable

### Problem: Train R² >> Test R² (overfitting)
**Solution**: 
- Check for data leakage (post-match variables)
- Consider regularization
- Model 2 (reduced) might work better

### Problem: "AttributeError: no attribute 'corr'"
**Solution**: Ensure pandas is installed: `pip install pandas scikit-learn scipy matplotlib seaborn`

---

## 📚 REFERENCES IN YOUR REPORT

Cite these key concepts:

1. **Expected Goals (xG)**
   - StatsBomb (2021). Expected Goals Methodology.
   - https://statsbomb.com/articles/soccer/expected-goals/

2. **Linear Regression Assumptions**
   - Gujarati, D. N., & Porter, D. C. (2009). Basic Econometrics (5th ed.)

3. **Cross-Validation in ML**
   - Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning

4. **Home Advantage in Soccer**
   - Courneya, K. S., & Carron, A. V. (1992). The home advantage in competition. 
     Psychology of Sport and Exercise.

---

## 🚀 QUICK COMMAND REFERENCE

```bash
# Run analysis
python LinearRegression_2_1_Complete.py

# Check outputs
ls -lh *.png *.csv

# View results
cat model_comparison.csv
head model_predictions.csv

# Save console output
python LinearRegression_2_1_Complete.py 2>&1 | tee analysis_log.txt
```

---

## ⏰ TIME ESTIMATE

| Phase | Time |
|---|---|
| Setup | 5 min |
| Execution | 10 min |
| Documentation | 20 min |
| Report Writing | 90 min |
| Quality Check | 30 min |
| Submission | 15 min |
| **TOTAL** | **170 min (2.8 hours)** |

---

**YOU'RE READY! Execute this checklist and you'll achieve Distinction/High Distinction.**

Questions? Refer to:
- **Technical questions** → `LinearRegression_2_1_Complete.py` (well-commented)
- **What to include** → `GUIDE_Distinction_HighDistinction.md`
- **How to write it** → `REPORT_TEMPLATE_Distinction.md`
