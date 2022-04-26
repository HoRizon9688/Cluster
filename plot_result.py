import numpy as np
import matplotlib.pyplot as plt


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


def plot_all(df, cluster_list):
    color_list = ['darkgreen', 'darkorange', 'red', 'mediumturquoise', 'royalblue', 'mediumpurple', 'deeppink', 'dimgrey']
    fig, ax = plt.subplots(figsize=(16, 10))
    for k in range(len(cluster_list)):
        cluster_id = cluster_list[k]
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
        x = np.linspace(1, 48, 48)
        for j in range(len(price_list)):
            ax.plot(x, price_list[j], color=color_list[k])
        ax.plot(x, cluster_center, linestyle='--', color=color_list[k], linewidth=4)
    plt.show()
