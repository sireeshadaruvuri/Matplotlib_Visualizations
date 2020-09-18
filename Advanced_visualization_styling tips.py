import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
d = pd.read_excel('C:\Siri F1 assignments\data science training\Visualization\P12-Churn-Modelling.xlsx')
d.Geography = d.Geography.astype('category')
print(d.info())
print(d.Geography.cat.categories)
list = []
list1 = []  # to create lables
for i in d.Geography.cat.categories:
    list.append(d[d.Geography == i].EstimatedSalary)
    list1.append(i)  # to create labels
print(list)
sns.set_style('whitegrid')
fig, ax = plt.subplots() # create one subplot and then keep histogram in it so that it would be easy to increase the size
fig.set_size_inches(11.7, 8.27)
plt.title('churn modelling',fontsize = 25,color = 'darkblue',fontname = 'calibri')
plt.ylabel('EstimatedSalary',fontsize = 20,color = 'green',fontname = 'calibri')
plt.xlabel('Geography',fontsize = 20, color = 'blue',fontname = 'calibri')
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
h = plt.hist(list, stacked=True, label=list1)  # stacked histogram is created
plt.legend(frameon = True, fancybox = True, shadow = True, framealpha = 1,prop = {'size':20})  # to add a legend add labels and increase the size of legend
plt.show()
