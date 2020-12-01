##T-test
#specify data to use
data1 = joined.iloc[:, [3]]
data2 = data1.iloc[56:,:]
data3 = data1.iloc[:55,:]
#t-test
import scipy.stats as stats
t_stat, p_val = stats.ttest_ind(data2, data3, equal_var=False)
print(t_stat)
print(p_val)