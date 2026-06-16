import matplotlib.pyplot as plt

# months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# sales = [45,52,48,61,58,72,69,75,68,82,90,95]

# # Line Chart = trends over time
# plt.figure(figsize=(12,5))
# plt.plot(months,sales,marker='o', color='steelblue', linewidth=2, markersize = 8)
# plt.fill_between(months,sales,alpha=0.15,color='steelblue')
# plt.title('Monthly Sales 2026 (Rs. Thousand)', fontsize=14, fontweight='bold')
# plt.xlabel('Month')
# plt.grid(True,alpha=0.3)
# plt.tight_layout()
# plt.show()

# #bar chart 
# cities = ['Bhopal','Indore','Jabalpur','Gwalior','Ujjain']
# students = [1200,2800,980,850,650]
# colors = ['#2196F3','#4CAF50','#FF9800','#9C27B0','#F44336']

# #Bar Chart = compare cateories

# plt.figure(figsize=(9,5))
# bars = plt.bar(cities, students,color = colors,edgecolor = 'White',linewidth=1.5)
# plt.title('Students Enrolled per City')
# plt.ylabel('Number od Students')
# for bar,val in zip(bars,students):
#     plt.text(bar.get_x()+bar.get_width()/2,val+30, str(val),ha ='center',fontweight='bold')
# plt.tight_layout()
# plt.show()

##
# import numpy as np 

# study_hrs = np.random.uniform(2,10,50)
# marks = study_hrs * 7 + np.random.normal(0,8,50)
# marks = np.clip(marks,38,100)

# plt.figure(figsize=(8,5))
# plt.scatter(study_hrs,marks,c=marks, cmap='RdYlGn', s=100,
# alpha=0.8)
# plt.colorbar(label='Marks')
# plt.title('Study Hours vs Exam Marks')
# plt.xlabel('Study Hours/Day')
# plt.ylabel('Exam Marks')
# plt.show()

##
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)
#Data

df = pd.DataFrame({
    'marks':      np.random.randint(40,100,100),
    'study_hours':np.random.uniform(2,10,100),
    'city':       np.random.choice(['Bhopal','Indore','Jabalpur'],100),
    'gender':     np.random.choice(['Male','Female'],100)})
#Histogram with KDE - see the distribution

plt.figure(figsize=(10,4))
sns.histplot(df['marks'], bins=20, kde=True, color='steelblue')
plt.title('Distribution of Student Marks')
plt.show()



