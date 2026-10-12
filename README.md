<h1>HIT140 Assessment 3 – Foundations of Data Science - Charles Darwin University - October 2026 </h1>

**Group 23:**
- Danielle S407528
- Gabrielle S375255
- Judith S395778
- Manuela S320756

⚽ **Project Overview - FIFA World Cup Analysis** ⚽<br>
This project investigates the FIFA World Cup 2026 statistics.

📌 **Objective 2:**<br>
Your team will perform two related but distinct linear regression tasks as specified below.

**Linear Regression 2.1**<br>
Build and evaluate a linear regression model that predicts the goal difference between two opposing teams in FIFA World Cup 2026 matches. You must compile a dataset that comprises 104 rows, each representing an actual match in the FIFA World Cup 2026. Your dataset must include exactly eight (8) explanatory variables (excluding any ID field). You must thoughtfully decide what these explanatory variables would be and then collect their corresponding data.

<em>Note: All explanatory variables must provide information that is available before a match. 
For example, the number of shots on target made during a match cannot be used as an explanatory variable for predicting the goal difference of that match.</em>


**Linear Regression 2.2**<br>
Build and evaluate a second linear regression model that predicts the number of goals scored by a team in a single FIFA World Cup 2026 match. 
You must compile a dataset that comprises 208 rows, each representing a team's statistics for a specific match. Your dataset must include exactly eight (8) explanatory variables (excluding any ID field). 
You must thoughtfully decide what these explanatory variables would be and then collect their corresponding data.<br>


<em>Note: All explanatory variables must provide information that is available before a match.  
For example, the number of shots on target made by a team during a match cannot be used as an explanatory variable for predicting their goal for that match.</em><br>


**Only a maximum of 4 explanatory variables can be shared between Linear Regression 2.1 and Linear Regression 2.2**

**Load data**
- matches_data = pd.read_csv('matchesk.csv')
- external_data = pd.read_csv('external_factors.csv')
- teams_data = pd.read_csv('teamsk.csv')
- venues_data = pd.read_csv('venuesk.csv')
- full_data = pd.read_csv('full.csv')


**Source:**
- FIFA Official Website: `https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics`
- FB Ref: `https://fbref.com/en/`
- Kaggle: `https://www.kaggle.com/datasets`

<h2>2.1 Linear Regression</h2>

**Stage 1: Conceptual Domains Identification**  
Goal difference is determined by the interplay of three domains: (a) *team capability* (inherent strength and attacking prowess), (b) *match conditions* (venue and officiating characteristics), and (c) *contextual factors* (travel fatigue and psychological state). This framework ensured comprehensive coverage of mechanisms influencing match outcomes.

**Stage 2: Pre-Match Data Constraint**  
The specification "pre-match data only" eliminates post-match statistics (shots, corners, possession during play) and retroactively calculated metrics. This constraint is critical for genuine predictive utility models must rely on information available *before* kickoff, not observed during play.

**Stage 3: Variable Operationalisation**

| Domain | Variable | Justification | Source |
|--------|----------|---------------|--------|
| **Team Capability** | home_Possession (%) | Ball possession reflects team's intended tactical approach and control in play; aggregate FIFA data proxies expected possession tendency | FIFA tournament statistics |
| | away_Possession (%) | Symmetric away team measure; possession asymmetry (home - away) indicates control differential | FIFA tournament statistics |
| | home_xG | Expected Goals quantifies shot quality and finishing threat independent of actual conversion; pre-match xG based on team historical efficiency | Match external factors |
| | away_xG | Away team expected goals; provides balanced assessment of offensive threat | Match external factors |
| **Match Conditions** | betting_odds_home | Market-implied probability of home win incorporates collective expert judgment; odds compress multiple unobserved variables into single summary statistic | Pre-match betting market |
| | referee_strictness | Officiating bias influences goal-scoring opportunities through penalty-giving propensity and tackling tolerance; strictness rating derived from historical yellow/red card distribution | Referee profile dataset |
| **Contextual Factors** | travel_distance_km | Away team travel distance quantifies jet lag, sleep disruption, and recovery difficulty; non-linear fatigue effects expected | Match venue data |
| | social_sentiment_home | Team social media sentiment proxies psychological readiness, confidence, and squad morale pre-match; aggregate measure filters match-day noise | Social media analytics |