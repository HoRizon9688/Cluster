import xlrd
import os
import pandas as pd

# city = os.listdir("./2018")
# sheet = pd.read_excel(io="./2018/巴南.xls", header=None)
# print(sheet)

data_xls = pd.read_excel('渝北.xls', sheet_name='sheet1')
data_xls.to_csv('渝北.csv', encoding='utf-8', index=False)
