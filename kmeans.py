import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn import metrics

X = np.random.randint(2000, 2300, 20)
print(X)
plt.scatter(X, len(X) * [1], marker='o')
# my_x_ticks = np.arange(2000, 2500)
# my_y_ticks = np.arange(1)
# plt.xticks(my_x_ticks)
# plt.yticks(my_y_ticks)
plt.show()

x = X.reshape(-1, 1)
print(x)

km_cluster = KMeans(n_clusters=4)
y_pred = km_cluster.fit_predict(x)
print('聚类结果:\n', y_pred)
plt.scatter(x, len(x) * [1], c=y_pred, marker='o')
plt.show()

print(metrics.calinski_harabasz_score(x, y_pred))
