## Explanatory Variable Derivation & Theory Justification

### 1. Introduction & Research Objective

The objective of this analysis is to develop a linear regression model predicting goal difference (home goals minus away goals) in FIFA World Cup 2026 matches using exclusively pre-match explanatory variables. The constraint of EXACTLY 8 variables required thoughtful selection, balancing predictive power, theoretical relevance, and practical availability. This report explains the rationale behind each variable selection and interprets the resulting model performance.

### 2. Explanatory Variable Selection Framework

The eight variables were derived through a three-stage selection framework. Stage 1: Conceptual Domains Identification. Stage 2: Pre-Match Data Constraint, and Stage 3: Variable Operationalisation, please refer to Table 1 for the explanatory variables used by Group 23. 
The FIFA World Cup 2026 consisted of 104 matches that resulted with Spain being the ultimate champions of the competition. The aim of the first task was to use linear regression to analyse and predict the goal difference between the two finalist opposing teams, Spain and Argentina. The second task was to predict the number of goals for one team for that same match. Group 23 have compared the results with the true results using Python programming to perform the linear regression. Our groups challenge was to research 8 viable and unique explanatory variables (x) for each task, Objective 2.1 and 2.2, and evaluate the results to achieve a calculation for the response variable (y). 

Nevertheless, our task was to be creative and make several comparisons using a test/train model, comparing the results against a baseline model. Our variables were chosen independently, compared, and evaluated using a multiple linear regression model using Python programming software. Our data files were saved as csv files using Microsoft Excel,  readable by VS Code, using several  packages called pandas, which is designed for reading csv files. Other packages were also  used to perform the linear regression. These include math, numpy, and sklearn plus several other sub-packages. Data visualisation was also performed using  matplotlib.pyplot, which were used to create scatterplots and Seaborn to create heatmaps. 

However, data visualisation is important as it provides a brief visual overview of the datasets which helps to identify problems and successes quite clearly if the data is accurate and appropriately selected. For instance, scatterplots are useful in determining if the data shows uniformity and if there any outliers. This is useful when an organisation is testing and looking to make improvements. Heatmaps also provide useful information by performing correlations of the data. If any of the  variables  are too similar, then a variable can be dropped, as removing unnecessary  information that is already presented using a similar variable can be quite helpful when working on data visualisation. Further research is then needed to replace the variable with another, or simply removed, depending on the results of the MAE, MSE, RMSE, RMSE normalised, and R². Group 23 tested our datasets against the error values and compared them with a baseline at different stages to test this hypothesis. Our findings are listed below.

### Formula for Linear Regression

y=b_{0}{+b}_{1}x_{1}{+b}_{2}x_{2}…

Nevertheless, in Objective 2.1, our datasets comprised of 104 rows matching the 104 matches played during the FIFA Worl Cup 2026. In Objective 2.2, the datasets represented each team and their goals which consisted of 208 rows. Our groups challenge was to select a maximum of eight explanatory variables (x) for each objective that would be the most relevant in determining the solution for the response variable (y). These are provided in Table 1 listed below. 

Table 1: Explanatory Variables (x), Dependant Variable(y) Selected by Group 23 

Tasks	Manuela Crannis – s320756. Data collected from Stats Don’t Lie website
	Judith Dawson	Gabby Davis 	Danielle Whitney s

Obj.  2.1	x = Score First Half Team 1
x = Score First Half Team 2 
x = Possession Team 1
x = Possession Team 2 
x = Attempts at Goal Team 1
x = Attempts at Goal Team 2
x = Goals Conceded Team 1
x =  Goals Conceded Team 2
y = Pred. Goal Diff.	x =Home Possession
x = Away Possession
x =Home xG
x =Away xG
x =Home Betting Odds
x =Referee Strictness
x =Home Team Travel distance
x =Home Social sentiment
y = Pred. Goal Diff.	x =
x =
x =
x =
x =
x =
x =
x =
y = Pred. Goal Diff.


	x =Home possession
x = Away Possession
x = Home xG
x = Away xG
x =Betting odds home
x = referee strictness
x = travel distance (km)
x = social sentiment (home)
y = Pred. Goal Diff.
Obj. 2.2	x =Team_1or2
x =Team_Score
x =Possession
x =Attempts_at_Goal
x =Goals_Conceded
x =Shots_Target
x = Free_Kicks
x =Red_Cards 
y = xG_(Predicted No. of Goals	x =
x =
x =
x =
x =
x =
x =
x =
9. Predicted No. of Goals	x =
x =
x =
x =
x =
x =
x =
x =
y =Predicted No. of Goals	x =
x =
x =
x =
x =
x =
x =
x =
y = Predicted no. of Goals

Table 2 : Results of the Test/Train Models 2.1 by Danielle Whitney and Manuela Crannis

Test Size (DW)	70% Training	80% Training	90% Training		Test Size (MC)	70% Training	80% Training	90% Training
	 	 	 			 	 	 
	30% Test	20% Test	10% Test			30% Test	20% Test	10% Test
Intercept	0.4444	0.494	0.5054		Intercept	-0.1074	-0.1186	-0.1273
MAE (MLP)	1.4226	1.4518	1.34		MAE (MLP)	1.4307	1.4494	1.4741
MSE (MLP)	3.604	3.4809	2.3431		MSE (MLP)	3.178	3.1061	3.0259
RMSE (MLP)	1.8984	1.8657	1.5307		RMSE (MLP)	1.7827	1.7624	1.7395
R2	0.2406	0.3048	0.4864		RMSE_Norm (MLP)	0.936	0.9283	0.9034
CV_R2	0.2478	0.2478	0.2478		RÂ² (MLP)	0.1202	0.1328	0.1735
Intercept	0.4444	0.494	0.5054		 	 	 
MAE (Baseline)	1.4002	1.4246	1.3508		MAE (Baseline)	1.578	1.5941	1.6657
MSE (Baseline)	3.279	3.1512	2.4343		MSE (Baseline)	3.6384	3.5866	3.6695
RMSE (Baseline)	1.8108	1.7752	1.5602		RMSE (Baseline)	1.9075	1.8938	1.9156
RMSE_Norm (Baseline)	0.3091	0.3706	0.4664		RMSE_Norm (Baseline)	1.0015	0.9975	0.9949
RÂ² (Baseline)	0.3238	0.3238	0.3238		RÂ² (Baseline)	-0.0073	-0.0013	-0.0023


Final Linear Regression - Calculating the co-efficient of the variables were used to calculate y variable by Danielle Whitney.
I have run optimization on the data I used and have updated the values below. The best performing split for me was the 90/10 split. 
Final Linear Regression - Calculating the co-efficient of the variables were used to calculate y variable by Manuela Crannis.
GD(y)= -1.15 - (T1S) -1.0146 - (T2S) -2.376 + (SFHT1) 0.7201 + (SFHT2)  0.3479 - (PT1)  -0.0116 + (PT2)  0.0167 + (AaGT1)  0.0291 - (AaGT2)  -0.0335 + (GCT1)  0.4672 + (GCT2)  1.1226. The linear regression performed better than the baseline for this question.
Table 3 : Results of the Test/Train Models 2.1 by Gabby Davis and Judith Dawson
Test Size	70% Training	80% Training	90% Training		Test Size	70% Training	80% Training	90% Training
	 	 	 			 	 	 
	30% Test	20% Test	10% Test			30% Test	20% Test	10% Test
Intercept					Intercept			
MAE (MLP)					MAE (MLP)			
MSE (MLP)					MSE (MLP)			
RMSE (MLP)					RMSE (MLP)			
RMSE_Norm (MLP)					RMSE_Norm (MLP)			
RÂ² (MLP)					RÂ² (MLP)			
 					 		
MAE (Baseline)					MAE (Baseline)			
MSE (Baseline)					MSE (Baseline)			
RMSE (Baseline)					RMSE (Baseline)			
RMSE_Norm (Baseline)					RMSE_Norm (Baseline)			
RÂ² (Baseline)					RÂ² (Baseline)			

Final Linear Regression - Calculating the co-efficient of the variables were used to calculate y variable by Gabby Davis.

Final Linear Regression - Calculating the co-efficient of the variables were used to calculate y variable by Judith Dawson.

Figure 1: Objective 2.1-Results Obtained  using Heat Maps and Scatterplots by Manuela Crannis
  
2.2 Linear Regression: 

Test Size (MC)	70% Training	80% Training	90% Training
	 	 	 
	30% Test	20% Test	10% Test
Intercept			
MAE (MLP)			
MSE (MLP)			
RMSE (MLP)			
RMSE_Norm (MLP)			
RÂ² (MLP)			
 			
MAE (Baseline)			
MSE (Baseline)			
RMSE (Baseline)			
RMSE_Norm (Baseline)			
RÂ² (Baseline)			
			
Figure 2: Objective 2.2-Results using Heat Maps and Scatterplots by Manuela Crannis

All charts done on this page are by Judith Dawson

7. Conclusions & Interpretive Synthesis

Key Findings:
	Variable Selection was Well-Motivated: The 8-variable specification balances conceptual coverage (team capability, match conditions, contextual factors) with parsimony appropriate for n=104. Each variable addresses a theoretically distinct mechanism influencing goal difference.
	Group 23  used a training / test model of 70%, 80%, 90% to test our models to determine if the explanatory variables we selected were appropriate for this task. We also calculated the mean absolute error, mean squared error, root mean square error, and normalised root mean square error and compared them with a baseline.
	For further clarification our group also compared our results with the actual result of the grand final match between Argentina and Spain versus the predicted result for both Linear Regression Models 2.1 and 2.2. Our results can be viewed using the link provided to our repository in GitHub, Group 23 – Assessment 3 – Objective 2. 

