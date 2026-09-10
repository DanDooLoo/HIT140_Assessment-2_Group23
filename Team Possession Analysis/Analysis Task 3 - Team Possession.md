## Question for Analysis
Do high possession and low possession teams show significant difference in team composition in the FIFA26 World Cup?

## Data Preperation and Sampling
To begin a master list of all matches was extracted from the FBRef website and saved to `fbref_match_list.csv`.

Possession values were entered manually into fields `"Home Possession"` and `"Away Possession"`.

It was decided that sampled groups would be selected based on possession proportion data, to check for groups that had viable sample sizes to produce reliable inferential statistical data the `sample_size_check.py` script was used.

We sampled for two groups; teams that held ≥ 0.65 or ≤ 0.35 possession proportions, they held 33 and 32 in sample size respectively.

Using the script `possession_match_sampler.py` the samples were extracted from the master list and written to their own CSVs; `high_possession_sample.csv` and `low_possession_sample.csv`.

The high and low possession sample lists were compared to one another using `check_missing_counterpart.py` since the similar sample sizes implied that the entries in each list were **counterparts** to each other.

At this stage, all matches were assigned a match ID using `match_list_assign_id.py` to the match master list, which was at this stage called `fbref_match_possession_shots_cleaned_names.csv`.

The script found matches in `high_possession_sample.csv` that didn't appear in `low_possession_sample.csv`, this made manual saving of team data from the FBRef website easier since I could safely take both teams from a sampled match without having to go into the same match twice when going through both high and low samples.

Team CSV files had the naming convention `match_{matchID}_{teamtype}.csv`, `match_004_away.csv` for example. This was to help relate it back to the master list, which held possession data, since there was no identifying data inside the files.

## Data Wrangling
With the help of Copilot `wrangle_teamprop.py` so that we can extract data from the 65 sample CSVs and assign them to their correct possession data entry on the master list, this was done by using the files naming convention described earlier with the Glob library.

Team proportion was calculated within the same script. Where more specific roles were assigned to their broader role of either defenders, midfielders and forwards. Team composition was calculated based on proportion of these three roles in the team, for this reason goal keepers were excluded.

It had to be that every player could only contribute 1 role to the team, no more and no less. If a player had a dual role of DF/MF they contributed 0.5 to DF and 0.5 to MF, or if they had 3 roles they contributed 0.33 etc. So a players role contribution was 1/ number of roles played to each role played.

Sometimes there were more than 10 outfield players on a team due to subs. The whole team composition was calculated by taking all proportions of roles and dividing by the amount of outfield players. This new data frame was saved to `team_composition.csv`.

Using `check_proportions.py` we doubled checked whether all team proportions (DFs, MFs and FWs) added to one to make sure all calculations were correct, and checked a few against the FBREF website manually.

The team possession stats was later added creating a new file called `composition_and_possession.csv` this is the file that forms the basis of all future calculations and analysis.