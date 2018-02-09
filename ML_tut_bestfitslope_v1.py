from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

xs = np.array([1,2,3,2,1], dtype=np.float64)
ys = np.array([1,2,3,4,2], dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
	m = (((mean(xs) * mean(ys)) - mean(xs*ys)) / 
	((mean(xs)*mean(xs)) - mean(xs*xs)))
	
	# b = y - mx
	b = mean(ys) - m*mean(xs)
	return m, b

m, b = best_fit_slope_and_intercept(xs,ys)

regression_line = [(m*x)+b for x in xs]

plt.scatter(xs,ys)
plt.plot(xs, regression_line)
plt.show()