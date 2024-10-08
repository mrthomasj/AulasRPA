import xlsxwriter as excel
import os

filename = "C:\\Users\\trjeh\\PycharmProjects\\AulasRPA\\DolarEuro.xlsx"

workbook = excel.Workbook(filename)

sheet1 = workbook.add_worksheet()

sheet1.write('A1', 'Nome')
sheet1.write('B1', 'Valor')

workbook.close()

os.startfile(filename)