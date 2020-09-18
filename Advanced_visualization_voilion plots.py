import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

d = pd.read_excel('C:\Siri F1 assignments\data science training\Visualization\P12-Churn-Modelling.xlsx')
s = sns.violinplot(data=d, x = 'Geography', y = 'EstimatedSalary')
plt.show()
s1 = sns.boxplot(data = d, x = 'Geography', y = 'EstimatedSalary')
plt.show()