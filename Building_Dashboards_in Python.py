import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
d = pd.read_excel('C:\Siri F1 assignments\data science training\Visualization\P12-Churn-Modelling.xlsx')
sns.set_style('darkgrid')
f, axes = plt.subplots(2,2)
s2 = sns.kdeplot(d.CustomerId, d.EstimatedSalary, ax=axes[0,0],figsize = (15,15))  # here ax is axes which is array
s3 = sns.kdeplot(d.CustomerId, d.CreditScore, ax=axes[0,1])
s2.set(ylim = (0,150000))
s4 = sns.violinplot(data=d, x = 'Geography', y = 'EstimatedSalary', ax = axes[1,0])
#s5 = sns.boxplot(data = d, x = 'Geography', y = 'EstimatedSalary', ax = axes[1,1])

#how to add a non seaborn plot
#hist1 = plt.hist(d.EstimatedSalary, bins=20, ax = axes[1,1]) #if we add like this it gives an error
axes[1,1].hist(d.EstimatedSalary, bins=20) #this is the standard approach of doing for pyplot
plt.show()
#styling for dashboards
sns.set_style('dark',{'axes.facecolor':'black'})
f, axes = plt.subplots(2,2)
s2 = sns.kdeplot(d.CustomerId, d.EstimatedSalary,shade = True, shade_lowest=True,cmap = 'inferno',
                 ax=axes[0,0],figsize = (10,10))# here ax is axes which is array
s2n = sns.kdeplot(d.CustomerId, d.EstimatedSalary,cmap = 'cool',
                 ax=axes[0,0],figsize = (10,10))
s3 = sns.kdeplot(d.CustomerId, d.CreditScore, ax=axes[0,1],shade = True, shade_lowest=True,cmap = 'inferno')
s3n = sns.kdeplot(d.CustomerId, d.CreditScore, ax=axes[0,1],cmap = 'cool')
s2.set(ylim = (0,200000))
#to change remaining two grids to black change sns.setstyle above
#palette will be used for color in voilin plot
s4 = sns.violinplot(data=d, x = 'Geography', y = 'EstimatedSalary',palette = 'YlOrRdh;',ax = axes[1,0])
#for kde plot outerline contouring
axes[1,1].hist(d.EstimatedSalary, bins=20)
plt.show()