import openpyxl
import os

files = []
materialsArray = []

sqlFile = open("InsertMaterials.sql", "w")
sqlFile.write("INSERT INTO temptable VALUES \n")
sqlFile = open("InsertMaterials.sql", "a")
tempFiles = os.listdir('/Users/User/Documents/Scripts/Excel Processing/green_DUMP')

for f in tempFiles:
    if f.endswith('.xlsx') or f.endswith('.xls'):
        files.append(f)


for workbook in files:
    print str(workbook)
    wb = openpyxl.load_workbook('/Users/User/Documents/Scripts/Excel Processing/green_DUMP/'+str(workbook), read_only = True, data_only = True)

    sheetsArray = wb.get_sheet_names()

    for inc in range(0,len(sheetsArray)):

        try:
            sheet = wb.get_sheet_by_name(str(sheetsArray[inc]))
            # Scanning Area
            if str(sheetsArray[inc]).lower() == "sample":
                continue
            scanColumns = [
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
            ]
            flag = True

            supplier = ""
            material = ""
            perComponent = ""
            perPart = ""

            # Scan for supplier names
            for i in range(0,len(scanColumns)):
                if flag:
                    for k in range(1,10):
                        cell = str(scanColumns[i])+str(k)
                        if str(sheet[cell].value).lower() == "supplier name:" or str(sheet[cell].value).lower() == "supplier":
                            supplier = str(sheet[str(scanColumns[i+1])+str(k)].value)

                else:
                    break

            # Scan for materials description column
            colStartIndex = 0
            rowIndexArray = []
            for i in range(0,len(scanColumns)):
                if flag:
                    for k in range(10,25):
                        cell = str(scanColumns[i])+str(k)
                        if str(sheet[cell].value).lower() == "component material":
                            colStartIndex = i
                            break

                else:
                    break

            # Scan for rows
            for k in range(10,30):
                cell = str(scanColumns[colStartIndex]) + str(k)
                if str(sheet[cell].value).lower() == "component material":
                    rowIndexArray.append(k)
                if str(sheet[cell].value).lower() == "kg material / component":
                    rowIndexArray.append(k)
                if str(sheet[cell].value).lower() == "material cost / part":
                    rowIndexArray.append(k)

            # build objects
            for i in range(colStartIndex+1, len(scanColumns)):
                if sheet[str(scanColumns[i])+str(rowIndexArray[0])].value != None:
                    material = str(sheet[str(scanColumns[i])+str(rowIndexArray[0])].value)
                    perComponent = str(sheet[str(scanColumns[i])+str(rowIndexArray[1])].value)
                    perPart = str(sheet[str(scanColumns[i])+str(rowIndexArray[2])].value)

                    material = {
                        'supplier': supplier,
                        'material': material,
                        'perComponent': perComponent,
                        'perPart': perPart,
                        'file': workbook
                    }
                    materialsArray.append(material)
                else:
                    break


        except:
            pass

for i in range(len(materialsArray)):
    if i == len(materialsArray)-1:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), '"+materialsArray[i]['material']+"','"+materialsArray[i]['perComponent']+"','"+materialsArray[i]['perPart']+"', NOW(), NOW(),(select id from proposals where user_id in (select id from users where email='dummy@maker.com')),(select id from users where email = 'dummy@supplier.com'),'"+material[i]['file']+"');\n")
    else:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), '"+materialsArray[i]['material']+"','"+materialsArray[i]['perComponent']+"','"+materialsArray[i]['perPart']+"', NOW(), NOW(),(select id from proposals where user_id in (select id from users where email='dummy@maker.com')),(select id from users where email = 'dummy@supplier.com'),'"+material[i]['file']+"'),\n")

sqlFile.close()
