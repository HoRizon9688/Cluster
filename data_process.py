import os

import numpy as np
import xlrd
import re

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics

city = os.listdir("./2018")
avg_price = []
for i in range(len(city)):
    workbook_name = "./2018/" + city[i]
    # print(workbook_name)
    workbook = xlrd.open_workbook(workbook_name)
    sheet = workbook.sheet_by_index(0)
    cols = sheet.col_values(1)

    find_price = re.compile(r'\d*')
    price_list = []

    for j in cols:
        price = find_price.findall(j)
        price_list.append(int(price[0]))

    avg = sum(price_list) / len(price_list)
    avg_price.append(int("{:.0f}".format(avg)))
print(avg_price)

np_array = np.array(avg_price)
plt.scatter(np_array, len(np_array) * [1], marker='o')
plt.show()

np_array = np_array.reshape(-1, 1)
km_cluster = KMeans(n_clusters=5)
y_pred = km_cluster.fit_predict(np_array)
print('聚类结果:\n', y_pred)
plt.scatter(np_array, len(np_array) * [1], c=y_pred, marker='o')
plt.show()

print(metrics.calinski_harabasz_score(np_array, y_pred))
