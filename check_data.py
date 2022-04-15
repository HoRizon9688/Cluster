import xlrd
import os

year = "./2016"

city = os.listdir(year)
for i in range(len(city)):
    workbook_name = year + "/" + city[i]
    workbook = xlrd.open_workbook(workbook_name)
    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows
    if rows != 12:
        print(city[i])


# 2017缺失数据：云阳.xls # 巫山.xls # 巫溪.xls # 彭水.xls # 酉阳.xls
# 2016年往前数据缺失太多，暂不使用
