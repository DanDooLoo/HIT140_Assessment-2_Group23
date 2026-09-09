#  HIT140 Assessment 2 – Foundations of Data Science - Charles Darwin University - September 2026 
### Group 23 – Danielle, Gabrielle, Judith, Manuela

## 📌 Project Overview - FIFA World Cup Analysis ⚽
This project investigates whether aggressive goalkeepers — defined by actions outside the penalty area — have significantly different save efficiency compared to less aggressive goalkeepers.  
The analysis uses FIFA World Cup 2026 goalkeeper data.

## 🎯 Research Question 1 - Yellow Cards
During the FIFA World Cup 2026, what was the average age of the players and yellow cards that were issued throughout the tournament? Are players with less time on the field more likely to be issued with yellow cards?

## 🎯 Research Question 2 - Judith - Penalty Shoot Outs
add text here.....

## 🎯 Research Question 3 - Gabby - Possessions
add text here.........

## 🎯 Research Question 4 - Goalkeeper Aggression vs Save Efficiency
Do goalkeepers with higher aggression have significantly different save efficiency?

   # Sub‑questions:
     1. Are aggressive keepers more efficient?
     2. Less efficient?
     3. Or no different at all?

## 📊 Data Sources & Datasets
## 🔗 Source: 
- FIFA Official Website
- FB Ref

## Link: 
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics
- https://fbref.com/en/

## 🧱 Dataset
- Goalkeeper = goalkeepers: 61
- Rounds
- Matches
- FBREF Opponents
- FBREF Squads
- FBREF Stats
- FBREF Discipline
- Venues
- Teams

## 🧪 Random Sample Generator Used
- Random sample: 30 (random_state = 42)
- gk_sample = gk.sample(30, random_state=42)

### 📈 Key Metrics:
- **Aggression Ratio** = Outside Actions / Inside Actions  
- **Save Efficiency** = Saves / Total Actions
- **Yellow Cards**
- **Possessions**
- **Penalty Shoot Out**

## ⚙️ Methods Used
- Data wrangling (Pandas)
- Data preparation and sampling (Python & Juypter Notebooks)
- Descriptive statistics
- Inferential statistics (Confidence intervals (95%))
- Inferential statistics (One & Two-sample t-test)
- Visulisations (Galton's Bell Curve, Scatter (Seaborn), Boxplot, Plot.Figure, Histogram, Violinplot)

## 🖥️ Coding Methods Used & GitHub Coding Used
- Python
- Juypter Notebooks (Python)
- HTML
- Markdown

## 📦 Packages:
- Pandas as PD
- Matplotlib.pyplot as plt
- Scipy.stat as st
- Numpy as np
- Math
- Statsmodel.stats.weightstats as stm
- Seaborn

## 🖼️ Visuals
The repository includes:
- Aggression ratio distributions  
- Save efficiency distributions  
- Confidence interval plots  
- Galton bell curve overlays  
- Histogram of yellow cards
- Violin distribution plots

## 💡 Key Findings
- High and low aggression groups show overlapping confidence intervals.
- Save efficiency differences are descriptive only, not statistically significant.
- Aggression does **not** predict save efficiency in this sample.

## 📽️ YouTube Video
A full narrated breakdown of the analysis is available on YouTube.  
*(Insert link once uploaded)*

## 📂 Repository Structure
- 

## Author:
![alt text](image.png) 
Danielle Whitney - Student # S407528