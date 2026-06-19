# #
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats #open-source python library used for scientific, mathematical, 

# #Employee saliries (in thousands Rs.)

# salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

# #Central Tendency - where is the 'Centre' of the data
# mean = np.mean(salaries)
# median =np.median(salaries)
# mode = stats.mode(salaries,keepdims=True).mode[0]

# print(f'Mean (Average):  Rs.{mean:.1f}K')
# print(f'Median (Middle Value):  Rs.{median}K')
# print(f'Mode (Most common):  Rs.{mode}K')

# #Spread - how varied is the data?

# std = np.std(salaries)
# var = np.var(salaries)
# rng = max(salaries)-min(salaries)
# q1 = np.percentile(salaries,25)
# q3 = np.percentile(salaries,75)
# iqr = q3 - q1

# print(f'Std Deviation: {std:.2f}K (most important spread measure)')
# print(f'IQR: {iqr}K (Q1 ={q1}, Q3={q3})')

# #Outlier detection using IQR (Interquartile Range)

# lower = q1 - 1.5*iqr
# upper = q3 + 1.5*iqr
# outliers = [x for x in salaries if x < lower or x> upper]
# print(f'Outliers: {outliers}')

#
##Correlation For Aiml

# #data
# from scipy import stats #open-source python library used for scientific, mathematical
# import numpy as np 
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# #data
# np.random.seed(42)
# study = np.random.uniform(2,10,60)
# marks = study * np.random.normal(0,10,60)
# marks = np.clip(marks,30,100)
# absent = 10 - study + np.random.normal(0,1,60)

# df = pd.DataFrame({'Study_Hours':study,'Marks':marks,'Absences':absent})

# corr_matrix = df.corr()
# print(corr_matrix.round(3))

# plt.figure(figsize=(6,4))
# sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',vmin=-1,vmax=1,fmt='.2f')
# plt.title('Correlation Matrix'); plt.show()

# #Pearson correlation
# r, p_value = stats.pearsonr(study, marks)
# print(f'Study-Marks correlation: r={r:.3f}, p={p_value:.4f}')
# print('Interpretation:','Strong positive' if r>0.7 else 'Moderate' if r>0.4 else 'Weak')

# #
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm #Normal Distribution calculator

# #You feed it a mean and standard deviation, and it can answer any probabilty question 

# #Normal Destribution - the bell curve
# #Normal distribution with mean 165cm and standard deviation 7cm
# mean_h,std_h = 165,7

# prob = 1 - norm.cdf(175, mean_h,std_h) #Cumulative distribution function , tells how
# print(f'P(height>175cm) = {prob:.4f} = {prob*100:.1f}%')

# #The 68-95-99.7 Rule
# print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
# print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
# print(f'68% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')

# #

# from sklearn.model_selection import train_test_split, cross_val_score
# import numpy as np

# np.random.seed(42)
# X = np.random.randn(500, 5)
# y = np.random.randint(0,2,500)

# # 80/20 Train-Test Split
# X_train,X_test,y_train,y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y
# )
# print(f'Training samples: {len(X_train)} | Test samples: {len(X_test)}')

# # 5-Fold Cross-Validation - more reliable than single split
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=58, random_state=42)
# cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
# print(f'CV Scores each fold: {cv_scores.round(3)}')
# print(f'Mean: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}')

##

# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt

# #Data
# n_A, conv_A = 1000, 52
# n_B, conv_B = 1000, 68
# rate_A = conv_A / n_A
# rate_B = conv_B / n_B

# print(f'Version A conversion rate: {rate_A*100:.1f}%')
# print(f'Version B conversion rate: {rate_B*100:.1f}%')
# print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')

# ##
# table = [ [conv_A,n_A-conv_A],[conv_B, n_B-conv_B]]
# chi2, p_value, dof,expected = stats.chi2_contingency(table)

# print(f'Chi-square: {chi2:.4f}')
# print(f'P-value: {p_value:.4f}')
# print('Result:','SIGNIFICANT -B is better!' if p_value<0.05 else 'NOT significant - could be random')

##LINEAR REGRESSION

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Study hours vs exam marks

study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5]
marks = [25,38,52,68,71,78,85,89,93,96,43,68,82,91]

X = np.array(study).reshape(-1,1) #must be 2D for skylearn
y = np.array(marks)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)  #LEARNING happens here

print(f'Slope:    {model.coef_[0]:.2f} (marks increae per study hour)')
print(f'Intercept:{model.intercept_:.2f} (marks at 0 study hours) ')

y_pred = model.predict(X_test)
print(f'R² Score: {r2_score(y_test,y_pred):.4f} (1.0 = perfect)')
print(f'RMSE:    {mean_squared_error(y_test,y_pred)**0.5:.2f} marks average error')

#Predict new students
new_pred = model.predict([[7]])[0]
print(f'Student studying 7hrs predicted marks: {new_pred:.1f}')

#plot
plt.figure(figsize=(9,5))
plt.scatter(X,y,color='steelblue',s=100,alpha=0.8,label='Actual')
plt.plot(X,model.predict(X),color='red',linewidth=2,label='Predicted line')
plt.xlabel('Study Hours/Day'); plt.ylabel('Exam Marks')
plt.title('Linear Regression - Study Hours vs Marks')
plt.legend(); plt.grid(True,alpha=0.3); plt.show()
