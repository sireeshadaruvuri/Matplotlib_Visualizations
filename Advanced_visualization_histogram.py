import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

d = pd.read_excel('C:\Siri F1 assignments\data science training\Visualization\P12-Churn-Modelling.xlsx')
print(d.head())
print(d.columns)
f = sns.jointplot(data=d, x='Age', y='CreditScore', kind='hex')
plt.show()
# create a simple histogram
hist = sns.distplot(d.EstimatedSalary)
plt.show()
# histogram in pyplot , seaborn is an upgraded version of pyplot
hist1 = plt.hist(d.EstimatedSalary, bins=20)
plt.show()  # seaborn adds grids n styles to pyplot, without seaborn pyplot visualizations would'nt look good
# stacked histograms
# filter the dataframe with country as Spain
print(d[d.Geography == 'Spain'])
h3 = plt.hist(d[
                  d.Geography == 'Spain'].EstimatedSalary)  # filtering a dataframe with country and then plotting with histragram in pyplot
h4 = plt.hist(d[d.Geography == 'France'].EstimatedSalary)
h5 = plt.hist(d[d.Geography == 'Germany'].EstimatedSalary)
plt.show()
# for stacked histogram(one on top of another instead of overlaping) create a list of h3,h4 and h5
li = plt.hist([d[d.Geography == 'Spain'].EstimatedSalary, d[d.Geography == 'France'].EstimatedSalary,
               d[d.Geography == 'Germany'].EstimatedSalary], bins=10, stacked=True)
plt.show()
# it will be difficult to pass many values to geography manually, istead use loop to make it easy
# first think of how to get the different geography values to pass in the for loop
# it can be done if we declare geography as a category variable
# then we can take all values from that category variable using d.Geography.cat.categories
d.Geography = d.Geography.astype('category')
print(d.info())
print(d.Geography.cat.categories)
list = []
list1 = []  # to create lables
for i in d.Geography.cat.categories:
    list.append(d[d.Geography == i].EstimatedSalary)
    list1.append(i)  # to create labels
print(list)
h = plt.hist(list, stacked=True, label=list1)  # stacked histogram is created
plt.legend()  # to add a legend add labels
plt.show()
# -----------------------
# KDE(Kernel Density Estimation) Plot
# create a scatter plot using seaborn
s = sns.lmplot(data=d, x='EstimatedSalary', y='CreditScore', fit_reg=False, hue='Geography')
plt.show()
# create a KDE plot
s1 = sns.kdeplot(d.CreditScore, d.EstimatedSalary, shade=True, shade_lowest=False, cmap='Blues')
plt.show()
# sub plots
f, ax = plt.subplots(1, 2)
plt.show()
f, axes = plt.subplots(1, 2,figsize = (12,6), sharex=True,sharey=True)
s2 = sns.kdeplot(d.CustomerId, d.EstimatedSalary, ax=axes[0])  # here ax is axes which is array
s3 = sns.kdeplot(d.CustomerId, d.CreditScore, ax=axes[1])
plt.show()
#to set the limit of x axis
#s2.set(xlim=(-20,160))