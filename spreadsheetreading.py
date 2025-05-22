#spreadsheetreading.py

# Reading an excel file using Python 
import xlrd 

# Give the location of the file 
loc = ("movies.xls") 

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
print(sheet.cell_value(0, 0)) 

#Extract Number of rows & cols
print (sheet.nrows)
print (sheet.ncols)

#Extract row value
print (sheet.row_values(1))

#Extract col value
print (sheet.col_values(0))