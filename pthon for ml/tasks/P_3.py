
       
def buy(products):
    total_discount_price=0

    while True:
        product_name= input("enter product name: ").lower()
    
        if product_name not in map (lambda x: x["name"].lower(),products):
            print("product not found in the table.please enter a valid product.")
            continue
        quantity_required=float(input("enter quantity required: "))
    #for i in products:
     #if i["name"].lower() == product_name:
       # product = i
       # break 
        product= next(i for i in products if i ["name"].lower()== product_name)
    
        if quantity_required > product["quantity"]:
            print("insufficient quantity.please enter a new quantity.")
            continue
        discount_quantity = quantity_required // 250
        discount_percentage = 5.0 * discount_quantity
        total_discount = min(discount_percentage, 25.0)  
        discounted_price = quantity_required * product["price"] * (1 - total_discount / 100)
    
    
        product["quantity"] -= quantity_required

    
        total_discount_price += discounted_price

        print(f"Discounted Price: ${discounted_price:.2f}")

        another_item = input("Do you want to add another item? (yes/no): ")
        if another_item.lower() != 'yes':
            break
        
        
