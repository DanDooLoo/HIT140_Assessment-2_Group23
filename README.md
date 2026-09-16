#  HIT140 Assessment 2 – Foundations of Data Science - Charles Darwin University - September 2026 

## Group 23: 
- Danielle S407528
- Gabrielle S375255
- Judith S395778
- Manuela S320756

# ⚽ Project Overview - FIFA World Cup Analysis ⚽
This project investigates the FIFA World Cup 2026 statistics.
<br>

## 📌 Objective 1:
Perform four (4) distinct analytic tasks that analyse the FIFA World Cup 2026 statistics using Python.

Each analytic task must be driven by a distinct question that will be answered using all the following skills:
* Analytic question formulation
* Data wrangling
* Data preparation and sampling
* Descriptive statistics
* Inferential statistics (Confidence interval)
* Inferential statistics (Two-sample t-Test)

Each analytic task must also have a distinct focal point of investigation that differs from the other tasks. 
<br>
<br>

# 🎯 Analysis Research Questions

### Research Question 1 - Yellow Cards
During the FIFA World Cup 2026, what was the average age of the players and yellow cards that were issued throughout the tournament? Are players with less time on the field more likely to be issued with yellow cards?

### Research Question 2 - Minuets Played - Position Analysis
What was the average number of minutes played by field position 
- Exploring the relationship between team ranking and attacking performance 
Analysing Goals Scored and FIFA Rankings 
- Exploring whether higher-ranked teams scored more goals during the FIFA World Cup 2026.

### Research Question 3 - Possessions
Do high possession and low possession teams show significant difference in team composition in the FIFA26 World Cup?

### Research Question 4 - Goalkeeper Aggression vs Save Efficiency
Do goalkeepers with higher aggression have significantly different save efficiency?

#### Sub‑questions:
1. Are aggressive keepers more efficient?
2. Less efficient?
3. Or no different at all?
<br>

# 📊 Data Sources & Datasets

### 🔗 Sources: 
1. FIFA Official Website
2. FB Ref

#### Links: 
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics
- https://fbref.com/en/

### 🧱 Datasets:
- Goalkeeper = goalkeepers: 61
- Rounds
- Matches
- FBREF Opponents
- FBREF Squads
- FBREF Stats
- FBREF Discipline
- Venues
- Teams
<br>

## 🧪 Random Sample Generator Used
- Random sample: 30 (random_state = 42)
- gk_sample = gk.sample(30, random_state=42)
<br>

# 📈 Metrics & Methods

### 🗝️ Key Metrics:
- **Aggression Ratio** = Outside Actions / Inside Actions  
- **Save Efficiency** = Saves / Total Actions
- **Yellow Cards**
- **Possessions**
- **Penalty Shoot Out**

### ⚙️ Methods Used:
- Data wrangling (Pandas)
- Data preparation and sampling (Python & Juypter Notebooks)
- Descriptive statistics
- Inferential statistics (Confidence intervals (95%))
- Inferential statistics (One & Two-sample t-test)
- Visulisations (Galton's Bell Curve, Scatter (Seaborn), Boxplot, Plot.Figure, Histogram, Violinplot)
<br>

# 🖥️ Coding Languages and Packages Utilised

### 🐍 Coding Lanugages:
- Python
- Juypter Notebooks (Python)
- HTML
- Markdown

### 📦 Packages:
- Pandas as PD
- Matplotlib.pyplot as plt
- Scipy.stat as st
- Numpy as np
- Math
- Statsmodel.stats.weightstats as stm
- Seaborn
<br>

# 🖼️ Visualisations
Include:
- Aggression ratio distributions  
- Save efficiency distributions  
- Confidence interval plots  
- Galton bell curve overlays  
- Histogram of yellow cards
- Violin distribution plots
<br>

# 💡 Key Findings
- High and low aggression groups show overlapping confidence intervals.
- Save efficiency differences are descriptive only, not statistically significant.
- Aggression does **not** predict save efficiency in this sample.
<br>

# 📽️ YouTube Video
A full narrated breakdown of the analysis is available on YouTube.  
https://youtu.be/ToZjo_cY3Vo

## 📂 Repository Structure
- TBD......

### Author
<img width="331" height="424" alt="image" src="https://github.com/user-attachments/assets/dbc2c40c-895d-48af-9389-574eddaee24b" />


Danielle Whitney - Student # S407528
