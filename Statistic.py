#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats #open-source python library used for scientific, mathematical, 

#Employee saliries (in thousands Rs.)

salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#Central Tendency - where is the 'Centre' of the data
mean = np.mean(salaries)
median =np.median(salaries)
mode = stats.mode(salaries,keepdims=True).mode[0]

print(f'Mean (Average):  Rs.{mean:.1f}K')
print(f'Median (Middle Value):  Rs.{median}K')
print(f'Mode (Most common):  Rs.{mode}K')

#Spread - how varied is the data?

std = np.std(salaries)
var = np.var(salaries)
rng = max(salaries)-min(salaries)
q1 = np.percentile(salaries,25)
q3 = np.percentile(salaries,75)
iqr = q3 - q1

print(f'Std Deviation: {std:.2f}K (most important spread measure)')
print(f'IQR: {iqr}K (Q1 ={q1}, Q3={q3})')

#Outlier detection using IQR (Interquartile Range)

lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers = [x for x in salaries if x < lower or x> upper]
print(f'Outliers: {outliers}')


