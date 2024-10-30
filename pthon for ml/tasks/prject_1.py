import random
from prettytable import prettytable
u ="Dimes"
p="1111"
def login():
    
    while True:
        x=input("name: ")
        if x== u:
            y=input("password: ")
            
            if y==p:
                s=random.randrange(10000,1000000)
                print("varification code is ",s)
                
                while True:
                    l=int(input("enter verification code: "))
                    if l ==s:
                        print("welcome")
                        break
                    else:
                        print("incorrect verification code. tryagain.")
                break
            else:
                print("incorrect password")
        else:
            print("incorrect username")       
        
              
                
    