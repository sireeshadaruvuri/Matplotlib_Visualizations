import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')
#import os
#print(os.getcwd())
p = pd.read_excel('C:\Siri F1 assignments\SEC 6050\week3\Week3_data visualization.xlsx')
print(p.head())
print(p.info())
print(p.describe())
print(p.columns)
p.columns = ('Year','State','AverageMax','AverageMin','Season','AverageHumidityIn','AverageUVIndex')
print(p.columns)
print(p.info())
print(p.describe())
#convert variables into categorical variables so that year will be considered as year instead of integer
#p.Year.astype('category') #this will just return the result won't change the column
#override it to change the column
p.Year = p.Year.astype('category')
print(p.info()) #year is a categorical variable now
p.AverageMax = p.AverageMax.astype('category')
p.AverageMin = p.AverageMin.astype('category')
p.AverageHumidityIn = p.AverageHumidityIn.astype('category')
p.AverageUVIndex = p.AverageUVIndex.astype('category')
print(p.info())
print(p.describe())
print(p.AverageMax.cat.categories) #to see values in the category

#-------------------------------
#Joint plot
d = sns.jointplot(data = p, x = 'State',y = 'AverageMax')
plt.show()
#use kind to change the shape of jointplot
d = sns.jointplot(data=p,x ='State',y = 'AverageMax',kind='hex' )