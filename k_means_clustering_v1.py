import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import Kmeans

# csv file
df = pd.read_csv('data.csv', delim_whitespace=True)

print df.head()

k = 2
kmeans = KMeans(n_cluster=k)
kmeans = kmeans.fit(df)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

#Test

x_test = [[12,32],[45,43],[34,77],[23,45],[54,21],[77,66],[32,3],[6,43]]

prediction = kmeans.predict(x_test)

print prediction

colors = ['blue','red','green','black']
y = 0
for x in labels:
	plt.scatter(df.iloc[y,0], df.iloc[y,1],color=colors[x])
	y+=1
	
for x in range(k):
	lines = plt.plot(centroids[x,0],centroids[x,1],'kx')
	plt.setp(lines,ms=15.0)
	plt.setp(lines,mew=2.0)
	
title = ('No of clusters (k) = {}').format(k)
plt.title(title)
plt.xlabel('eruptions (mins)')
plt.ylabel('waiting (mins)')
plt.show()