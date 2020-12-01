##PLOT FLU v COVID

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read data
df = pd.read_excel('2.xlsx','Table 3', header=[4])
#specify dataframe
df = df.iloc[0:244,[0,2,3]]
print(df)
print(df.shape)
df = df.sort_index()
import matplotlib.ticker as tick

#plot line graphs
plt.plot(df['Date of death'], df['Flu'], color='blue', label = 'Flu')
plt.plot(df['Date of death'], df['COVID-19'], color='red', label = 'COVID-19')
plt.xticks(np.arange(1,250,30))
plt.title('Flu and COVID-19 daily deaths 2020', fontsize=14)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Deaths', fontsize=14)
plt.legend(loc="upper left")

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='medium'  
)
