#import dependencies
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import mlab
import numpy as np
import random

#set path
filepath = "../2024/CSV/Neighborhood_zhvi_uc_sfr_sm_sa_month.csv"
house=pd.read_csv(filepath)

#drop columns
house = house.drop(["RegionID", "SizeRank", "StateName", "Metro"], axis=1)

#Find total null values
house.isnull().values.sum()

#Create New Columns for Rate of Change
house1["Rate of Change 10year"]=(house1["2024-05-31"]-house1["2014-05-31"])/house1["2014-05-31"]
house1["Rate of Change 5year"]=(house1["2024-05-31"]-house1["2019-05-31"])/house1["2019-05-31"]
house1["Rate of Change 3year"]=(house1["2024-05-31"]-house1["2021-05-31"])/house1["2021-05-31"]

#Get Top 50 Neighborhoods by 5 Year Rate of Change
top_50 = house1.sort_values(by=['Rate of Change 5year'], ascending=False)

#Plotting all Neighborhoods based on 5 Year Rate of Change
alldf=top_50[['RegionName', 'City', 'State','Rate of Change 5year']].sort_values(by=('Rate of Change 5year'), ascending=False)
alldf['%']=alldf['Rate of Change 5year'].apply(lambda x: x*100)

#Clear Null values
alldf=alldf.dropna()

#Assign x and y axes
x_all=alldf['RegionName']
y_all=alldf['%']

#show basic stats
alldf.describe()

stats=np.percentile((alldf['%']), range(0,125,25))

min=stats[0]
pct25=stats[1]
mean_all=np.mean(y_all)
pct75=stats[3]
max=stats[4]

#Percentiles
tile75 = []
tile50 = []
tile25 = []

for i in y_all:
    if i <= max and i > pct75:
        tile75.append(i)
    if i<= pct75 and i>pct25:
        tile50.append(i)
    if i<= pct25 and i>min:
        tile25.append(i)

tiles=[tile75, tile50, tile25]
for i in tiles:
    print(len(i))


#Scatterplot for all neighborhoods
plt.figure(figsize = (10, 6))  

#Colorcode data points
conditions  = [ (y_all<=max) & (y_all>pct75), (y_all<=pct75) & (y_all>mean_all), (y_all<=mean_all) & (y_all>pct25), (y_all<=pct25) & (y_all>0), y_all<=0 ]
choices     = [ 'green', 'greenyellow', 'yellow', 'orange', 'red' ]
#choices     = [ 5,4,3,2,1 ]
colorall = np.select(conditions, choices, default=np.nan)

#Plot Neighborhoods
plt.scatter( x_all, y_all, marker = 'o', s = 15, c = colorall) 

#Plot Percentile Lines
minl = plt.axhline(y=min)
#plt.text(len(x_all)-10, min, 'MIN', fontsize = 10)

pct25l = plt.axhline(y=pct25)
plt.text(len(x_all), 0, '25th Percentile', fontsize = 10)

meanl = plt.axhline(y=mean_all)
plt.text(len(x_all), mean_all, 'MEAN | 50th Percentile', fontsize = 10)

pct75l = plt.axhline(y=pct75)
#plt.text(len(x_all), pct75, '75th Percentile', fontsize = 10)

maxl = plt.axhline(y=max)
plt.text(len(x_all), 150, '75th Percentile', fontsize = 10)

#Plot labels
plt.xticks([], rotation = 90)
plt.title("All Neighborhoods based on 5 Year Rate of Change")
plt.ylabel("Growth Rate %")
plt.xlabel("Neighborhoods")

plt.tight_layout()
#plt.savefig('../2024/Output Plots/All Neighborhoods 5 year ROC')
plt.show()


#Data frame for top 50
plotdf=alldf.head(50)
plotdf['%']=plotdf['Rate of Change 5year'].apply(lambda x: x*100)

#Assign x and y axes
x_axis=plotdf['RegionName']
y_axis=plotdf['%']

#Find Median
median=y_axis.median()

#Find Mean
mean=y_axis.mean()
mean


#Scatterplot for top 50
plt.figure(figsize = (7, 9))  

#Color code data points
conditions  = [ y_axis >= mean, (y_axis<mean) & (y_axis>median), y_axis <= median ]
choices     = [ 'green', 'orange', 'red' ]
    
color = np.select(conditions, choices, default=np.nan)

#Plot Neighborhoods
plt.scatter( y_axis, x_axis, marker = 'o', s = 15, color = color) 

#Plot Median Line
m1 = plt.axvline(x=np.median(y_axis), ls=':')
plt.text(median-6.5, -2, str(round(median,2)), fontsize = 10)

#Plot Mean Line
#m2 = plt.axvline(x=np.mean(y_axis))
#plt.text(mean, -2, str(round(mean,2)), fontsize = 10)

plt.legend([m1],['Median'],loc = "upper right",fontsize = "medium",fancybox = True)
plt.title("Top 50 Neighborhoods based on 5 Year Rate of Change")
plt.ylabel("Neighborhoods")
plt.yticks(fontfamily='sans-serif', fontsize='x-small')
plt.xlabel("Growth Rate %")

plt.tight_layout()
#plt.savefig('../2024/Output Plots/Top 50 Neighborhoods scatterplot')
plt.show()
