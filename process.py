import openpyxl
import os

files = []

sqlFile = open("sqlDump.txt", "w")

tempFiles = os.listdir('/Users/User/Documents/Scripts/Excel Processing')

for f in tempFiles:
    if f.endswith('.xlsx'):
        files.append(f)

for workbook in files:
    wb = openpyxl.load_workbook('/Users/User/Documents/Scripts/Excel Processing/'+str(workbook), read_only = True, data_only = True)

    sheetsArray = wb.get_sheet_names()


    array = []



    for inc in range(0,len(sheetsArray)):
        sheet = wb.get_sheet_by_name(str(sheetsArray[inc]))
        flag = True
        column = [
            'C', # Operation
            'D', # Cost per part
            'E', # Material cost/Part Added
            'G', # Machine
            'H', # Cycle Time
            'I', # Yield
            'K'  # $/hr
        ]
        row = 28
        while (flag):
            string = ""
            for element in column:
                if sheet[str(column[0])+str(row)].value != None:
                    if element == 'C':
                        string = str(sheet[str(element)+str(row)].value)
                    else:
                        string = string + "," + str(sheet[str(element)+str(row)].value)
                else:
                    flag = False
                    break
            array.append(string)
            row = row + 1

sqlFile.writelines(array)
sqlFile.close()
print array
