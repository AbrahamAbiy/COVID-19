##PLOT ALL v COVID deaths

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read data
df = pd.read_excel('2.xlsx','Table 3', header=[4])
df = df.iloc[0:244,[0,2,3]]
print(df)
print(df.shape)
#df = df.sort_index()

#change date names so it can match format in total deaths dataset
df['Date of death'] = df['Date of death'].str.replace(r'(^.*January.*$)', 'Jan-203')
df['Date of death'] = df['Date of death'].str.replace(r'(^.*February.*$)', 'Feb-203')
df['Date of death'] = df['Date of death'].str.replace(r'(^.*March.*$)', 'Mar-203 ')
df['Date of death'] = df['Date of death'].str.replace(r'(^.*April.*$)', 'Apr-203')
df['Date of death'] = df['Date of death'].str.replace(r'(^.*May.*$)', 'May-203')
df['Date of death'] = df['Date of death'].str.replace(r'(^.*June.*$)', 'Jun-203')
df['Date of death'] = df['Date of death'].str.replace(r'(^.*July.*$)', 'Jul-203')
df['Date of death'] = df['Date of death'].str.replace(r'(^.*August.*$)', 'Aug-203')
print(df)
#df.columns['Date of death', 'Flu', 'COVID-19']

#sum up deaths in same month
df1 = df.groupby(['Date of death'])['COVID-19'].sum().reset_index()
print(df1)
#df.to_csv('2017M.csv')

#read total deaths dataset
df2 = pd.read_csv('2015-2019.csv', header = 0)
df2 = df2.iloc[0:66,[0,1]]
df2 = df2
print(df2)

#merge datasets by date
joined = pd.merge(df1, df2, how='right', left_on='Date of death', right_on='Date')
print(joined)


#plot linegraph
import matplotlib.ticker as tick
plt.plot(joined['Date'], joined['ENGLAND, WALES AND ELSEWHERE 1,2'], color='blue', label = 'Total')
plt.plot(joined['Date'], joined['COVID-19'], color='red', label = 'COVID-19')
plt.xticks(np.arange(1,65,5))
plt.title('Total and COVID-19 monthly deaths 2020', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Deaths', fontsize=14)
plt.legend(loc="upper left")

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='medium'  
)
