import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


series = [9109, 9746, 8636, 9040, 9758, 10476, 10975, 11545, 11405, 11243, 11086, 10786,
          10549, 10475, 10532, 10510, 10601, 10639, 10780, 10886, 10889, 10842, 10739, 10615,
          10706, 10678, 10751, 10527, 10508, 10542, 10675, 10712, 10751, 10778, 10800, 10775,
          10791, 10870, 10963, 11111, 11364, 11640, 11755, 11939, 12018, 11903, 11902, 11839]
plt.plot(series)
plt.show()

result1 = adfuller(series, autolag='AIC')
print(f'ADF Statistic: {result1[0]}')
print(f'p-value: {result1[1]}')

# 采用2018-2021巴南区数据检测平稳性，结果为满足时间序列平稳性
