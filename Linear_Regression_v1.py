# in progress v1.1

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# csv file
df = pd.read_csv('data.csv', delim_whitespace=True)

print df.head()

x_train = df['Father'].values[:,np.newaxis]
y_train = df['Sons'].values

lm = LinearRegression()

lm.fit(x_train, y_train)

x_test = [[12],[32],[43],[55],[12],[23]]

predictions = lm.predict(x_test)
print predictions

plt.scatter(x_train, y_train, color='r')
plt.plot(x_test, prediction,color='b',linewidth=3)
plt.xlabel('Father height in inches')
plt.ylabel('Son height in inches')
plt.show()