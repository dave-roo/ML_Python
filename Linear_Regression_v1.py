import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# csv file
df = pd.read_csv('data.csv', delim_whitespace=True)

print df.head()

