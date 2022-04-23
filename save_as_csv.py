import xlrd
import os
import pandas as pd

path = './'

# file_list = os.listdir(path)
# for i in file_list:
#     save_name = i.replace("xls", "csv")
#     data_xls = pd.read_excel(path + i, sheet_name='sheet1')
#     data_xls.to_csv(path + save_name, encoding='utf-8', index=False)


data_xls = pd.read_excel(path + 'merge_data.xls', sheet_name='sheet1')
data_xls.to_csv(path + 'merge_data.csv', encoding='utf-8', index=False)
