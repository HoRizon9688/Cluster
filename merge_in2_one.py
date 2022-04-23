import xlrd
import xlwt
import os
import pandas as pd

path = './test/'
city = os.listdir(path)

info_list = []

for i in range(len(city)):
    workbook_name = path + city[i]
    workbook = xlrd.open_workbook(workbook_name)
    worksheet = workbook.sheet_by_index(0)
    row = worksheet.nrows
    for j in range(1, row):
        row_data = worksheet.row_values(j)
        int_row_data = list(map(int, row_data))
        info_list.append(int_row_data)

info_list.sort()  # 从1到37排序，需转为int类型后再用sort排序

merge_workbook = xlwt.Workbook(encoding='utf-8')
merge_worksheet = merge_workbook.add_sheet('sheet1')
merge_worksheet.write(0, 0, "id")
merge_worksheet.write(0, 1, "timestamp")
merge_worksheet.write(0, 2, "price")
for k in range(len(info_list)):
    merge_worksheet.write(k + 1, 0, info_list[k][0])
    merge_worksheet.write(k + 1, 1, info_list[k][1])
    merge_worksheet.write(k + 1, 2, info_list[k][2])
merge_workbook.save(path + 'merge_data.xls')
