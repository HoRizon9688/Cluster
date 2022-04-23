import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples

df = pd.read_csv('mini_features.csv')

area_name = {'1': '渝北', '2': '江北', '3': '沙坪坝', '4': '南岸', '5': '九龙坡', '6': '渝中', '7': '巴南', '8': '大渡口', '9': '北碚',
           '10': '万州', '11': '璧山', '12': '合川', '13': '永川', '14': '江津', '15': '涪陵', '16': '铜梁', '17': '长寿', '18': '潼南',
           '19': '荣昌', '20': '开州', '21': '大足', '22': '南川', '23': '垫江', '24': '綦江', '25': '梁平', '26': '丰都', '27': '武隆',
           '28': '奉节', '29': '云阳', '30': '石柱', '31': '秀山', '32': '忠县', '33': '彭水', '34': '黔江', '35': '巫山', '36': '酉阳',
           '37': '巫溪'}

k = 11

score_list = []
for i in range(2, k):
    km_cluster = KMeans(n_clusters=i)
    y_pred = km_cluster.fit_predict(df)
    score = silhouette_score(df, y_pred)
    score_list.append(score)

plt.plot(list(range(2, k)), score_list)
plt.xticks(range(0, k, 1))
plt.grid(linestyle='--')
plt.xlabel("Number of Clusters Initialized")
plt.ylabel("Silhouette score")
plt.show()

best_k = score_list.index(max(score_list)) + 2
print("最优k值：{}".format(best_k))

best_km = KMeans(n_clusters=best_k)
y_pred = best_km.fit_predict(df)
# print(y_pred)

for j in range(best_k):
    cluster = np.where(y_pred == j)[0]
    id_list = np.array([1] * cluster.size) + cluster
    name_list = []
    for city_id in id_list:
        city_name = area_name[str(city_id)]
        name_list.append(city_name)
    print("cluster {}: {}".format(j + 1, name_list), end='   ')
    print("共{}个城市".format(cluster.size))