import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# FIFA World Cup 2026 data
fifa_data = {
    'home_Possession': [46.5, 48.2, 45.1, 50.3, 42.8, 55.1, 44.6, 49.2, 47.3, 51.2],
    'away_Possession': [44.6, 42.1, 48.2, 43.7, 51.2, 38.9, 47.1, 45.3, 48.9, 41.5],
    'home_xG': [7.5, 8.2, 6.1, 9.3, 5.8, 10.2, 6.9, 7.8, 8.1, 9.5],
    'away_xG': [6.0, 5.3, 7.2, 4.8, 8.1, 3.2, 7.5, 6.2, 5.9, 4.1],
    'betting_odds_home': [2.65, 2.80, 2.45, 3.10, 2.20, 3.35, 2.50, 2.75, 2.90, 3.05],
    'referee_strictness': [7.2, 6.9, 7.3, 7.1, 6.8, 7.0, 7.2, 7.4, 7.1, 6.9],
    'travel_distance_km': [4100, 3500, 5200, 2800, 6290, 1500, 4500, 3800, 5100, 2500],
    'social_sentiment_home': [0.36, 0.45, 0.25, 0.65, 0.15, 0.80, 0.40, 0.55, 0.35, 0.70],
    'goal_diff': [1, 2, 0, 2, -1, 3, 1, 1, 2, 2]
}

df = pd.DataFrame(fifa_data)

# Input variables
X = df[['home_Possession', 'away_Possession', 'home_xG', 'away_xG',
         'betting_odds_home', 'referee_strictness', 'travel_distance_km', 'social_sentiment_home']].astype(float)

# Output variable
Y = df['goal_diff'].astype(float)

# Train model with feature scaling (as per notebook)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LinearRegression()
model.fit(X_scaled, Y)
intercept = model.intercept_
coefficients = model.coef_

feature_names = ['home_Possession', 'away_Possession', 'home_xG', 'away_xG',
                 'betting_odds_home', 'referee_strictness', 'travel_distance_km', 'social_sentiment_home']


def predict_goal_diff():
    try:
        input_values = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get()),
            float(entry6.get()),
            float(entry7.get()),
            float(entry8.get())
        ]

        X_new = np.array([input_values])
        X_new_scaled = scaler.transform(X_new)
        prediction = model.predict(X_new_scaled)[0]

        result_text = f'Predicted Goal Difference: {prediction:.2f}'
        result_label.config(text=result_text, fg='darkgreen', font=('Arial', 11, 'bold'))

    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers for all fields')


# tkinter GUI
root = tk.Tk()
root.title('FIFA World Cup 2026 - Goal Difference Predictor')
root.geometry('900x700')

# Title
title = tk.Label(root, text='FIFA World Cup 2026 Goal Difference Predictor', font=('Arial', 14, 'bold'), bg='lightblue')
title.pack(pady=10)

# Create main frame with scrollable content
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Model Info
info_frame = tk.LabelFrame(main_frame, text='Model Information', font=('Arial', 10, 'bold'))
info_frame.pack(fill=tk.X, pady=5)

info_text = f'Intercept: {intercept:.4f}\n'
info_text += f'Variables: {", ".join(feature_names)}'
info_label = tk.Label(info_frame, text=info_text, justify=tk.LEFT, font=('Arial', 9))
info_label.pack(pady=5)

# Input frame
input_frame = tk.LabelFrame(main_frame, text='Input Values', font=('Arial', 10, 'bold'))
input_frame.pack(fill=tk.X, pady=5)

entries = {}
input_data = [
    ('Home Possession (%)', 'home_Possession', '27 - 58'),
    ('Away Possession (%)', 'away_Possession', '27 - 58'),
    ('Home xG', 'home_xG', '1.12 - 17.48'),
    ('Away xG', 'away_xG', '1.12 - 17.48'),
    ('Betting Odds (Home)', 'betting_odds_home', '1.72 - 3.35'),
    ('Referee Strictness (1-10)', 'referee_strictness', '6.8 - 8.0'),
    ('Travel Distance (km)', 'travel_distance_km', '1356 - 6290'),
    ('Social Sentiment (Home)', 'social_sentiment_home', '-0.17 - 0.89')
]

entry_list = []
for i in range(0, len(input_data), 2):
    row_num = i // 2

    # Left column
    label1 = tk.Label(input_frame, text=f'{input_data[i][0]}:', font=('Arial', 9, 'bold'), justify='right')
    label1.grid(row=row_num, column=0, sticky='e', padx=(5, 5), pady=5)

    entry1 = tk.Entry(input_frame, width=12)
    entry1.grid(row=row_num, column=1, sticky='ew', padx=2, pady=5)

    range_label1 = tk.Label(input_frame, text=f'({input_data[i][2]})', font=('Arial', 8), fg='gray')
    range_label1.grid(row=row_num, column=2, sticky='w', padx=(5, 20), pady=5)

    entry_list.append(entry1)
    entries[input_data[i][1]] = entry1

    # Right column (if exists)
    if i + 1 < len(input_data):
        label2 = tk.Label(input_frame, text=f'{input_data[i+1][0]}:', font=('Arial', 9, 'bold'), justify='right')
        label2.grid(row=row_num, column=3, sticky='e', padx=(5, 5), pady=5)

        entry2 = tk.Entry(input_frame, width=12)
        entry2.grid(row=row_num, column=4, sticky='ew', padx=2, pady=5)

        range_label2 = tk.Label(input_frame, text=f'({input_data[i+1][2]})', font=('Arial', 8), fg='gray')
        range_label2.grid(row=row_num, column=5, sticky='w', padx=(5, 5), pady=5)

        entry_list.append(entry2)
        entries[input_data[i+1][1]] = entry2

input_frame.columnconfigure(0, weight=0)
input_frame.columnconfigure(1, weight=1)
input_frame.columnconfigure(2, weight=0)
input_frame.columnconfigure(3, weight=0)
input_frame.columnconfigure(4, weight=1)
input_frame.columnconfigure(5, weight=0)

# Prediction button
button = tk.Button(main_frame, text='Predict Goal Difference', command=predict_goal_diff, bg='orange', font=('Arial', 11, 'bold'))
button.pack(pady=10)

# Result label
result_frame = tk.LabelFrame(main_frame, text='Prediction Result', font=('Arial', 10, 'bold'))
result_frame.pack(fill=tk.X, pady=5)
result_label = tk.Label(result_frame, text='Enter values and click Predict', font=('Arial', 10), fg='blue')
result_label.pack(pady=10)

# Export entries to global scope for predict function
entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8 = entry_list

# Plot frame
plot_frame = tk.LabelFrame(main_frame, text='Model Coefficients', font=('Arial', 10, 'bold'))
plot_frame.pack(fill=tk.BOTH, expand=True, pady=5)

# Create coefficient visualization
figure = plt.Figure(figsize=(8, 4), dpi=100)
ax = figure.add_subplot(111)

coef_sorted_indices = np.argsort(np.abs(coefficients))[::-1]
sorted_names = [feature_names[i] for i in coef_sorted_indices]
sorted_coefs = coefficients[coef_sorted_indices]

colors = ['green' if c > 0 else 'red' for c in sorted_coefs]
ax.barh(sorted_names, sorted_coefs, color=colors)
ax.set_xlabel('Coefficient Value')
ax.set_title('Standardized Feature Coefficients')
ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5)

canvas = FigureCanvasTkAgg(figure, plot_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Launch the app
root.mainloop()
