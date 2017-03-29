import openpyxl
import os

files = []
supplierDict = {}

sqlFile = open("InsertUsers.sql", "w")
sqlFile.write("INSERT INTO users (id,type,company,contact,email,password,created_at,updated_at) VALUES \n")
sqlFile = open("InsertUsers.sql", "a")
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
            for i in range(0,len(scanColumns)):
                if flag:
                    for k in range(1,10):
                        cell = str(scanColumns[i])+str(k)
                        if str(sheet[cell].value).lower() == "supplier name:" or str(sheet[cell].value).lower() == "supplier":
                            supplier = str(sheet[str(scanColumns[i+1])+str(k)].value)
                            if supplier.lower() in supplierDict or supplier == None:
                                flag = False
                                break
                            supplierDict[supplier.lower()] = supplier
                else:
                    break
        except:
            pass

supplierArray = []
for supp in supplierDict:
    supplierArray.append(supp)

for i in range(len(supplierArray)):
    if i == len(supplierArray)-1:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')),1, '" + supplierArray[i] + "', 'Dummy', '"+str(i)+"@dummy.com','$2a$10$kq9/Z90q2fX8rDN0vKfTNuEVpGoJYVJ/SUHLyFn4avW5g7v3D4zE6',NOW(),NOW());\n")
    else:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')),1, '" + supplierArray[i] + "', 'Dummy', '"+str(i)+"@dummy.com','$2a$10$kq9/Z90q2fX8rDN0vKfTNuEVpGoJYVJ/SUHLyFn4avW5g7v3D4zE6',NOW(),NOW()),\n")

sqlFile.write("\n\nINSERT INTO offers (id, proposal_id, user_id, created_at, updated_at) VALUES \n")
for i in range(len(supplierArray)):
    if i == len(supplierArray)-1:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), (SELECT id FROM proposals LIMIT 1), (SELECT id FROM users WHERE company = '" + supplierArray[i] + "'), NOW(), NOW());\n")
    else:
        sqlFile.write("(UNHEX(REPLACE(UUID(), '-', '')), (SELECT id FROM proposals LIMIT 1), (SELECT id FROM users WHERE company = '" + supplierArray[i] + "'), NOW(), NOW()),\n")

sqlFile.close()
