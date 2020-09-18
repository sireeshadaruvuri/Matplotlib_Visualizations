import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
d = pd.read_excel('C:\Siri F1 assignments\data science training\Visualization\P4-Section6-Homework-Dataset-1.xlsx')
print(d.head())
print(d.info())
print(d.columns)
sns.set_style('darkgrid')
print(d.Genre.unique())#to get values of Genre column
print(len(d.Genre.unique()))
print(d.Studio.unique())
#gen = d[(d.Genre == 'action'),(d.Genre == 'adventure'),(d.Genre == 'animation'),(d.Genre == 'comedy')]
#instead of filtering with so much code create a filter n call it
f1 = ['action','adventure','animation','comedy']
f2 = d[d.Genre.isin(f1)]
print(f2.Genre.unique())
studio_filters = ['Buena Vista Studios','Fox','Paramount Pictures','Sony','Universal','WB']
f3 = f2[f2.Studio.isin(studio_filters)]
print(f3.Studio.unique())
s = sns.boxplot(data=f3,x='Genre',y='Gross % US')
s2 = sns.stripplot(x = 'Genre',y = 'Gross % US',hue = 'Studio',data = f3, jitter = True)
#s1 = sns.scatterplot(data=f2,x='Genre',y='Gross % US')
plt.title('Domestic gross % by genre')
s.legend()
plt.show()