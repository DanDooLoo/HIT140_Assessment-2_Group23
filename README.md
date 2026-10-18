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

[Reference Documant - How to Convert PDF to PNG by DGW](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/blob/main/Workings[Drafts]/Danielle_Files_Ass3/PDFtoImgQuickConvert.md)

### Assessment 2: Group Presentation
[Objective 1](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki/Objective-1-%E2%80%90-Group-Presentation)<br>
[Group 23: Objective 1 - Documentation](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki/Objective-1-%E2%80%90-Group-Documentation)

### Assessment 3: Group Report
[Objective 2](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki/Objective-2-%E2%80%90-Linear-Regression-Models-%E2%80%90-Question-2.1-&-2.3)<br>
[Group 23: Objective 2 - Documentation](https://github.com/DanDooLoo/HIT140_Assessment-2_Group23/wiki/Objective-2-%E2%80%90-Documentation)

<h2>📌 Objective 2:</h2>

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
- Stats Don't Lie: `https://www.thestatsdontlie.com/football/world-cup-2026/`

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
## Explanatory Variable Derivation & Theory Justification

### Introduction & Research Objective
The objective of this analysis is to develop a linear regression model predicting goal difference (home goals minus away goals) in FIFA World Cup 2026 matches using exclusively pre-match explanatory variables. The constraint of EXACTLY 8 variables required thoughtful selection, balancing predictive power, theoretical relevance, and practical availability. This report explains the rationale behind each variable selection and interprets the resulting model performance.

### Explanatory Variable Selection Framework 
The eight variables were derived through a three-stage selection framework. Stage 1: Conceptual Domains Identification. Stage 2: Pre-Match Data Constraint, and Stage 3: Variable Operationalisation, please refer to Table 1 for the explanatory variables used by Group 23.

The FIFA World Cup 2026 consisted of 104 matches that resulted with Spain being the ultimate champions of the competition. The aim of the first task was to use linear regression to analyse and predict the goal difference between the two finalist opposing teams, Spain and Argentina. The second task was to predict the number of goals for one team for that same match. Group 23 have compared the results with the true results using Python programming to perform the linear regression. Our groups challenge was to research 8 viable and unique explanatory variables (x) for each task, Objective 2.1 and 2.2, and evaluate the results to achieve a calculation for the response variable (y). 

Nevertheless, our task was to be creative and make several comparisons using a test/train model, comparing the results against a baseline model. Our variables were chosen independently, compared, and evaluated using a multiple linear regression model using Python programming software. Our data files were saved as csv files using Microsoft Excel, readable by VS Code, using several packages called pandas, which is designed for reading csv files. Other packages were also used to perform the linear regression. These include math, numpy, and sklearn plus several other sub-packages. Data visualisation was also performed using matplotlib.pyplot, which were used to create scatterplots and Seaborn to create heatmaps. 

However, data visualisation is important as it provides a brief visual overview of the datasets which helps to identify problems and successes quite clearly if the data is accurate and appropriately selected. For instance, scatterplots are useful in determining if the data shows uniformity and if there any outliers. This is useful when an organisation is testing and looking to make improvements. Heatmaps also provide useful information by performing correlations of the data. If any of the variables are too similar, then a variable can be dropped, as removing unnecessary information that is already presented using a similar variable can be quite helpful when working on data visualisation. Further research is then needed to replace the variable with another, or simply removed, depending on the results of the MAE, MSE, RMSE, RMSE normalised, and R². Group 23 tested our datasets against the error values and compared them with a baseline at different stages to test this hypothesis. Our findings are listed below.


## Formula for Linear Regression

` y=b_{0}{+b}_{1}x_{1}{+b}_{2}x_{2}… `

Nevertheless, in Objective 2.1, our datasets comprised of 104 rows matching the 104 matches played during the FIFA Worl Cup 2026. In Objective 2.2, the datasets represented each team and their goals which consisted of 208 rows. Our groups challenge was to select a maximum of eight explanatory variables (x) for each objective that would be the most relevant in determining the solution for the response variable (y). These are provided in Table 1 listed below. 

## Table 1: Explanatory Variables (x), Dependant Variable(y) Selected by Group 23

| Task | Manuela Crannis – s320756 | Danielle Whitney – s407528 |
|------|--------------------------|----------------------------|
| **Obj. 2.1** | x = Score First Half Team 1<br>x = Score First Half Team 2<br>x = Possession Team 1<br>x = Possession Team 2<br>x = Attempts at Goal Team 1<br>x = Attempts at Goal Team 2<br>x = Goals Conceded Team 1<br>x = Goals Conceded Team 2<br>y = Pred. Goal Diff. | y = Pred. Goal Diff<br><br>**Base Features (8):**<br>x = elo_rating_diff<br>x = xG_home<br>x = xG_away<br>x = home_Possession<br>x = travel_distance_km<br>x = betting_odds_home<br>x = pitch_quality<br>x = referee_strictness<br><br>**Feature Engineering:**<br>elo_squared → Non-linear ELO effect *(elo_rating_diff²)*<br>xG_diff → Expected goals advantage *(xG_home − xG_away)*<br>xG_ratio → Expected goals ratio *(xG_home / xG_away + 0.1)*<br>possession_x_elo → Possession × Team Strength interaction<br>possession_x_xG_diff → Possession × Expected Goals advantage interaction<br>referee_x_travel → Referee Strictness × Travel Distance interaction |

| Task | Gabby Davis – s375255 | Judith Dawson – s395778 |
|------|----------------------|-------------------------|
| **Obj. 2.2** | Data taken from the FBR website.<br><br>x = (**LDIF**) Latitude difference from home country to venue<br>x = (**AGE**) Avg. age of team<br>x = (**MFP**) Midfielder proportion<br>x = (**DLG**) Days since team's last tournament game<br>x = (**RP**) Recent performance, avg. score of last three games<br>x = (**WC22XP**) Combined minutes played in FIFA22 by players on the team<br>x = (**WC22GS**) Combined goals scored by players on the team<br>x = (**WC22SOT**) Combined shots on target by players on the team<br>y = (xG) Predicted No. of Goals | x = (**LDIF**) Average international caps<br>x = (**AGE**) Forward proportion<br>x = (**MFP**) Days of rest<br>x = (**DLG**) Recent attacking performance<br>x = (**RP**) Recent defence performance<br>x = Previous World Cup experiences<br>x = Previous World Cup assists<br>x = Opponent defence strengths<br>y = Predicted No. of Goals |

## Table 2 : Results of the Test/Train Models
**2.1 by** Danielle Whitney [DW] and Manuela Crannis [MC]

## Model 2.1.1 by  Manuela Crannis

| Test Size (MC) | 70% Training / 30% Test | 80% Training / 20% Test | 90% Training / 10% Test |
|----------------|-------------------------|-------------------------|-------------------------|
| Intercept | -0.1074 | -0.1186 | -0.1273 |
| MAE (MLP) | 1.4307 | 1.4494 | 1.4741 |
| MSE (MLP) | 3.1780 | 3.1061 | 3.0259 |
| RMSE (MLP) | 1.7827 | 1.7624 | 1.7395 |
| RMSE_Norm (MLP) | 0.9360 | 0.9283 | 0.9034 |
| R² (MLP) | 0.1202 | 0.1328 | 0.1735 |
| MAE (Baseline) | 1.5780 | 1.5941 | 1.6657 |
| MSE (Baseline) | 3.6364 | 3.5866 | 3.6695 |
| RMSE (Baseline) | 1.9075 | 1.8933 | 1.9156 |
| RMSE_Norm (Baseline) | 1.0015 | 0.9975 | 0.9949 |
| R² (Baseline) | -0.0073 | -0.0013 | -0.0023 |

---

## Model 2.1.2 by Danielle Whitney

| Test Size (DW) | 70% Training / 30% Test | 80% Training / 20% Test | 90% Training / 10% Test |
|----------------|-------------------------|-------------------------|-------------------------|
| Intercept | -0.14270 | -0.13310 | -0.13380 |
| MAE (MLP) | 0.43050 | 0.43730 | 0.43480 |
| MSE (MLP) | 0.49940 | 0.49930 | 0.49270 |
| RMSE (MLP) | 0.4994 | 0.4993 | 0.4927 |
| R² | 0.87170 | 0.85390 | 0.80140 |
| CV_R² | 0.87810 | 0.87810 | 0.87810 |
| Intercept (Baseline) | -0.14273 | -0.13306 | -0.13381 |
| MAE (Baseline) | 1.15575 | 1.03906 | 0.90278 |
| MSE (Baseline) | 1.96641 | 1.71973 | 1.33333 |
| RMSE (Baseline) | 1.40229 | 1.31138 | 1.15470 |
| RMSE_Norm (Baseline) | 1.00583 | 1.00384 | 1.04447 |
| R² (Baseline) | -0.01170 | -0.00769 | -0.09091 |

<br>

**Final Linear Regression: [Figure 2]**<br>
Calculating the co-efficient of the variables were used to calculate y variable by Danielle Whitney.<br>
I  have run optimisation on the data I used and have updated the values above. I used Polynomial Interactions to enhance the prediction model. 
Visualisation of the response variable using a histogram and a Q-Q plot showed that goal difference follows a normal distribution. 

<br>

**Final Linear Regression: [Figure 1]**<br>
Calculating the co-efficient of the variables were used to calculate y variable by Manuela Crannis;<br>

The linear regression model performed better than the baseline model for this question. 

A correlation matrix heatmap was used to assess all explanatory variables for high multicollinearity. 
The heatmap revealed only some moderate multicollinearity, so all variables were retained.

 GD(y) | (T1S) | (T2S) | (SFHT1) | (SFHT2) | (PT1) | (PT2) | (AaGT1) |(AaGT2) | (GCT1) | (GCT2) |
|------|-------|-------|---------|---------|-------|------|---------|--------|-------|---------|
| -1.15 | -1.0146 | -2.376 | 0.7201 | 0.3479 | -0.0116 | 0.0167 | 0.0291 | -0.0335 | 0.4672 | 1.1226 |

<br>

## Figure 1: Objective 2.1 Results Obtained using Heat Maps and Scatterplots by Manuela Crannis
<img width="442" height="272" alt="image" src="https://github.com/user-attachments/assets/2ea286b8-022e-4aae-9a3a-833947556d04" />


## Figure 2: Objective 2.1 Visulisations by Danielle Whitney
<img width="538" height="385" alt="image" src="https://github.com/user-attachments/assets/c479aa84-ddb1-488f-bcb2-cf7b9afb3110" />


## 2.2 Linear Regression: Gabby Davis and Judith Dawson

## Model 2.2.1 by Gabby Davis

| Test Size (GD) | 70% Training / 30% Test | 80% Training / 20% Test | 90% Training / 10% Test |
|----------------|-------------------------|-------------------------|-------------------------|
| Intercept | 3.4690 | 5.3813 | 5.5732 |
| MAE | 1.0303 | 1.0047 | 0.8929 |
| MSE | 1.5446 | 1.6080 | 1.5716 |
| RMSE | 1.2428 | 1.2681 | 1.2536 |
| Norm. RMSE | 0.1775 | 0.1812 | 0.1791 |
| R-squared | 0.0132 | 0.1670 | 0.2999 |
| MAE (Baseline) | 1.9540 | 1.2111 | 1.2111 |
| MSE (Baseline) | 1.8967 | 2.0418 | 2.2483 |
| RMSE (Baseline) | 1.3772 | 1.4289 | 1.4995 |
| Norm. RMSE (Baseline) | 0.1967 | 0.2041 | 0.2142 |
| R-squared (Baseline) | -0.2118 | -0.0577 | -0.0015 |

---

## Model 2.2.2 by Judith Dawson

| Test Size (JD) | 70% Training / 30% Test | 80% Training / 20% Test | 90% Training / 10% Test |
|----------------|-------------------------|-------------------------|-------------------------|
| Intercept | 1.2428 | 1.2681 | 1.2536 |
| MAE (MLP) | 1.0357 | 1.0734 | 0.8067 |
| MSE (MLP) | 2.2052 | 2.2784 | 0.8983 |
| RMSE (MLP) | 1.4850 | 1.5094 | 0.9478 |
| RMSE_Norm (MLP) | 0.2121 | 0.2156 | 0.1359 |
| R² (MLP) | 0.0242 | 0.0075 | 0.1351 |
| MAE (Baseline) | 1.1490 | 1.2212 | 0.9619 |
| MSE (Baseline) | 1.1490 | 1.2212 | 0.9619 |
| RMSE (Baseline) | 1.4677 | 1.5190 | 1.1056 |
| RMSE_Norm (Baseline) | 0.2097 | 0.2170 | 0.3685 |
| R² (Baseline) | -0.0004 | -0.0204 | -0.1771 |
			
### 2.2.1 Initial Multiple Linear Regression Equation
The initial model equation was calculated before applying optimisation strategies to improve the model’s performance.
Adj. R-Squared: 0.083, RMSE: 1.30863, NRMSE: 0.18694
xG(y) = 5.3491 – 0.0073(LDIF) – 0.1442(AGE) + 0.3165(MFP) – 0.0239(DLG) – 0.0621(RP) + 1.766e-06(WC22XP) – 0.0515(WC22GS) + 0.0628(WC22SOT)

### 2.2.1 Optimisation Actions and Interpretation
1. The p-value for WC22XP (team’s combined minutes played in WC22) showed little relationship with goals scored, its coefficient was near zero at 0.000001766, and the variable had a very high p-value at p = 0.990. Upon removing the variable, the model’s performance improved only slightly. Despite this, the variable WC22SOT’s p value improved from 0.110 to 0.049 which suggests removing WC22XP made WC22SOT’s contribution more apparent. 
2. A correlation matrix heatmap was used to check for variables that have high multicollinearity. All the variables created from the WC22 stats were highly multicollinear. Upon dropping two WC22 related variables, leaving WC22SOT, the adj. r-squared was bumped up to 0.90.
3.  The model overall is performing poorly. Optimisation by removing redundant and multicollinear variables reaped little improvements in performance, suggesting that the variables have little predictive capabilities in relation to goals scored.

<img width="525" height="339" alt="image" src="https://github.com/user-attachments/assets/ad10a36b-cfba-4354-b4f5-5a87544d43bc" />

### 2.2.1 Final Equation
xG(y) = 5.1957 – 0.0082(LDIF) – 0.1375(AGE) + 0.2780(MFP) – 0.0230(DLG) – 0.0617(RP) + 0.0447(WC22SOT)

### 2.2.2 Visualising the Relationship Between Recent Performance and Goals Scored

<img width="516" height="345" alt="image" src="https://github.com/user-attachments/assets/d9bd5cad-dbd1-4c2b-92f9-a18b02cae83b" />

The scatterplot reveals a slight positive relationship between recent performance and current goals scored, with higher average goals across the previous three matches being roughly associated with slightly higher goals in the current match.

## Conclusions & Interpretive Synthesis
### Key Findings:

1.	Variable Selection was Well-Motivated: The 8-variable specification balances conceptual coverage (team capability, match conditions, contextual factors) with parsimony appropriate for n=104. Each variable addresses a theoretically distinct mechanism influencing goal difference.
2.	Group 23 used a training / test model of 70%, 80%, 90% to test our models to determine if the explanatory variables we selected were appropriate for this task. We also calculated the mean absolute error, mean squared error, root mean square error, and normalised root mean square error and compared them with a baseline.
3.	For further clarification our group also compared our results with the actual result of the grand final match between Argentina and Spain versus the predicted result for both Linear Regression Models 2.1 and 2.2. Our results can be viewed using the link provided to our repository in GitHub, Group 23 – Assessment 3 – Objective 2. 

Author: Danielle Whitney
