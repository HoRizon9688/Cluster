import numpy as np
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from sklearn.metrics import calinski_harabasz_score
from tslearn.clustering import KShape


def plot_clustering(df, area_name, cluster):
    cluster_id = cluster.tolist()
    price_list = []
    cluster_center = []
    for i in cluster_id:
        temp = df['price'][i * 48:i * 48 + 48]
        price_list.append(temp.tolist())
    for i in range(48):
        value = 0
        for j in price_list:
            value += j[i]
        cluster_center.append(value / len(price_list))
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(1, 48, 48)
    for j in range(len(price_list)):
        name = area_name[str(cluster_id[j] + 1)]
        ax.plot(x, price_list[j], label=name)
    ax.plot(x, cluster_center, label='聚类中心', linestyle='--', color='black')
    ax.legend(bbox_to_anchor=(1.12, 1), loc='upper right')
    plt.show()


df = pd.read_csv('mini_features.csv')
df2 = pd.read_csv('merge_data.csv')

area_name = {'1': '渝北', '2': '江北', '3': '沙坪坝', '4': '南岸', '5': '九龙坡', '6': '渝中', '7': '巴南', '8': '大渡口', '9': '北碚',
           '10': '万州', '11': '璧山', '12': '合川', '13': '永川', '14': '江津', '15': '涪陵', '16': '铜梁', '17': '长寿', '18': '潼南',
           '19': '荣昌', '20': '开州', '21': '大足', '22': '南川', '23': '垫江', '24': '綦江', '25': '梁平', '26': '丰都', '27': '武隆',
           '28': '奉节', '29': '云阳', '30': '石柱', '31': '秀山', '32': '忠县', '33': '彭水', '34': '黔江', '35': '巫山', '36': '酉阳',
           '37': '巫溪'}

k = 20

sc_score_list = []  # 轮廓系数
ch_score_list = []  # CH系数
inertia_list = []

for i in range(2, k):
    km_cluster = KMedoids(n_clusters=i, random_state=0)
    y_pred = km_cluster.fit_predict(df)
    sc_score = silhouette_score(df, y_pred)
    sc_score_list.append(sc_score)
    ch_score = calinski_harabasz_score(df, y_pred)
    ch_score_list.append(ch_score)
    inertia_list.append(km_cluster.inertia_)


plt.plot(list(range(2, k)), ch_score_list)
plt.xticks(range(0, k, 1))
plt.grid(linestyle='--')
plt.xlabel("Number of Clusters Initialized")
plt.ylabel("Calinski Harabasz score")
plt.show()

plt.plot(list(range(2, k)), sc_score_list)
plt.xticks(range(0, k, 1))
plt.grid(linestyle='--')
plt.xlabel("Number of Clusters Initialized")
plt.ylabel("Silhouette score")
plt.show()

plt.plot(list(range(2, k)), inertia_list)
plt.xticks(range(0, k, 1))
plt.grid(linestyle='--')
plt.xlabel("Number of Clusters Initialized")
plt.ylabel("Inertia")
plt.show()

best_k = 4
# best_k = sc_score_list.index(max(sc_score_list)) + 2
print("最优k值：{}".format(best_k))

best_km = KMedoids(n_clusters=best_k, random_state=0)
y_pred = best_km.fit_predict(df)
# print(y_pred)

for j in range(best_k):
    cluster = np.where(y_pred == j)[0]
    plot_clustering(df2, area_name, cluster)
    id_list = np.array([1] * cluster.size) + cluster
    name_list = []
    for city_id in id_list:
        city_name = area_name[str(city_id)]
        name_list.append(city_name)
    print("cluster {}: {}".format(j + 1, name_list), end='   ')
    print("共{}个城市".format(cluster.size))
