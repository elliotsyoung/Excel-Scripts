import openpyxl
import xlrd
import os

files = []
oldFiles = []
laborArray = []

sqlFile = open("InsertLabors2.sql", "w")
sqlFile.write("INSERT INTO labors VALUES \n")
sqlFile = open("InsertLabors2.sql", "a")
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
            if str(sheetsArray[inc]).lower() == "sample" or str(sheetsArray[inc]).lower() == "sheet 1":
                continue
            flag = True
            scanColumns = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R']

            supplier = "dummy"
            name = ""
            cycle = ""
            yeeld = ""
            rate = ""




            # Scan for materials description row
            rowStartIndex = 0
            colIndexArray = []
            for i in range(0,len(scanColumns)):
                if flag:
                    for k in range(6,15):
                        cell = str(scanColumns[i])+str(k)
                        if str(sheet[cell].value).lower() == "operation description" or str(sheet[cell].value).lower() == "operation":
                            rowStartIndex = k
                            break

                else:
                    break

            # Scan for columns
            for i in range(0,len(scanColumns)):
                cell = str(scanColumns[i]) + str(rowStartIndex)
                if str(sheet[cell].value).lower() == "operation description" or str(sheet[cell].value).lower() == "operation":
                    colIndexArray.append(scanColumns[i])
                if str(sheet[cell].value).lower() == "machine":
                    colIndexArray.append(scanColumns[i])
                if str(sheet[cell].value).lower() == "cycle time secs" or str(sheet[cell].value).lower() == "cycle time (secs)":
                    colIndexArray.append(scanColumns[i])
                if str(sheet[cell].value).lower() == "yield" or str(sheet[cell].value).lower() == "yield (%)":
                    colIndexArray.append(scanColumns[i])
                if str(sheet[cell].value).lower() == "total rate $/hr":
                    colIndexArray.append(scanColumns[i])

            # build objects
            for i in range(rowStartIndex+2, 60):
                if str(sheet[str(colIndexArray[0])+str(i)].value) != "None":
                    name = str(sheet[str(colIndexArray[1])+str(i)].value)
                    cycle = str(sheet[str(colIndexArray[2])+str(i)].value)
                    yeeld = str(sheet[str(colIndexArray[3])+str(i)].value)
                    rate = str(sheet[str(colIndexArray[4])+str(i)].value)

                    labor = {
                        'supplier': supplier,
                        'name': name,
                        'cycle': cycle,
                        'yeeld': yeeld,
                        'rate': rate
                    }
                    laborArray.append(labor)
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
            if str(sheetsArray[inc]).lower() == "sample" or str(sheetsArray[inc]).lower() == "sheet 1":
                continue
            flag = True

            supplier = "dummy"
            name = ""
            cycle = ""
            yeeld = ""
            rate = ""




            # Scan for materials description row
            rowStartIndex = 0
            colIndexArray = []
            for i in range(7,30):
                if flag:
                    for k in range(0,4):
                        if str(sheet.cell_value(i,k)).lower() == "operation description" or str(sheet.cell_value(i,k)).lower() == "operation":
                            rowStartIndex = i
                            flag = False
                            break
                else:
                    break
            # Broken Here
            print rowStartIndex
            # Scan for columns
            for i in range(0,10):
                print str(sheet.cell_value(rowStartIndex,i)).lower()
                if str(sheet.cell_value(rowStartIndex,i)).lower() == "operation description" or str(sheet.cell_value(rowStartIndex,i)).lower() == "operation":
                    print "op detected"
                    colIndexArray.append(i)
                if str(sheet.cell_value(rowStartIndex,i)).lower() == "machine":
                    print "mach detected"
                    colIndexArray.append(i)
                if str(sheet[cell].value).lower() == "cycle time secs" or str(sheet[cell].value).lower() == "cycle time (secs)":
                    print "cycle detected"
                    colIndexArray.append(i)
                if str(sheet[cell].value).lower() == "yield" or str(sheet[cell].value).lower() == "yield (%)":
                    print "yeild detected"
                    colIndexArray.append(i)
                if str(sheet.cell_value(rowStartIndex,i)).lower() == "total rate $/hr":
                    print "rate detected"
                    colIndexArray.append(i)

            print colIndexArray
            # build objects
            for i in range(rowStartIndex+2, 60):
                print sheet.cell_value(i,colIndexArray[0])
                if sheet.cell_value(i,colIndexArray[0]) != None:
                    name = str(sheet.cell_value(i, colIndexArray[1]))
                    cycle = str(sheet.cell_value(i, colIndexArray[2]))
                    yeeld = str(sheet.cell_value(i, colIndexArray[3]))
                    rate = str(sheet.cell_value(i, colIndexArray[4]))

                    print name,cycle,yeeld,rate
                    labor = {
                        'supplier': supplier,
                        'name': name,
                        'cycle': cycle,
                        'yeeld': yeeld,
                        'rate': rate
                    }
                    print labor
                    laborArray.append(labor)
                else:
                    break
        except:
            pass

for i in range(0, len(laborArray)):
    if str(laborArray[i]['rate']) == 'None':
        laborArray[i]['rate'] = 0
    elif i == len(laborArray)-1:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), 0, '"+laborArray[i]['name']+"', '"+laborArray[i]['cycle']+"', ("+laborArray[i]['yeeld']+"*100), "+laborArray[i]['rate']+", 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com'));\n")
    else:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), 0, '"+laborArray[i]['name']+"', '"+laborArray[i]['cycle']+"', ("+laborArray[i]['yeeld']+"*100), "+laborArray[i]['rate']+", 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),\n")
sqlFile.close()
