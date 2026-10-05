"""
Enhanced Linear Regression Analysis with Multiple Test-Train Splits
Calculates metrics for 70%, 80%, and 90% test sizes
Compares against Baseline (predicting mean)
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("ENHANCED LINEAR REGRESSION WITH MULTIPLE TEST SPLITS")
print("="*70)

# Load data (using your existing analysis)
matches_data = pd.read_csv('matchesk.csv')
external_data = pd.read_csv('external_factors.csv')
teams_data = pd.read_csv('teamsk.csv')
venues_data = pd.read_csv('venuesk.csv')

# Merge data
dataset = matches_data.merge(external_data, left_on='match_id', right_on='match_id', how='inner')
dataset['goal_diff'] = dataset['goals_home'] - dataset['goals_away']

# Add ELO ratings
teams_elo_map = dict(zip(teams_data['team_id'].astype(str), teams_data['elo_rating']))
dataset['team_home_str'] = dataset['team_home'].astype(str)
dataset['team_away_str'] = dataset['team_away'].astype(str)
dataset['home_elo_rating'] = dataset['team_home_str'].map(teams_elo_map)
dataset['away_elo_rating'] = dataset['team_away_str'].map(teams_elo_map)

avg_elo = teams_data['elo_rating'].mean()
dataset['home_elo_rating'].fillna(avg_elo, inplace=True)
dataset['away_elo_rating'].fillna(avg_elo, inplace=True)

# Add possession
dataset['home_Possession'] = 50 + np.random.normal(0, 3, len(dataset))
dataset['home_Possession'] = dataset['home_Possession'].clip(30, 70)

# Add pitch quality
avg_pitch_quality = venues_data['pitch_quality_score'].mean()
dataset['pitch_quality'] = avg_pitch_quality

# Create features
dataset['elo_rating_diff'] = dataset['home_elo_rating'] - dataset['away_elo_rating']

X_features = [
    'elo_rating_diff', 'xG_home', 'xG_away', 'home_Possession',
    'travel_distance_km', 'betting_odds_home', 'pitch_quality', 'referee_strictness'
]

final_df = dataset[X_features + ['goal_diff']].dropna()
X = final_df[X_features].copy()
y = final_df['goal_diff'].copy()

print(f"\nTotal dataset: {len(X)} matches\n")

# ============================================================================
# TEST MULTIPLE SPLITS: 70%, 80%, 90%
# ============================================================================

results_summary = []

for test_size in [0.30, 0.20, 0.10]:  # 30%, 20%, 10% test = 70%, 80%, 90% train
    test_pct = int((1 - test_size) * 100)

    print(f"\n{'='*70}")
    print(f"TEST SIZE: {test_pct}% TRAINING - {int(test_size*100)}% TEST")
    print(f"{'='*70}")

    X_scaled = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=test_size, random_state=42
    )

    print(f"Train samples: {len(X_train)}, Test samples: {len(X_test)}")

    # ========================================================================
    # MLP PERFORMANCE (Your Linear Regression Model)
    # ========================================================================
    print(f"\nMLP PERFORMANCE:")
    print("-" * 70)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred_test = model.predict(X_test)

    # Calculate metrics
    mae = mean_absolute_error(y_test, y_pred_test)
    mse = mean_squared_error(y_test, y_pred_test)
    rmse = np.sqrt(mse)
    rmse_normalized = rmse / y_test.std()  # Normalized by test set std
    r2 = r2_score(y_test, y_pred_test)

    intercept = model.intercept_
    coef = model.coef_  # Array of coefficients

    print(f"Intercept: {intercept:.6f}")
    print(f"Coefficients: {[f'{c:.6f}' for c in coef]}")
    print(f"\nMAE: {mae:.6f}")
    print(f"MSE: {mse:.6f}")
    print(f"RMSE: {rmse:.6f}")
    print(f"RMSE (Normalised): {rmse_normalized:.6f}")
    print(f"R²: {r2:.6f}")

    # ========================================================================
    # BASELINE PERFORMANCE (Predict Mean)
    # ========================================================================
    print(f"\nBASELINE PERFORMANCE (Predicting Mean):")
    print("-" * 70)

    # Baseline: always predict the mean of training set
    y_pred_baseline = np.full_like(y_test, y_train.mean())

    mae_baseline = mean_absolute_error(y_test, y_pred_baseline)
    mse_baseline = mean_squared_error(y_test, y_pred_baseline)
    rmse_baseline = np.sqrt(mse_baseline)
    rmse_baseline_normalized = rmse_baseline / y_test.std()
    r2_baseline = r2_score(y_test, y_pred_baseline)

    print(f"MAE: {mae_baseline:.6f}")
    print(f"MSE: {mse_baseline:.6f}")
    print(f"RMSE: {rmse_baseline:.6f}")
    print(f"RMSE (Normalised): {rmse_baseline_normalized:.6f}")
    print(f"R²: {r2_baseline:.6f}")

    # ========================================================================
    # IMPROVEMENT OVER BASELINE
    # ========================================================================
    print(f"\nIMPROVEMENT OVER BASELINE:")
    print("-" * 70)

    mae_improvement = ((mae_baseline - mae) / mae_baseline) * 100
    rmse_improvement = ((rmse_baseline - rmse) / rmse_baseline) * 100
    r2_improvement = r2 - r2_baseline

    print(f"MAE Improvement: {mae_improvement:.2f}%")
    print(f"RMSE Improvement: {rmse_improvement:.2f}%")
    print(f"R² Improvement: {r2_improvement:.6f}")

    # Store results
    results_summary.append({
        'Test Size': f"{test_pct}% Train / {int(test_size*100)}% Test",
        'Intercept': intercept,
        'MAE (MLP)': mae,
        'MSE (MLP)': mse,
        'RMSE (MLP)': rmse,
        'RMSE_Norm (MLP)': rmse_normalized,
        'R² (MLP)': r2,
        'MAE (Baseline)': mae_baseline,
        'MSE (Baseline)': mse_baseline,
        'RMSE (Baseline)': rmse_baseline,
        'RMSE_Norm (Baseline)': rmse_baseline_normalized,
        'R² (Baseline)': r2_baseline,
    })

# ============================================================================
# SUMMARY TABLE
# ============================================================================
print("\n" + "="*70)
print("SUMMARY TABLE FOR YOUR REPORT")
print("="*70)

summary_df = pd.DataFrame(results_summary)
print("\n" + summary_df.to_string(index=False))

# Save to CSV for easy viewing
summary_df.to_csv('model_comparison_multiple_splits.csv', index=False)
print("\n✓ Saved: model_comparison_multiple_splits.csv")

# ============================================================================
# FORMATTED OUTPUT FOR YOUR TABLE
# ============================================================================
print("\n" + "="*70)
print("FORMATTED OUTPUT FOR YOUR ASSIGNMENT TABLE")
print("="*70)

for idx, row in summary_df.iterrows():
    print(f"\n{row['Test Size'].upper()}")
    print(f"Intercept: {row['Intercept']:.6f}")
    print(f"\nMLP Performance:")
    print(f"  MAE: {row['MAE (MLP)']:.6f}")
    print(f"  MSE: {row['MSE (MLP)']:.6f}")
    print(f"  RMSE: {row['RMSE (MLP)']:.6f}")
    print(f"  RMSE (Normalised): {row['RMSE_Norm (MLP)']:.6f}")
    print(f"  R²: {row['R² (MLP)']:.6f}")

    print(f"\nBaseline Performance:")
    print(f"  MAE: {row['MAE (Baseline)']:.6f}")
    print(f"  MSE: {row['MSE (Baseline)']:.6f}")
    print(f"  RMSE: {row['RMSE (Baseline)']:.6f}")
    print(f"  RMSE (Normalised): {row['RMSE_Norm (Baseline)']:.6f}")
    print(f"  R²: {row['R² (Baseline)']:.6f}")

print("\n" + "="*70)
print("ANALYSIS COMPLETE ✓")
print("="*70)
