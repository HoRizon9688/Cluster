import numpy as np
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from sklearn.metrics import calinski_harabasz_score
from tslearn.clustering import KShape
from plot_result import *
from sklearn.manifold import TSNE

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

# for i in range(2, k):
#     km_cluster = KMedoids(n_clusters=i, random_state=0)
#     y_pred = km_cluster.fit_predict(df)
#     sc_score = silhouette_score(df, y_pred)
#     sc_score_list.append(sc_score)
#     ch_score = calinski_harabasz_score(df, y_pred)
#     ch_score_list.append(ch_score)
#     inertia_list.append(km_cluster.inertia_)
#
#
# plt.plot(list(range(2, k)), ch_score_list)
# plt.xticks(range(0, k, 1))
# plt.grid(linestyle='--')
# plt.xlabel("Number of Clusters Initialized")
# plt.ylabel("Calinski Harabasz score")
# plt.show()
#
# plt.plot(list(range(2, k)), sc_score_list)
# plt.xticks(range(0, k, 1))
# plt.grid(linestyle='--')
# plt.xlabel("Number of Clusters Initialized")
# plt.ylabel("Silhouette score")
# plt.show()
#
# plt.plot(list(range(2, k)), inertia_list)
# plt.xticks(range(0, k, 1))
# plt.grid(linestyle='--')
# plt.xlabel("Number of Clusters Initialized")
# plt.ylabel("Inertia")
# plt.show()

best_k = 4
# best_k = sc_score_list.index(max(sc_score_list)) + 2
print("最优k值：{}".format(best_k))

best_km = KMedoids(n_clusters=best_k, random_state=0)
y_pred = best_km.fit_predict(df)

r1 = pd.Series(best_km.labels_).value_counts()  # 统计各个类别的数目
r2 = pd.DataFrame(best_km.cluster_centers_)  # 找出聚类中心

r = pd.concat([r2, r1], axis=1)  # 横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(df.columns) + [u'类别数目']  # 重命名表头
print(r)

r = pd.concat([df, pd.Series(best_km.labels_, index=df.index)], axis=1)  # 详细输出每个样本对应的类别
r.columns = list(df.columns) + [u'聚类类别']
print(r)

tsne = TSNE()
tsne.fit_transform(df)
tsne = pd.DataFrame(tsne.embedding_, index=df.index)
# print(tsne)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# d = tsne[r[u'聚类类别'] == 0]  # 找出聚类类别为0的数据对应的降维结果
# plt.scatter(d[0], d[1], color='dodgerblue', marker='*')
# d = tsne[r[u'聚类类别'] == 1]
# plt.scatter(d[0], d[1], color='darkorange', marker='.')
# d = tsne[r[u'聚类类别'] == 2]
# plt.scatter(d[0], d[1], color='mediumpurple', marker='^')
# d = tsne[r[u'聚类类别'] == 3]
# plt.scatter(d[0], d[1], color='dimgrey', marker=',')
# plt.show()

cluster_list = []
color_list = ['dodgerblue', 'darkorange', 'mediumpurple', 'dimgrey']
marker_list = ['*', '.', '^', ',']
for i in range(best_k):
    cluster = np.where(y_pred == i)[0]
    cluster_list.append(cluster)
    id_list = np.array([1] * cluster.size) + cluster
    name_list = []
    for city_id in id_list:
        city_name = area_name[str(city_id)]
        name_list.append(city_name)
    print("cluster {}: {}".format(i + 1, name_list), end='   ')
    print("共{}个城市".format(cluster.size))
    d = tsne[r[u'聚类类别'] == i]
    plt.scatter(d[0], d[1], color=color_list[i], marker=marker_list[i], label="第{}类".format(i+1))
plt.legend()
plt.show()
# cluster_list = []
# for j in range(best_k):
#     cluster = np.where(y_pred == j)[0]
#     cluster_list.append(cluster)
#     plot_clustering(df2, area_name, cluster)
#     id_list = np.array([1] * cluster.size) + cluster
#     name_list = []
#     for city_id in id_list:
#         city_name = area_name[str(city_id)]
#         name_list.append(city_name)
#     print("cluster {}: {}".format(j + 1, name_list), end='   ')
#     print("共{}个城市".format(cluster.size))
#
# plot_all(df2, cluster_list)
