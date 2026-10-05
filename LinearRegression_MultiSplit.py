"""
Linear Regression Analysis - Multiple Test-Train Splits
Calculates metrics for 70%, 80%, and 90% training data
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
print("LINEAR REGRESSION - MULTIPLE TEST-TRAIN SPLITS ANALYSIS")
print("="*70)

# Load data
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
np.random.seed(42)
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

print(f"Total dataset: {len(X)} matches\n")

# Store all results
all_results = []

# Test the three splits: 70%, 80%, 90% training
test_splits = [
    (0.30, "70% Training / 30% Test"),
    (0.20, "80% Training / 20% Test"),
    (0.10, "90% Training / 10% Test")
]

for test_size, split_name in test_splits:
    print("\n" + "="*70)
    print(f"TEST SIZE: {split_name}")
    print("="*70)

    X_scaled = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=test_size, random_state=42
    )

    print(f"Train samples: {len(X_train)}, Test samples: {len(X_test)}")

    # ====================================================================
    # MLP (Linear Regression) Performance
    # ====================================================================
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred_test = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred_test)
    mse = mean_squared_error(y_test, y_pred_test)
    rmse = np.sqrt(mse)
    rmse_normalized = rmse / y_test.std()
    r2 = r2_score(y_test, y_pred_test)
    intercept = model.intercept_

    print(f"\nMLP PERFORMANCE:")
    print(f"  Intercept: {intercept:.6f}")
    print(f"  MAE: {mae:.6f}")
    print(f"  MSE: {mse:.6f}")
    print(f"  RMSE: {rmse:.6f}")
    print(f"  RMSE (Normalised): {rmse_normalized:.6f}")
    print(f"  R²: {r2:.6f}")

    # ====================================================================
    # Baseline Performance (Predicting Mean)
    # ====================================================================
    y_pred_baseline = np.full_like(y_test, y_train.mean(), dtype=float)

    mae_baseline = mean_absolute_error(y_test, y_pred_baseline)
    mse_baseline = mean_squared_error(y_test, y_pred_baseline)
    rmse_baseline = np.sqrt(mse_baseline)
    rmse_baseline_normalized = rmse_baseline / y_test.std()
    r2_baseline = r2_score(y_test, y_pred_baseline)

    print(f"\nBASELINE PERFORMANCE (Predicting Mean):")
    print(f"  MAE: {mae_baseline:.6f}")
    print(f"  MSE: {mse_baseline:.6f}")
    print(f"  RMSE: {rmse_baseline:.6f}")
    print(f"  RMSE (Normalised): {rmse_baseline_normalized:.6f}")
    print(f"  R²: {r2_baseline:.6f}")

    # Store results
    all_results.append({
        'Test Size': split_name,
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
        'R² (Baseline)': r2_baseline
    })

# ========================================================================
# Save all results to CSV
# ========================================================================
print("\n" + "="*70)
print("SAVING RESULTS")
print("="*70)

results_df = pd.DataFrame(all_results)
results_df.to_csv('model_comparison_all_splits.csv', index=False)
print("✓ Saved: model_comparison_all_splits.csv")

# Print summary table
print("\n" + "="*70)
print("SUMMARY TABLE")
print("="*70)
print("\n" + results_df.to_string(index=False))

print("\n" + "="*70)
print("ANALYSIS COMPLETE ✓")
print("="*70)
