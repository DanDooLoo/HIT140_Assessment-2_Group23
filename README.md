<div align="center">
<h1>Group 23 ~ Assessment 3 </h1>
<h2>Foundations of Data Science </h2>
<h3>Charles Darwin University </h3>

![alt text](image.png)

</div>
<h2>Group 23:</h2>

| Name | Student # | Study Mode | Region |
|--------|----------|---------------|--------|
| Danielle | S407528 | Online | WA |
| Gabrielle | S375255 | Online | NT |
| Judith | S395778 | Online | NSW |
| Manuela | S320756 | Online | NSW |

<h2>⚽ Project Overview - FIFA World Cup Analysis</h2>

This project investigates the FIFA World Cup 2026 statistics.

## Group 23 wiki
[Take Me Home](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki)

### Assessment 2: Group Presentation
[Objective 1](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki/Objective-1-%E2%80%90-Group-Presentation)<br>
[Group 23: Objective 1 - Documentation](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki/Objective-1-%E2%80%90-Group-Documentation)

### Assessment 3: Group Report
[Objective 2](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki/Objective-2-%E2%80%90-Linear-Regression-Models-%E2%80%90-Question-2.1-&-2.3)<br>
[Group 23: Objective 2 - Documentation](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki/Objective-2-%E2%80%90-Documentation)

<h2>📌 Objective 2:</h2>

Your team will perform two related but distinct linear regression tasks as specified below.

**2.1 Linear Regression**<br>

Build and evaluate a linear regression model that predicts the goal difference between two opposing teams in FIFA World Cup 2026 matches. You must compile a dataset that comprises 104 rows, each representing an actual match in the FIFA World Cup 2026. Your dataset must include exactly eight (8) explanatory variables (excluding any ID field). You must thoughtfully decide what these explanatory variables would be and then collect their corresponding data.

<em>Note: All explanatory variables must provide information that is available before a match. 
For example, the number of shots on target made during a match cannot be used as an explanatory variable for predicting the goal difference of that match.</em>


**2.2 Linear Regression**<br>

Build and evaluate a second linear regression model that predicts the number of goals scored by a team in a single FIFA World Cup 2026 match. 
You must compile a dataset that comprises 208 rows, each representing a team's statistics for a specific match. Your dataset must include exactly eight (8) explanatory variables (excluding any ID field). 
You must thoughtfully decide what these explanatory variables would be and then collect their corresponding data.<br>


<em>Note: All explanatory variables must provide information that is available before a match.  
For example, the number of shots on target made by a team during a match cannot be used as an explanatory variable for predicting their goal for that match.</em><br>

**Only a maximum of 4 explanatory variables can be shared between Linear Regression 2.1 and Linear Regression 2.2**


<br>
<h2>Group 23: Assessment 3 - Objective 2 - Linear Regression</h2>

**🧱 Load data**
- `matches_data` = pd.read_csv('matchesk.csv')
- `external_data` = pd.read_csv('external_factors.csv')
- `teams_data` = pd.read_csv('teamsk.csv')
- `venues_data` = pd.read_csv('venuesk.csv')
- `full_data` = pd.read_csv('full.csv')


**🔗 Sources:**
- FIFA Official Website: `https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics`
- FB Ref: `https://fbref.com/en/`
- Kaggle: `https://www.kaggle.com/datasets`

<h2>🧪 2.1 Linear Regression</h2>

**🗺️ Stage 1: Conceptual Domains Identification**

Goal difference is determined by the interplay of three domains:<br>

(a) `team capability` (inherent strength and attacking prowess)<br>
(b) `match conditions` (venue and officiating characteristics)<br>
(c) `contextual factors` (travel fatigue and psychological state)<br>

This framework ensured comprehensive coverage of mechanisms influencing match outcomes.

**🗺️ Stage 2: Pre-Match Data Constraint**

The specification "pre-match data only" eliminates post-match statistics (shots, corners, possession during play) and retroactively calculated metrics. This constraint is critical for genuine predictive utility models must rely on information available *before* kickoff, not observed during play.

**⚙️ Stage 3: Variable Operationalisation**

| Domain | Variable | Justification | Source |
|--------|----------|---------------|--------|
| **Team Capability** | `home_Possession (%)` | Ball possession reflects team's intended tactical approach and control in play; aggregate FIFA data proxies expected possession tendency | FIFA tournament statistics |
| | `away_Possession (%)` | Symmetric away team measure; possession asymmetry (home - away) indicates control differential | FIFA tournament statistics |
| | `home_xG` | Expected Goals quantifies shot quality and finishing threat independent of actual conversion; pre-match xG based on team historical efficiency | Match external factors |
| | `away_xG` | Away team expected goals; provides balanced assessment of offensive threat | Match external factors |
| **Match Conditions** | `betting_odds_home` | Market-implied probability of home win incorporates collective expert judgment; odds compress multiple unobserved variables into single summary statistic | Pre-match betting market |
| | `referee_strictness` | Officiating bias influences goal-scoring opportunities through penalty-giving propensity and tackling tolerance; strictness rating derived from historical yellow/red card distribution | Referee profile dataset |
| **Contextual Factors** | `travel_distance_km` | Away team travel distance quantifies jet lag, sleep disruption, and recovery difficulty; non-linear fatigue effects expected | Match venue data |
| | `social_sentiment_home` | Team social media sentiment proxies psychological readiness, confidence, and squad morale pre-match; aggregate measure filters match-day noise | Social media analytics |

## 🚀 2.1 LINEAR REGRESSION MODELING RESULTS

### 🎯 4. MODEL SPECIFICATION & EVALUATION FRAMEWORK

**Model:** Ordinary Least Squares (OLS) multiple linear regression  
**Transformation:** StandardScaler normalisation (mean=0, std=1) enables direct coefficient comparison and stabilises numerical estimation  
**Validation Strategy:** 80/20 train/test split (random_state=42 for reproducibility) + 5-fold cross-validation to assess generalisation

**Results (Primary 80/20 Split):**

| Metric | Train | Test | Cross-Validation |
|--------|-------|------|------------------|
| **R² Score** | 0.4148 | **0.3048** | 0.2478 ± 0.0974 |
| **RMSE** | 1.567 goals | **1.8657 goals** | — |
| **MAE** | 1.228 goals | **1.4518 goals** | — |
| **N (samples)** | 83 | 21 | 104 |

### 💡 5. RESULTS INTERPRETATION

**What R² = 0.3048 Means:**  
The model explains 30.5% of test-set goal difference variance. In discrete outcome prediction (goal difference ranges -3 to +2, n=104), this represents *moderate* predictive power. Context matters:<br>

(a) goal difference is inherently stochastic with irreducible randomness from match-to-match referee variance, defensive lapses, and finishing luck;<br>
(b) 8 pre-match variables cannot capture tactical in-game adjustments, substitution timing, or injury attrition during play;<br>
(c) a null model (predicting mean=0) achieves R²=0.00, so 0.30 represents meaningful structure extraction<br>

**RMSE = 1.87 Goals Interpretation:**  
Average prediction error is ±1.87 goals. Given that 95% of matches produce goal differences in the range [-3, +2], this error magnitude places ~68% of predictions within ±1.87 of true values a practically useful signal. For tournament forecasting (predicting winner/loser, not exact scoreline), directional correctness matters more than absolute accuracy; sign error on predictions would reduce utility but magnitude error has graduated consequences.

**Train-Test Divergence (0.4148 vs. 0.3048):**  
The 11% gap suggests *modest overfitting* the model fits training noise not present in held out data. However, the CV mean R² (0.2478) falling *below* test R² indicates test-set sampling variation (small n=21) rather than systematic overfitting. Multi-split robustness testing (70/30, 90/10 splits) confirmed this: Test R² ranges 0.30–0.49, consistent with noise driven variation on small test subsets.

<h3>2.2 Linear Regression</h3>
.....to be added

Author: Danielle Whitney + Gabby Davis