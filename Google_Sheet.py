//отправка таблицы в Google Sheet

import gspread
SERVICE_ACCOUNT="testing-356314-e1ae0fbd5850.json"//то, что мы сформировали с https://console.cloud.google.com/apis/api/sheets.googleapis.com/metrics?project=testing-356314
#testing-356314-e1ae0fbd5850.json  -файл где лежит ключь
gc=gspread.service_account(filename=SERVICE_ACCOUNT)
sh=gc.create("testing_table_for_analitic")//какое название будет у таблицы
sh.share("k.selikhovkina@gmail.com", perm_type="user", role="writer")
worksheet=sh.get_worksheet(0)
worksheet.update([df4.columns.values.tolist()]+df4.values.tolist())//df4-наш датафрейм



//взятие чужой таблицы из Google Sheet
from io import BytesIO
import requests
r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQWMsvBTVio9C7IOOxfFO9C15BRHyME-_ENHqBodDOjuiHwk9fCuF5hUVmDs497PZOqPYK3exdSikOK/pub?gid=1006633900&single=true&output=csv')
data = r.content

dfs = pd.read_csv(BytesIO(data))
