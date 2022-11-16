from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

sns.set_theme(style='darkgrid')
df = pd.read_excel('finaldata.xlsx')
print(df)
sns.pairplot(data=df)
sns.lmplot(x='Percent Students', y='Year', data=df)
plt.show()
x = df[['Percent Students']]
x.head()
y = df['Year']
y.head()

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=101)

lm = LinearRegression()
lm.fit(x_train, y_train)
print(lm.coef_)
prediction = lm.predict(x_test)
plt.scatter(y_test, prediction)
plt.show()
print('MAE=', metrics.mean_absolute_error(y_test, prediction))
print('MSE=', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))
plt.hist(prediction-y_test, bins=3)
plt.show()
co = pd.DataFrame(lm.coef_, x.columns)
co.columns = ['coefficient']
print(co)
