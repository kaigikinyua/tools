from openpyxl import Workbook
import json
import datetime

def fetch_data():
    data=None
    with open("data.json","r") as f:
        data=json.load(f)
    return data
data=fetch_data()
shops_data=data["shops"]
inter_data=data["users"]

wb=Workbook()
shopSheet=wb.active
shopSheet.title="Shops"
interSheet=wb.create_sheet("Internal")
start=2
shopSheet['A1']="NUM"
shopSheet['B1']="Date"
shopSheet['C1']="Shopname"
shopSheet['D1']="Device Description"
shopSheet['E1']="Serial Number"
shopSheet['F1']="Comment"

for col in shops_data:
    shopSheet['A'+str(start)]=start-1
    shopSheet['B'+str(start)]=datetime.date.today()
    shopSheet['C'+str(start)]=col["shopname"]
    shopSheet['D'+str(start)]=col["asset"]
    shopSheet['E'+str(start)]=col["sn"]
    shopSheet['F'+str(start)]=col["comment"]
    start+=1

start=2
interSheet['A1']="NUM"
interSheet['B1']="Date"
interSheet['C1']="Username"
interSheet['D1']="Device Description"
interSheet['E1']="Serial Number"
interSheet['F1']="Comment"
for col in inter_data:
    interSheet['A'+str(start)]=start-1
    interSheet['B'+str(start)]=datetime.date.today()
    interSheet['C'+str(start)]=col["user"]
    interSheet['D'+str(start)]=col["asset"]
    interSheet['E'+str(start)]=col["sn"]
    interSheet['F'+str(start)]=col["comment"]
    start+=1

wb.save("test.xlsx")

    




