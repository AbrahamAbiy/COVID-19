##TimeSeriesAnalysis
import pandas as pd
#read data
df2 = pd.read_excel('2.xlsx','Table 3', header=[4])
df2 = df2.iloc[0:244,[0,3]]

#specify array and convert datatype
import matplotlib.pyplot as plt
ac = df2.iloc[:,1]
ac = ac.astype(float)

#plot acf
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(residuals)

#plot pacf
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(residuals)

#fit ARIMA model
from statsmodels.tsa.arima_model import ARIMA

order = (1, 1, 1)
model = ARIMA(ac, order)
fit = model.fit()
fit.summary()

#plot residuals
residuals = pd.DataFrame(fit.resid, columns=['residuals'])
residuals.plot(kind='kde')

#plot forecast
preds = fit.predict(244, 300, typ='levels')
preds.astype(int)
plt.plot(preds)
plt.title('Forecast')
ARIMA.forecast(fit)

