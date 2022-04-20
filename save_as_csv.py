import xlrd
import os
import pandas as pd

# city = os.listdir("./2018")
# sheet = pd.read_excel(io="./2018/巴南.xls", header=None)
# print(sheet)

path = './test/'
file_list = os.listdir(path)
for i in file_list:
    save_name = i.replace("xls", "csv")
    data_xls = pd.read_excel(path + i, sheet_name='sheet1')
    data_xls.to_csv(path + save_name, encoding='utf-8', index=False)
