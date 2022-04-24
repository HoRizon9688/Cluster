import matplotlib.pyplot as plt
import xlrd
import pandas as pd
import numpy as np

cluster_id = [0, 1, 5, 8]
df = pd.read_csv('merge_data.csv')

area_name = {'1': '渝北', '2': '江北', '3': '沙坪坝', '4': '南岸', '5': '九龙坡', '6': '渝中', '7': '巴南', '8': '大渡口', '9': '北碚',
           '10': '万州', '11': '璧山', '12': '合川', '13': '永川', '14': '江津', '15': '涪陵', '16': '铜梁', '17': '长寿', '18': '潼南',
           '19': '荣昌', '20': '开州', '21': '大足', '22': '南川', '23': '垫江', '24': '綦江', '25': '梁平', '26': '丰都', '27': '武隆',
           '28': '奉节', '29': '云阳', '30': '石柱', '31': '秀山', '32': '忠县', '33': '彭水', '34': '黔江', '35': '巫山', '36': '酉阳',
           '37': '巫溪'}

price_list = []
for i in cluster_id:
    temp = df['price'][i * 48:i * 48 + 48]
    price_list.append(temp.tolist())

# print(price_list)

fig, ax = plt.subplots(figsize=(12, 8))
x = np.linspace(1, 48, 48)
for k in range(len(price_list)):
    name = area_name[str(cluster_id[k] + 1)]
    ax.plot(x, price_list[k], label=name)
ax.legend(bbox_to_anchor=(1.1, 1))
plt.show()


# price_list = []
# for i in cluster_id:
#     temp = df['price'][i * 48:i * 48 + 48]
#     price_list.append(temp.tolist())
#
# # print(price_list)
#
# fig, ax = plt.subplots()
# x = np.linspace(1, 48, 48)
# for k in range(len(price_list)):
#     name = area_name[str(cluster_id[k]+1)]
#     ax.plot(x, price_list[k], label=name)
# ax.legend()
# plt.show()
