import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tslearn.clustering import TimeSeriesKMeans
from tslearn.datasets import CachedDatasets
from tslearn.preprocessing import TimeSeriesScalerMeanVariance, TimeSeriesResampler
from tslearn.utils import to_time_series_dataset
from tslearn.clustering import silhouette_score


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
    fig, ax = plt.subplots(figsize=(12, 8))
    x = np.linspace(1, 48, 48)
    for j in range(len(price_list)):
        name = area_name[str(cluster_id[j] + 1)]
        ax.plot(x, price_list[j], label=name)
    ax.plot(x, cluster_center, label='聚类中心', linestyle='--', color='black')
    ax.legend(bbox_to_anchor=(1.12, 1), loc='upper right')
    plt.show()


area_name = {'1': '渝北', '2': '江北', '3': '沙坪坝', '4': '南岸', '5': '九龙坡', '6': '渝中', '7': '巴南', '8': '大渡口', '9': '北碚',
           '10': '万州', '11': '璧山', '12': '合川', '13': '永川', '14': '江津', '15': '涪陵', '16': '铜梁', '17': '长寿', '18': '潼南',
           '19': '荣昌', '20': '开州', '21': '大足', '22': '南川', '23': '垫江', '24': '綦江', '25': '梁平', '26': '丰都', '27': '武隆',
           '28': '奉节', '29': '云阳', '30': '石柱', '31': '秀山', '32': '忠县', '33': '彭水', '34': '黔江', '35': '巫山', '36': '酉阳',
           '37': '巫溪'}

df = pd.read_csv('merge_data.csv')
df2 = pd.read_csv('merge_data.csv')
df_list = []

for i in range(37):
    data = df.iloc[i*48:i*48+48, 2].tolist()
    df_list.append(data)
time_series_data = to_time_series_dataset(df_list)
# X = TimeSeriesScalerMeanVariance().fit_transform(time_series_data)

k = 10

sc_score_list = []  # 轮廓系数
inertia_list = []

for i in range(2, k):
    km = TimeSeriesKMeans(n_clusters=i, n_init=2, random_state=0, metric="dtw")
    y_pred = km.fit_predict(time_series_data)
    sc_score = silhouette_score(time_series_data, y_pred, metric="dtw")
    sc_score_list.append(sc_score)
    inertia_list.append(km.inertia_)


plt.plot(list(range(2, k)), inertia_list)
plt.xticks(range(0, k, 1))
plt.grid(linestyle='--')
plt.xlabel("Number of Clusters Initialized")
plt.ylabel("Inertia")
plt.show()

plt.plot(list(range(2, k)), sc_score_list)
plt.xticks(range(0, k, 1))
plt.grid(linestyle='--')
plt.xlabel("Number of Clusters Initialized")
plt.ylabel("Silhouette score")
plt.show()

best_k = 6

km = TimeSeriesKMeans(n_clusters=best_k, n_init=2, random_state=0, metric="dtw")
y_pred = km.fit_predict(time_series_data)
print(y_pred)


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

