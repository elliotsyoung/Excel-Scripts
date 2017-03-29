import openpyxl
import os

files = []
laborArray = []

sqlFile = open("InsertLabors.sql", "w").write("INSERT INTO labors (id, type, labor, time, yield, rate, count, created_at, updated_at, proposal_id, user_id) VALUES \n")


sqlFile = open("InsertLabors.sql", "a")

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
            if str(sheetsArray[inc]).lower() == "sample":
                continue
            flag = True
            scanColumns = ['A','B','C','D','E','F','H','I','J','K','L','M','N','O','P','Q','R']

            name = ""
            cycle = ""
            yeeld = ""
            rate = ""



            # Scan for supplier names
            for i in range(0,len(scanColumns)):
                if flag:
                    for k in range(1,10):
                        cell = str(scanColumns[i])+str(k)
                        if str(sheet[cell].value).lower() == "supplier name:" or str(sheet[cell].value).lower() == "supplier":
                            supplier = str(sheet[str(scanColumns[i+1])+str(k)].value)

                else:
                    break

            # Scan for materials description row
            rowStartIndex = 0
            colIndexArray = []
            for i in range(0,len(scanColumns)):
                if flag:
                    for k in range(23,35):
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
                if str(sheet[cell].value).lower() == "machine type or manual labor process":
                    colIndexArray.append(scanColumns[i])
                if str(sheet[cell].value).lower() == "cycle time (seconds)":
                    colIndexArray.append(scanColumns[i])
                if str(sheet[cell].value).lower() == "yield":
                    colIndexArray.append(scanColumns[i])
                if str(sheet[cell].value).lower() == "total rate $/hr":
                    colIndexArray.append(scanColumns[i])

            # build objects
            for i in range(rowStartIndex+2, 60):
                if sheet[str(str(colIndexArray[0])+str(i))].value != None:
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

# print laborArray
for i in range(0, len(laborArray)):
    if str(laborArray[i]['rate']) == 'None':
        laborArray[i]['rate'] = 0
    elif i == len(laborArray)-1:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), 0, '"+laborArray[i]['name']+"', '"+laborArray[i]['cycle']+"', ("+laborArray[i]['yeeld']+"*100), "+laborArray[i]['rate']+", 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com'));\n")
    else:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), 0, '"+laborArray[i]['name']+"', '"+laborArray[i]['cycle']+"', ("+laborArray[i]['yeeld']+"*100), "+laborArray[i]['rate']+", 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),\n")
sqlFile.close()
