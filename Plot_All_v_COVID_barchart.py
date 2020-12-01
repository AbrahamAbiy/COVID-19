#plot barchart
import matplotlib.ticker as tick
# Set plot parameters
fig, ax = plt.subplots()
width = 0.6 # width of bar
x = np.arange(66)

ax.bar(joined['Date'], joined['ENGLAND, WALES AND ELSEWHERE 1,2'], width = 0.6, color='blue', label = 'Total',align='center')
ax.bar(x + width, joined['COVID-19'], color='red', width = 0.6, label = 'COVID-19',align='center')
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