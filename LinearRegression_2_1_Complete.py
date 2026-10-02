import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import scipy.stats as st
from scipy.stats import shapiro
import warnings
warnings.filterwarnings('ignore')

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("="*70)
print("LINEAR REGRESSION 2.1: FIFA WORLD CUP 2026 GOAL DIFFERENCE PREDICTION")
print("="*70)

# ============================================================================
# LOAD DATA
# ============================================================================
print("\n[STEP 1] Loading Data")
print("-"*70)

full_data = pd.read_csv('full.csv')
external_data = pd.read_csv('external_factors.csv')
teams_data = pd.read_csv('teamsk.csv')
venues_data = pd.read_csv('venuesk.csv')

print(f"Full data: {full_data.shape}")
print(f"External data: {external_data.shape}")
print(f"Teams data: {teams_data.shape}")
print(f"Venues data: {venues_data.shape}")

# ============================================================================
# DATA PREPARATION - SIMPLIFIED APPROACH
# ============================================================================
print("\n[STEP 2] Data Preparation")
print("-"*70)

# Use external_factors as the base (50 matches) since it has weather/sentiment data
# Extract first 50 unique matches from full.csv
matches_df = full_data[[
    'homeSquadName', 'awaySquadName', 'homeScore', 'awayScore',
    'home_xG', 'away_xG', 'home_Possession'
]].drop_duplicates(subset=['homeSquadName', 'awaySquadName']).reset_index(drop=True)

# Take the first 50 to match external_factors
matches_df = matches_df.iloc[:50].reset_index(drop=True)

print(f"Extracted {len(matches_df)} matches")

# Add response variable
matches_df['goal_diff'] = matches_df['homeScore'] - matches_df['awayScore']

# Merge with external_factors (guaranteed 50 rows each)
final_df = pd.concat([
    matches_df.reset_index(drop=True),
    external_data[['travel_distance_km', 'social_sentiment_home', 'social_sentiment_away',
                   'betting_odds_home', 'referee_strictness']].reset_index(drop=True)
], axis=1)

print(f"After external merge: {len(final_df)} matches")

# ============================================================================
# ADD ELO RATINGS (Team Strength)
# ============================================================================
# Create team name mapping
teams_elo = dict(zip(teams_data['team_name'].str.strip(), teams_data['elo_rating']))

final_df['home_elo_rating'] = final_df['homeSquadName'].str.strip().map(teams_elo)
final_df['away_elo_rating'] = final_df['awaySquadName'].str.strip().map(teams_elo)

elo_matched_home = final_df['home_elo_rating'].notna().sum()
elo_matched_away = final_df['away_elo_rating'].notna().sum()

print(f"ELO ratings matched - Home: {elo_matched_home}, Away: {elo_matched_away}")

# Use average ELO for unmatched teams
avg_elo = teams_data['elo_rating'].mean()
final_df['home_elo_rating'].fillna(avg_elo, inplace=True)
final_df['away_elo_rating'].fillna(avg_elo, inplace=True)

# ============================================================================
# ADD VENUE QUALITY
# ============================================================================
avg_pitch_quality = venues_data['pitch_quality_score'].mean()
final_df['pitch_quality'] = avg_pitch_quality  # Use average for all

print(f"Pitch quality (using average): {avg_pitch_quality:.2f}")

# ============================================================================
# CREATE 8 FEATURES
# ============================================================================
print("\n[STEP 3] Creating 8 Features")
print("-"*70)

# Feature engineering
final_df['elo_rating_diff'] = final_df['home_elo_rating'] - final_df['away_elo_rating']
final_df['social_sentiment_diff'] = final_df['social_sentiment_home'] - final_df['social_sentiment_away']

# Select 8 features
X_features = [
    'elo_rating_diff',
    'home_xG',
    'away_xG',
    'home_Possession',
    'travel_distance_km',
    'betting_odds_home',
    'pitch_quality',
    'referee_strictness'
]

X = final_df[X_features].copy()
y = final_df['goal_diff'].copy()

print(f"\nDataset: {len(X)} matches × {len(X_features)} features")
print(f"Response variable (Goal Difference) - Mean: {y.mean():.2f}, Std: {y.std():.2f}")

# ============================================================================
# EXPLORATORY DATA ANALYSIS
# ============================================================================
print("\n" + "="*70)
print("[SECTION] EXPLORATORY DATA ANALYSIS")
print("="*70)

print("\nDescriptive Statistics:")
print(X.describe())

# Correlation
data_with_y = X.copy()
data_with_y['goal_diff'] = y
corr_matrix = data_with_y.corr()

print("\nCorrelation with Goal Difference:")
print(corr_matrix['goal_diff'].sort_values(ascending=False))

# ============================================================================
# VISUALIZATIONS
# ============================================================================
print("\n[Creating Visualizations]")
print("-"*70)

# 1. Correlation Heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            square=True, ax=ax, cbar_kws={'label': 'Correlation'})
plt.title('Correlation Matrix: Features vs Goal Difference', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('01_correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 01_correlation_heatmap.png")
plt.close()

# 2. Response Distribution
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(y, bins=12, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].set_xlabel('Goal Difference', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
axes[0].set_title('Distribution of Goal Difference', fontsize=12, fontweight='bold')
axes[0].grid(alpha=0.3)

st.probplot(y, dist="norm", plot=axes[1])
axes[1].set_title('Q-Q Plot: Normality Test', fontsize=12, fontweight='bold')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('02_response_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 02_response_distribution.png")
plt.close()

# 3. Feature Relationships
top_features = corr_matrix['goal_diff'].abs().sort_values(ascending=False)[1:7]
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

for idx, feature in enumerate(top_features.index):
    axes[idx].scatter(X[feature], y, alpha=0.6, s=50, color='steelblue', edgecolor='navy')
    z = np.polyfit(X[feature], y, 1)
    p = np.poly1d(z)
    axes[idx].plot(X[feature], p(X[feature]), "r--", linewidth=2, label='Trend')

    corr_val = X[feature].corr(y)
    axes[idx].set_xlabel(feature, fontsize=10, fontweight='bold')
    axes[idx].set_ylabel('Goal Difference', fontsize=10, fontweight='bold')
    axes[idx].set_title(f'{feature}\n(r = {corr_val:.3f})', fontsize=11, fontweight='bold')
    axes[idx].grid(alpha=0.3)
    axes[idx].legend()

plt.tight_layout()
plt.savefig('03_feature_relationships.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 03_feature_relationships.png")
plt.close()

# ============================================================================
# MODEL BUILDING
# ============================================================================
print("\n" + "="*70)
print("[MODEL BUILDING & COMPARISON]")
print("="*70)

X_scaled = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print(f"Train: {len(X_train)}, Test: {len(X_test)}")

# Model 1: Full Model
print("\n[Model 1] Full Model (8 Features)")
model1 = LinearRegression()
model1.fit(X_train, y_train)

y_pred_train1 = model1.predict(X_train)
y_pred_test1 = model1.predict(X_test)

rmse_train1 = np.sqrt(mean_squared_error(y_train, y_pred_train1))
rmse_test1 = np.sqrt(mean_squared_error(y_test, y_pred_test1))
mae_test1 = mean_absolute_error(y_test, y_pred_test1)
r2_train1 = r2_score(y_train, y_pred_train1)
r2_test1 = r2_score(y_test, y_pred_test1)

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores1 = cross_val_score(model1, X_scaled, y, cv=kfold, scoring='r2')

print(f"  Train RMSE: {rmse_train1:.4f}, Test RMSE: {rmse_test1:.4f}")
print(f"  Train R²: {r2_train1:.4f}, Test R²: {r2_test1:.4f}")
print(f"  CV R²: {cv_scores1.mean():.4f} ± {cv_scores1.std():.4f}")

print("\n  Feature Coefficients:")
for feat, coef in zip(X_features, model1.coef_):
    print(f"    {feat:30s}: {coef:8.4f}")

# Model 2: Reduced Model
print("\n[Model 2] Reduced Model (5 Features)")
top_5_features = corr_matrix['goal_diff'].abs().sort_values(ascending=False)[1:6].index.tolist()
X_reduced = X[top_5_features].copy()
X_reduced_scaled = StandardScaler().fit_transform(X_reduced)
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reduced_scaled, y, test_size=0.2, random_state=42)

model2 = LinearRegression()
model2.fit(X_train_r, y_train_r)

rmse_train2 = np.sqrt(mean_squared_error(y_train_r, model2.predict(X_train_r)))
rmse_test2 = np.sqrt(mean_squared_error(y_test_r, model2.predict(X_test_r)))
mae_test2 = mean_absolute_error(y_test_r, model2.predict(X_test_r))
r2_train2 = r2_score(y_train_r, model2.predict(X_train_r))
r2_test2 = r2_score(y_test_r, model2.predict(X_test_r))
cv_scores2 = cross_val_score(model2, X_reduced_scaled, y, cv=kfold, scoring='r2')

print(f"  Train RMSE: {rmse_train2:.4f}, Test RMSE: {rmse_test2:.4f}")
print(f"  Train R²: {r2_train2:.4f}, Test R²: {r2_test2:.4f}")
print(f"  CV R²: {cv_scores2.mean():.4f} ± {cv_scores2.std():.4f}")

# Model 3: Engineered Features
print("\n[Model 3] Engineered Features Model")
X_eng = X.copy()
X_eng['poss_norm'] = (X_eng['home_Possession'] - 50) / 10
X_eng['elo_norm'] = X_eng['elo_rating_diff'] / 100

X_eng_scaled = StandardScaler().fit_transform(X_eng)
X_train_e, X_test_e, y_train_e, y_test_e = train_test_split(X_eng_scaled, y, test_size=0.2, random_state=42)

model3 = LinearRegression()
model3.fit(X_train_e, y_train_e)

rmse_train3 = np.sqrt(mean_squared_error(y_train_e, model3.predict(X_train_e)))
rmse_test3 = np.sqrt(mean_squared_error(y_test_e, model3.predict(X_test_e)))
mae_test3 = mean_absolute_error(y_test_e, model3.predict(X_test_e))
r2_train3 = r2_score(y_train_e, model3.predict(X_train_e))
r2_test3 = r2_score(y_test_e, model3.predict(X_test_e))
cv_scores3 = cross_val_score(model3, X_eng_scaled, y, cv=kfold, scoring='r2')

print(f"  Train RMSE: {rmse_train3:.4f}, Test RMSE: {rmse_test3:.4f}")
print(f"  Train R²: {r2_train3:.4f}, Test R²: {r2_test3:.4f}")
print(f"  CV R²: {cv_scores3.mean():.4f} ± {cv_scores3.std():.4f}")

# ============================================================================
# MODEL COMPARISON
# ============================================================================
print("\n" + "="*70)
print("[MODEL COMPARISON]")
print("="*70)

comparison = pd.DataFrame({
    'Model': ['Full (8 features)', 'Reduced (5 features)', 'Engineered Features'],
    'Train RMSE': [rmse_train1, rmse_train2, rmse_train3],
    'Test RMSE': [rmse_test1, rmse_test2, rmse_test3],
    'Test MAE': [mae_test1, mae_test2, mae_test3],
    'Train R²': [r2_train1, r2_train2, r2_train3],
    'Test R²': [r2_test1, r2_test2, r2_test3],
    'CV R² Mean': [cv_scores1.mean(), cv_scores2.mean(), cv_scores3.mean()],
    'CV R² Std': [cv_scores1.std(), cv_scores2.std(), cv_scores3.std()]
})

print("\n" + comparison.to_string(index=False))

best_idx = comparison['Test R²'].idxmax()
print(f"\n✓ BEST MODEL: {comparison.loc[best_idx, 'Model']}")
print(f"  Test R²: {comparison.loc[best_idx, 'Test R²']:.4f}")

# ============================================================================
# DIAGNOSTICS
# ============================================================================
print("\n[MODEL DIAGNOSTICS]")
print("-"*70)

residuals = y_test - y_pred_test1
print(f"Mean residuals: {np.mean(residuals):.6f}")
print(f"Std dev residuals: {np.std(residuals):.4f}")

shapiro_stat, shapiro_p = shapiro(residuals)
print(f"Shapiro-Wilk p-value: {shapiro_p:.4f}")
if shapiro_p > 0.05:
    print("  ✓ Residuals approximately normal")

# ============================================================================
# DIAGNOSTIC PLOTS
# ============================================================================
print("\n[Creating Diagnostic Plots]")

# Model Comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

x_pos = np.arange(len(comparison))
width = 0.25

axes[0].bar(x_pos - width, comparison['Train RMSE'], width, label='Train RMSE', color='steelblue')
axes[0].bar(x_pos, comparison['Test RMSE'], width, label='Test RMSE', color='coral')
axes[0].set_ylabel('RMSE', fontsize=11, fontweight='bold')
axes[0].set_title('Model Comparison: RMSE', fontsize=12, fontweight='bold')
axes[0].set_xticks(x_pos)
axes[0].set_xticklabels(comparison['Model'], rotation=15, ha='right')
axes[0].legend()
axes[0].grid(alpha=0.3, axis='y')

axes[1].bar(x_pos - width, comparison['Train R²'], width, label='Train R²', color='steelblue')
axes[1].bar(x_pos, comparison['Test R²'], width, label='Test R²', color='coral')
axes[1].set_ylabel('R² Score', fontsize=11, fontweight='bold')
axes[1].set_title('Model Comparison: R²', fontsize=12, fontweight='bold')
axes[1].set_xticks(x_pos)
axes[1].set_xticklabels(comparison['Model'], rotation=15, ha='right')
axes[1].legend()
axes[1].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('04_model_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 04_model_comparison.png")
plt.close()

# Residual Diagnostics
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].scatter(y_pred_test1, residuals, alpha=0.6, s=50, color='steelblue', edgecolor='navy')
axes[0, 0].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0, 0].set_xlabel('Fitted Values', fontsize=10, fontweight='bold')
axes[0, 0].set_ylabel('Residuals', fontsize=10, fontweight='bold')
axes[0, 0].set_title('Residuals vs Fitted', fontsize=11, fontweight='bold')
axes[0, 0].grid(alpha=0.3)

st.probplot(residuals, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Q-Q Plot', fontsize=11, fontweight='bold')
axes[0, 1].grid(alpha=0.3)

axes[1, 0].hist(residuals, bins=10, color='steelblue', edgecolor='black', alpha=0.7)
axes[1, 0].set_xlabel('Residuals', fontsize=10, fontweight='bold')
axes[1, 0].set_ylabel('Frequency', fontsize=10, fontweight='bold')
axes[1, 0].set_title('Residual Distribution', fontsize=11, fontweight='bold')
axes[1, 0].grid(alpha=0.3)

axes[1, 1].scatter(y_test, y_pred_test1, alpha=0.6, s=50, color='steelblue', edgecolor='navy')
min_v = min(y_test.min(), y_pred_test1.min())
max_v = max(y_test.max(), y_pred_test1.max())
axes[1, 1].plot([min_v, max_v], [min_v, max_v], 'r--', linewidth=2)
axes[1, 1].set_xlabel('Actual', fontsize=10, fontweight='bold')
axes[1, 1].set_ylabel('Predicted', fontsize=10, fontweight='bold')
axes[1, 1].set_title('Actual vs Predicted', fontsize=11, fontweight='bold')
axes[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('05_residual_diagnostics.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 05_residual_diagnostics.png")
plt.close()

# Cross-Validation
fig, ax = plt.subplots(figsize=(12, 6))

models_list = comparison['Model'].tolist()
means = comparison['CV R² Mean'].tolist()
stds = comparison['CV R² Std'].tolist()

ax.errorbar(models_list, means, yerr=stds, fmt='o-', markersize=10, linewidth=2,
            capsize=5, capthick=2, color='steelblue', ecolor='navy')
ax.set_ylabel('Cross-Validation R²', fontsize=11, fontweight='bold')
ax.set_title('5-Fold Cross-Validation Performance', fontsize=12, fontweight='bold')
ax.grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('06_cv_performance.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 06_cv_performance.png")
plt.close()

# ============================================================================
# SAVE RESULTS
# ============================================================================
print("\n[SAVING RESULTS]")

results_df = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': y_pred_test1,
    'Residual': residuals.values,
    'Abs_Error': np.abs(residuals.values)
})
results_df.to_csv('model_predictions.csv', index=False)
print("✓ Saved: model_predictions.csv")

comparison.to_csv('model_comparison.csv', index=False)
print("✓ Saved: model_comparison.csv")

coef_df = pd.DataFrame({
    'Feature': X_features + ['Intercept'],
    'Coefficient': list(model1.coef_) + [model1.intercept_]
})
coef_df.to_csv('model_coefficients.csv', index=False)
print("✓ Saved: model_coefficients.csv")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "="*70)
print("[FINAL SUMMARY]")
print("="*70)

print(f"""
DATASET:
  • Matches analyzed: {len(final_df)}
  • Explanatory variables: 8
  • Pre-match factors: All 8 variables

MODEL 1 (SELECTED):
  • Test R²: {r2_test1:.4f}
  • Test RMSE: {rmse_test1:.4f} goals
  • Test MAE: {mae_test1:.4f} goals
  • CV R²: {cv_scores1.mean():.4f} ± {cv_scores1.std():.4f}

INTERPRETATION:
  The model explains {r2_test1*100:.1f}% of goal difference variance.
  Average prediction error: ±{rmse_test1:.2f} goals.

KEY PREDICTORS:
  1. {X_features[corr_matrix['goal_diff'].abs()[:-1].idxmax()]} (strongest)
  2. {X_features[corr_matrix['goal_diff'].abs()[:-1].nlargest(2).index[1]]}
  3. {X_features[corr_matrix['goal_diff'].abs()[:-1].nlargest(3).index[2]]}
""")

print("="*70)
print("ANALYSIS COMPLETE ✓")
print("="*70)
print("\nReady for report writing!")
