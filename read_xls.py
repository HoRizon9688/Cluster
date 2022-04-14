import xlrd
import re

workbook = xlrd.open_workbook('./2018/万州.xls')

sheet = workbook.sheet_by_index(0)

# cols_num = sheet.ncols
# row_num = sheet.nrows

cols = sheet.col_values(1)

print(cols)

find_price = re.compile(r'\d*')
price_list = []
for i in cols:
    price = find_price.findall(i)
    price_list.append(int(price[0]))
print(price_list)

avg = sum(price_list)/len(price_list)
print("{:.0f}".format(avg))
