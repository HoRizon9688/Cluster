import matplotlib.pyplot as plt
import xlrd
import pandas as pd
import numpy as np

cluster_id = [0, 1, 5, 8]
df = pd.read_csv('merge_data.csv')

price_list = []
for i in cluster_id:
    temp = df['price'][i * 48:i * 48 + 48]
    price_list.append(temp.tolist())

# print(price_list)

fig, ax = plt.subplots()
x = np.linspace(1, 48, 48)
for j in price_list:
    ax.plot(x, j)
ax.legend()
plt.show()

# 还需要添加图例 legend
