import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

d = pd.read_excel('C:\Siri F1 assignments\data science training\Visualization\P12-Churn-Modelling.xlsx')
print(d.columns)
g = sns.FacetGrid(data=d, row='Geography', col='Tenure', hue='Geography')
g = g.map(plt.scatter, 'CreditScore', 'EstimatedSalary')
plt.show()
g = sns.FacetGrid(data=d, row='Geography', col='Tenure', hue='Geography')
kws = dict(linewidth = 0.5, edgecolor = 'black')  #keyword arguements
g = g.map(plt.hist,'EstimatedSalary', **kws)
plt.show()
#controlling axes and adding diagonals
g = sns.FacetGrid(data=d, row='Geography', col='Tenure', hue='Geography')
g = g.map(plt.scatter, 'CreditScore', 'EstimatedSalary')
g.set(xlim=(0,1000),ylim=(0,1000))
for ax in g.axes.flat:
    ax.plot((0,1000),(0,1000),c = 'gray', ls = '--')
g.add_legend()
plt.show()