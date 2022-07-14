import gspread
SERVICE_ACCOUNT="testing-356314-e1ae0fbd5850.json"//то, что мы сформировали с https://console.cloud.google.com/apis/api/sheets.googleapis.com/metrics?project=testing-356314
#testing-356314-e1ae0fbd5850.json  -файл где лежит ключь
gc=gspread.service_account(filename=SERVICE_ACCOUNT)
sh=gc.create("testing_table_for_analitic")
sh.share("k.selikhovkina@gmail.com", perm_type="user", role="writer")
worksheet=sh.get_worksheet(0)
worksheet.update([df4.columns.values.tolist()]+df4.values.tolist())//df4-наш датафрейм
