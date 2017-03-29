import openpyxl
import xlrd
import os

files = []
oldFiles = []
materialsArray = []

sqlFile = open("InsertMaterials2.sql", "w")
sqlFile.write("INSERT INTO materials VALUES \n")
sqlFile = open("InsertMaterials2.sql", "a")
tempFiles = os.listdir('/Users/User/Documents/Scripts/Excel Processing/yellow_DUMP')

for f in tempFiles:
    if f.endswith('.xlsx'):
        files.append(f)
    elif f.endswith('.xls'):
        oldFiles.append(f)

for workbook in files:
    print str(workbook)
    wb = openpyxl.load_workbook('/Users/User/Documents/Scripts/Excel Processing/yellow_DUMP/'+str(workbook), read_only = True, data_only = True)

    sheetsArray = wb.get_sheet_names()

    for inc in range(0,len(sheetsArray)):

        try:
            sheet = wb.get_sheet_by_name(str(sheetsArray[inc]))
            # Scanning Area
            if str(sheetsArray[inc]).lower() == "sample" or str(sheetsArray[inc]).lower() == "sheet 1":
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

            supplier = "dummy" # hardcoded for no supplier
            material = ""
            perComponent = ""
            perPart = ""

            # Scan for supplier names
            # No names in these files
            # for i in range(0,len(scanColumns)):
            #     if flag:
            #         for k in range(1,10):
            #             cell = str(scanColumns[i])+str(k)
            #             if str(sheet[cell].value).lower() == "supplier name:" or str(sheet[cell].value).lower() == "supplier":
            #                 supplier = str(sheet[str(scanColumns[i+1])+str(k)].value)
            #
            #     else:
            #         break

            # Scan for materials description column
            colStartIndex = 0
            rowIndexArray = []
            for i in range(0,4):
                if flag:
                    for k in range(0,8):
                        cell = str(scanColumns[i])+str(k)
                        if str(sheet[cell].value).lower() == "component material":
                            colStartIndex = i
                            break

                else:
                    break

            # Scan for rows
            for k in range(0,10):
                cell = str(scanColumns[colStartIndex]) + str(k)
                if str(sheet[cell].value).lower() == "component material":
                    rowIndexArray.append(k)
                if str(sheet[cell].value).lower() == "material cost / component":
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
                        'perPart': perPart
                    }
                    materialsArray.append(material)
                else:
                    break


        except:
            pass



for workbook in oldFiles:
    print str(workbook)

    wb = xlrd.open_workbook('/Users/User/Documents/Scripts/Excel Processing/yellow_DUMP/'+str(workbook))

    sheetsArray = wb.sheet_names()

    for inc in range(0,len(sheetsArray)):

        try:
            sheet = wb.sheet_by_name(str(sheetsArray[inc]))
            # Scanning Area
            if str(sheetsArray[inc]).lower() == "sample" or str(sheetsArray[inc]).lower() == "sheet 1":
                continue

            flag = True

            supplier = "dummy" # hardcoded for no supplier
            material = ""
            perComponent = ""
            perPart = ""


            # Scan for materials description column
            colStartIndex = 0
            rowIndexArray = []
            for i in range(0,4):
                if flag:
                    for k in range(0,8):
                        # print str(sheet.cell_value(k,i)).lower()
                        if str(sheet.cell_value(k,i)).lower() == "material description":
                            colStartIndex = i
                            break

                else:
                    break

            # Scan for rows
            for k in range(0,10):
                if str(sheet.cell_value(k,colStartIndex)).lower() == "material description":
                    rowIndexArray.append(k)
                if str(sheet.cell_value(k,colStartIndex)).lower() == "material cost/unit":
                    rowIndexArray.append(k)
                if str(sheet.cell_value(k,colStartIndex)).lower() == "material cost":
                    rowIndexArray.append(k)

            # build objects
            for i in range(colStartIndex+1, len(scanColumns)):
                if sheet.cell_value(rowIndexArray[0],i) != None:
                    material = str(sheet.cell_value(rowIndexArray[0],i))
                    perComponent = str(sheet.cell_value(rowIndexArray[2],i))
                    perPart = str(sheet.cell_value(rowIndexArray[1],i))

                    material = {
                        'supplier': supplier,
                        'material': material,
                        'perComponent': perComponent,
                        'perPart': perPart
                    }
                    materialsArray.append(material)
                else:
                    break
        except:
            pass







for i in range(len(materialsArray)):
    if str(materialsArray[i]['material']) == '':
        continue
    elif i == len(materialsArray)-1:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), '"+materialsArray[i]['material']+"','"+materialsArray[i]['perComponent']+"','"+materialsArray[i]['perPart']+"', NOW(), NOW(),(select id from proposals where user_id in (select id from users where email='dummy@maker.com')),(select id from users where email = 'dummy@supplier.com'));\n")
    else:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), '"+materialsArray[i]['material']+"','"+materialsArray[i]['perComponent']+"','"+materialsArray[i]['perPart']+"', NOW(), NOW(),(select id from proposals where user_id in (select id from users where email='dummy@maker.com')),(select id from users where email = 'dummy@supplier.com')),\n")

sqlFile.close()
