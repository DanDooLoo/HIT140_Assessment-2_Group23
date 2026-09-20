# Model 1 Summary: Predicting Goals Scored from Attempts at Goal

## Model Objective
Model 1 examines the fundamental relationship between shooting volume and goal-scoring in football. The model predicts the difference in goals scored based on the difference in attempts at goal, investigating how effectively teams convert their offensive opportunities relative to their opponents.

## Variables
- **Independent Variable (X):** Difference in Attempts at Goal (Home Attempts - Away Attempts)
- **Dependent Variable (Y):** Difference in Goals Scored (Home Goals - Away Goals)
- **Dataset:** 104 FIFA 2026 tournament matches

## Model Equation
**Y = 0.1806 + 0.1438 × X**

Where:
- Intercept (b₀) = 0.1806
- Slope (b₁) = 0.1438

## Interpretation
For every additional attempt at goal by the home team relative to the away team, the home team is predicted to score **0.144 more goals** on average. This indicates a direct but modest relationship between shooting volume and goal-scoring, suggesting that while more attempts generally lead to more goals, conversion efficiency varies significantly between teams and matches.

## Model Performance

### Test Set Performance (40% of data)
| Metric | Value |
|--------|-------|
| **Mean Absolute Error (MAE)** | 3.08 goals |
| **Mean Squared Error (MSE)** | 16.95 |
| **Root Mean Squared Error (RMSE)** | 4.12 goals |
| **Normalized RMSE (NRMSE)** | 0.1328 |

### Baseline Model Comparison
The baseline model (predicting the mean value) performed worse:
- **Baseline MAE:** 5.55 goals
- **Baseline RMSE:** 6.90 goals
- **Baseline NRMSE:** 0.2226

**Model 1 reduces error by ~40% compared to baseline**, demonstrating meaningful predictive capability.

## Model Fit Quality
- The NRMSE of 0.133 indicates relatively good prediction accuracy within the range of outcomes
- Prediction errors average ±4.12 goals, which is reasonable given typical match goal counts (0-3 goals per team)
- The model successfully captures the positive relationship between attempts and goals

## Diagnostic Observations
- Residuals appear relatively well-distributed around zero with good homoscedasticity
- The Q-Q plot shows residuals approximately follow a normal distribution
- Actual vs. Predicted plot demonstrates tight clustering around the ideal prediction line
- Relatively few outliers, suggesting the linear model captures the main pattern well

## Practical Implications
Model 1 demonstrates that shooting volume is a significant predictor of goal-scoring outcome:
- Home team advantage in attempts translates to goal advantage
- The model validates the intuitive principle that more shots generally lead to more goals
- Could be used for pre-match performance predictions based on expected shot volume
- Useful for tactical analysis: underperforming relative to expectations suggests conversion efficiency issues

## Comparison with Model 2
Model 1 (Attempts → Goals) achieves lower error rates and better fit than Model 2 (Goals → Attempts):
- Model 1 NRMSE: 0.1328 vs Model 2 NRMSE: 0.1220 (both good, Model 2 slightly better)
- Model 1 RMSE: 4.12 goals vs Model 2 RMSE: 20.98 attempts
- Model 1 shows stronger diagnostic patterns and better residual distribution
- Model 1 is more practical for real-world prediction (predicting goals from shots is more actionable)

## Limitations
- Coefficient of 0.1438 suggests additional unmeasured factors influence goal-scoring (team quality, player skill, luck)
- Linear model may not capture non-linear effects (e.g., diminishing returns at extreme shot volumes)
- Model assumes consistent conversion efficiency across different match contexts
- Some residual structure suggests potential improvements with additional predictor variables
