from prject_1 import login

from P_3 import buy



login
from prettytable import PrettyTable
products=[
    {"name":"water","price":88.0,"quantity":1200},
    {"name":"soda","price":130.0,"quantity":1200}, 
    {"name":"ships","price":75.0,"quantity":1200},
    {"name":"bread","price":45.0,"quantity":1200},    
    {"name":"eggs","price":65.0,"quantity":1200},    

    ]  

table=PrettyTable()
table.field_names=["name","price","quantity"]

for product in products:
    table.add_row([product["name"],product["price"],product["quantity"]])
table    


print(buy(products) )
       
       
    
   