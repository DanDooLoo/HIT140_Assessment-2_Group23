# Model 2 Summary: Predicting Attempts at Goal from Goals Scored

## Model Objective
Model 2 investigates the relationship between goal-scoring differences and shooting attempt differences between home and away teams. The model predicts the difference in attempts at goal based on the difference in goals scored, examining whether goals scored can predict team attacking effort.

## Variables
- **Independent Variable (X):** Difference in Goals Scored (Home Goals - Away Goals)
- **Dependent Variable (Y):** Difference in Attempts at Goal (Home Attempts - Away Attempts)
- **Dataset:** 104 FIFA 2026 tournament matches

## Model Equation
**Y = 4.0546 + 5.3176 × X**

Where:
- Intercept (b₀) = 4.0546
- Slope (b₁) = 5.3176

## Interpretation
For every additional goal scored by the home team relative to the away team, the home team is predicted to have **5.32 more attempts at goal** on average. This strong positive relationship suggests that teams scoring more goals tend to take significantly more shots, indicating an aggressive offensive strategy.

## Model Performance

### Test Set Performance (40% of data)
| Metric | Value |
|--------|-------|
| **Mean Absolute Error (MAE)** | 16.02 attempts |
| **Mean Squared Error (MSE)** | 440.24 |
| **Root Mean Squared Error (RMSE)** | 20.98 attempts |
| **Normalized RMSE (NRMSE)** | 0.1220 |

### Baseline Model Comparison
The baseline model (predicting the mean value) performed worse:
- **Baseline MAE:** 34.01 attempts
- **Baseline RMSE:** 41.11 attempts
- **Baseline NRMSE:** 0.2390

**Model 2 reduces error by ~53% compared to baseline**, indicating reasonable predictive power.

## Model Fit Quality
- The NRMSE of 0.122 suggests moderate prediction accuracy relative to the range of outcomes
- The model explains the relationship between goals and attempts, though prediction errors average ±20.98 attempts
- The strong slope coefficient (5.3176) indicates a robust linear relationship

## Diagnostic Observations
- Residuals show some heteroscedasticity (variance increases at higher fitted values)
- The Q-Q plot reveals slight deviations from normality, particularly in the tails
- Actual vs. Predicted plot shows reasonable scatter around the ideal line, with some outliers at extreme values

## Practical Implications
Model 2 demonstrates that goal-scoring differential is a significant predictor of shot volume differential. Teams that score more goals relative to their opponents also take substantially more attempts, suggesting:
- Offensive momentum impacts both scoring and shooting behavior
- Goals and attempts are strongly correlated in match outcomes
- The model could support tactical analysis of team attacking efficiency

## Limitations
- Average prediction error of ~21 attempts is substantial given typical match shot counts
- Model assumes linear relationship; actual patterns may be non-linear
- Residual patterns suggest room for model refinement through additional variables
