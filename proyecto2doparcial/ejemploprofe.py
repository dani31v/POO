import os
import platform
from datetime import date, datetime

# if not any(d['main_color'] == 'red' for d in a):
    # does not exist

# The information that the store wants to keep
myShopProducts = []
mySalesRecord = []

# Catalogs - Usually in systems we have catalogs that will have the unique values available in the system
product_upc = {""}
laboratories = {""}
payment_types = {"Cash", "Card"}

# Definition of functions
def clear_console():
    os_name = platform.system()

    if os_name == "Darwin" or os_name == "Linux":
        os.system('clear')

    else:
        os.system('cls')

def check_product_name_dB(products, name):
    for product in products:

        if product['Name'] == name:
            return True

    return False

def check_get_product_name_dB(products, name):
    for index in range(0,len(products),1):

        if products[index]['Name'] == name:
            return True, index

    return False, -1

def check_get_product_sku_dB(products, sku):
    for index in range(0,len(products),1):
        for index2 in range(0,len(products[index]['Batches']),1):
            if products[index]['Batches'][index2]['SKU'] == sku:
                return True, index, index2

    return False, -1, -1

def yes_no_loop(response, message):
    loop_control = False
    boolValue = False

    while loop_control == False:
        if response.lower() == "y":
            boolValue = True
            loop_control = True

        elif response.lower() == "n":
            boolValue = False
            loop_control = True

        else:
            input("Option not valid. Choose a correct option. Press enter to continue...")
            response = input(message)

    return boolValue

def add_product(products, id):
    correct_product = False

    Product = {
        "Id" : 0,
        "Name" : "",
        "Batches" : [],
        "Tax" : True 
    }

    clear_console()
    print("--- San Pablo pharmaceutical ---")
    print("--------- Add product ----------")

    name = input("Enter the name of the product: ")

    product_exist = check_product_name_dB(products, name)

    if product_exist:
        input("\nProduct already in dB. Press enter to continue...")
        return products, correct_product

    else:
        Product['Name'] = name

    message = "Does the product has taxes? (Y/N): "
    tax = yes_no_loop(input(f"\n{message}"), message)
    Product["Tax"] = tax

    Product["Id"] = id

    products.append(Product)
    
    input("\nProduct added correctly. Press enter to continue...")
    correct_product = True
    
    return products, correct_product

def update_product(products):

    clear_console()

    print("--- San Pablo pharmaceutical ---")
    print("--------- Edit product ---------")

    option = int(input("Search by name (0) or ID (1): "))

    if option == 0:
        name = input("Enter the name of the product: ")
        product_exist, index = check_get_product_name_dB(products, name)

        if product_exist:
            message = "Do you want to change the name of the product? (Y/N): "
            response = yes_no_loop(input(f"\n{message}"), message)

            if response:
                products[index]['Name'] = input("Enter the new name of the product: ")

            message = "Does the product has taxes? (Y/N): "
            tax = yes_no_loop(input(f"\n{message}"), message)
            products[index]["Tax"] = tax

            return products

        else:
            input("\nProduct is not registered in dB. Press enter to continue...")

            return products

    else:
        print(f"\nList of products:")
        display_products(products)

        index = int(input("\nEnter list value of the product: "))
        index -= 1

        if index < len(products) and index >= 0:
            message = "Do you want to change the name of the product? (Y/N): "
            response = yes_no_loop(input(f"\n{message}"), message)

            if response:
                products[index]['Name'] = input("Enter the new name of the product: ")

            message = "Does the product has taxes? (Y/N): "
            tax = yes_no_loop(input(f"\n{message}"), message)
            products[index]["Tax"] = tax

            return products

        else:
            input("\nSelected product is not registered in dB. Press enter to continue...")

            return products

def add_edit_batch(products):
    Product_batch = {
        "SKU" : "",
        "Laboratory" : "",
        "Presentation" : "",
        "Cost_value": 0.0,
        "Price_value": 0.0,
        "Expiration_date" : date(2026,1,1),
        "Stock" : 0
    }

    clear_console()

    print("--- San Pablo pharmaceutical ---")
    print("---- Add-Edit product batch ----")

    option = int(input("Search by name (0) or ID (1): "))

    if option == 0:
        name = input("Enter the name of the product: ")
        product_exist, index = check_get_product_name_dB(products, name)

        if product_exist:

            add_edit_option = int(input("Add (0) or Edit (1) batch: "))
            if add_edit_option == 0:
                sku = input("Input the SKU of the batch: ")
                while sku in product_upc:
                    sku = input("Input an SKU that is not in the dB: ")
                product_upc.add(sku)
                Product_batch["SKU"] = sku

                labo = input("Enter the laboratory of the batch: ")
                laboratories.add(labo)
                Product_batch["Laboratory"] = labo

                Product_batch["Presentation"] = input("Enter the presentation of the batch: ")
                Product_batch["Cost_value"] = float(input("Enter the cost of the batch: "))
                Product_batch["Price_value"] = float(input("Enter the sale price of the batch: "))
                year = int(input("Enter the expiration year of the batch: "))
                month = int(input("Enter the expiration month of the batch: "))
                Product_batch["Expiration_date"] = date(year,month,1)
                Product_batch["Stock"] = int(input("Enter the amount of stock of the batch: "))
                products[index]["Batches"].append(Product_batch)
                return products
            else:
                if len(products[index]["Batches"]) != 0:
                    print(f"\nList of batches:")
                    counter = 1
                    for batch in products[index]["Batches"]:
                        print(f"{counter}.- {batch['SKU']} - {batch['Laboratory']}")
                        counter += 1
                    index_batch = int(input("\nEnter list value of the batch: "))
                    index_batch -= 1
                    if index_batch < len(products) and index_batch >= 0:
                        value = products[index]["Batches"][index_batch]["SKU"]
                        product_upc.remove(value)
                        
                        sku = input(f"Input the new SKU of the batch ({value}): ")
                        while sku in product_upc:
                            sku = input(f"Input an SKU that is not in the dB ({value}): ")
                        product_upc.add(sku)
                        products[index]["Batches"][index_batch]["SKU"] = sku

                        value = products[index]["Batches"][index_batch]["Laboratory"]
                        labo = input(f"Enter the new laboratory of the batch ({value}): ")
                        laboratories.add(labo)
                        products[index]["Batches"][index_batch]["Laboratory"] = labo
                        
                        value = products[index]["Batches"][index_batch]["Presentation"]
                        products[index]["Batches"][index_batch]["Presentation"] = input(f"Enter the new presentation of the batch ({value}): ")

                        value = products[index]["Batches"][index_batch]["Cost_value"]
                        products[index]["Batches"][index_batch]["Cost_value"] = float(input(f"Enter the new cost of the batch ({value}): "))

                        value = products[index]["Batches"][index_batch]["Price_value"]
                        products[index]["Batches"][index_batch]["Price_value"] = float(input(f"Enter the new sale price of the batch ({value}): "))

                        value = products[index]["Batches"][index_batch]["Expiration_date"]
                        year = int(input(f"Enter the new expiration year of the batch ({value.year}): "))
                        month = int(input(f"Enter the new expiration month of the batch ({value.month}): "))
                        products[index]["Batches"][index_batch]["Expiration_date"] = date(year,month,1)

                        value = products[index]["Batches"][index_batch]["Stock"]
                        products[index]["Batches"][index_batch]["Stock"] = int(input(f"Enter the amount of stock of the batch ({value}): "))

                    return products
                
                else:
                    input("\nThere are no batches of the selected product in dB. Press enter to continue...")
                    return products
                
        else:
            input("\nProduct is not registered in dB. Press enter to continue...")
            return products

    else:
        print(f"\nList of products:")
        display_products(products)

        index = int(input("\nEnter list value of the product: "))
        index -= 1

        if index < len(products) and index >= 0:
            add_edit_option = int(input("Add (0) or Edit (1) batch: "))
            if add_edit_option == 0:
                sku = input("Input the SKU of the batch: ")
                while sku in product_upc:
                    sku = input("Input an SKU that is not in the dB: ")
                product_upc.add(sku)
                Product_batch["SKU"] = sku

                labo = input("Enter the laboratory of the batch: ")
                laboratories.add(labo)
                Product_batch["Laboratory"] = labo

                Product_batch["Presentation"] = input("Enter the presentation of the batch: ")
                Product_batch["Cost_value"] = float(input("Enter the cost of the batch: "))
                Product_batch["Price_value"] = float(input("Enter the sale price of the batch: "))
                year = int(input("Enter the expiration year of the batch: "))
                month = int(input("Enter the expiration month of the batch: "))
                Product_batch["Expiration_date"] = date(year,month,1)
                Product_batch["Stock"] = int(input("Enter the amount of stock of the batch: "))
                products[index]["Batches"].append(Product_batch)
                return products
            else:
                if len(products[index]["Batches"]) != 0:
                    print(f"\nList of batches:")
                    counter = 1
                    for batch in products[index]["Batches"]:
                        print(f"{counter}.- {batch['SKU']} - {batch['Laboratory']}")
                        counter += 1
                    index_batch = int(input("\nEnter list value of the batch: "))
                    index_batch -= 1
                    if index_batch < len(products) and index_batch >= 0:
                        value = products[index]["Batches"][index_batch]["SKU"]
                        product_upc.remove(value)
                        
                        sku = input(f"Input the new SKU of the batch ({value}): ")
                        while sku in product_upc:
                            sku = input(f"Input an SKU that is not in the dB ({value}): ")
                        product_upc.add(sku)
                        products[index]["Batches"][index_batch]["SKU"] = sku

                        value = products[index]["Batches"][index_batch]["Laboratory"]
                        labo = input(f"Enter the new laboratory of the batch ({value}): ")
                        laboratories.add(labo)
                        products[index]["Batches"][index_batch]["Laboratory"] = labo

                        value = products[index]["Batches"][index_batch]["Presentation"]
                        products[index]["Batches"][index_batch]["Presentation"] = input(f"Enter the new presentation of the batch ({value}): ")

                        value = products[index]["Batches"][index_batch]["Cost_value"]
                        products[index]["Batches"][index_batch]["Cost_value"] = float(input(f"Enter the new cost of the batch ({value}): "))

                        value = products[index]["Batches"][index_batch]["Price_value"]
                        products[index]["Batches"][index_batch]["Price_value"] = float(input(f"Enter the new sale price of the batch ({value}): "))

                        value = products[index]["Batches"][index_batch]["Expiration_date"]
                        year = int(input(f"Enter the new expiration year of the batch ({value.year}): "))
                        month = int(input(f"Enter the new expiration month of the batch ({value.month}): "))
                        products[index]["Batches"][index_batch]["Expiration_date"] = date(year,month,1)

                        value = products[index]["Batches"][index_batch]["Stock"]
                        products[index]["Batches"][index_batch]["Stock"] = int(input(f"Enter the amount of stock of the batch ({value}): "))

                    return products
                
                else:
                    input("\nThere are no batches of the selected product in dB. Press enter to continue...")
                    return products
        
        else:
            input("\nSelected product is not registered in dB. Press enter to continue...")
            return products

def create_sale(products, sales, id):
    correct_sale = False

    Sale = {
    "Order_number" : 0,
    "Order_date": datetime.now(),
    "Items_sold": [],
    "Subtotal": 0.0,
    "Taxes_amout": 0.0, # New value
    "Total": 0.0,
    "Payment_type" : "",
    "Is_Billed" : False
    }

    clear_console()
    print("--- San Pablo pharmaceutical ---")
    print("--------- Create sale ----------")

    Sale['Order_number'] = id

    continue_sale = True
    sku = input("Enter the sku of the product (Type 0 to exit): ")
    while continue_sale:
        product_exist, i, i2 = check_get_product_sku_dB(products, sku)

        if not(product_exist):
            sku = input("\nProduct not in dB. Enter a correct SKU: ")

        else:
            # Additional dictionary to contain the information for a sale and AVOID duplicity
            Sold_product = {
            "Name" : "",
            "Presentation" : "",
            "Laboratory" : "",
            "Price_value": 0.0,
            "Has_tax" : True, 
            "Quantity_sold": 0, # New value
            }

            Sold_product['Name'] = products[i]['Name']
            Sold_product['Presentation'] = products[i]['Batches'][i2]['Presentation']
            Sold_product['Laboratory'] = products[i]['Batches'][i2]['Laboratory']
            Sold_product['Price_value'] = products[i]['Batches'][i2]['Price_value']
            Sold_product['Has_tax'] = products[i]['Tax']
            qty = int(input("How many products of this presentation do you want to sale? "))

            if qty <= products[i]['Batches'][i2]['Stock']:
                Sold_product['Quantity_sold'] = qty
                products[i]['Batches'][i2]['Stock'] -= qty
                Sale['Items_sold'].append(Sold_product)

            else:
                input("\nAmount not available. Press enter to continue...")

        message = "Do you want to add another product? (Y/N): "
        response = yes_no_loop(input(f"\n{message}"), message)

        if response:
            sku = input("\nEnter the sku of the product: ")

        else:
            continue_sale = False

    if len(Sale['Items_sold']) == 0:
        input("\nSale is empty. Returning to the previous menu. Press enter to continue...")
        return products, sales, correct_sale
    
    else:
        subtotal = 0.0
        taxes_amout = 0.0

        for product_sold in Sale['Items_sold']:
            amount = product_sold['Price_value'] * product_sold['Quantity_sold']

            if product_sold['Has_tax']:
                subtotal = subtotal + amount
                taxes_amout = taxes_amout + (amount * 0.16)

            else:
                subtotal = subtotal + amount

        total = subtotal + taxes_amout
        Sale['Subtotal'] = subtotal
        Sale['Taxes_amout'] = taxes_amout
        Sale['Total'] = total

        correct_input = False
        pay_types = list(payment_types)
        while not(correct_input):
            print("Choose payment type:")
            counter = 1

            for paymentType in pay_types:
                print(f"{counter}.- {paymentType}")
                counter += 1

            j = int(input(": "))
            j -= 1

            if j < len(products) and j >= 0:
                Sale['Payment_type'] = pay_types[j]
                correct_input = True

            else:
                input("Option not valid. Press enter to continue...")
                
        message = "Do you want to bill the sale? (Y/N): "
        Sale['Is_Billed'] = yes_no_loop(input(f"\n{message}"), message)
        sales.append(Sale)
        correct_sale = True
        return products, sales, correct_sale

def display_products(products, displayMode = 0):
    if displayMode == 0:
        counter = 1
        for product in products:
            print(f"{counter}.- {product['Name']}")
            counter += 1
    elif displayMode == 1:
        clear_console()
        print("--- San Pablo pharmaceutical ---")
        print("- Specific product information -")
        print("\nList of products:\n")
        counter = 1
        for product in products:
            print(f"{counter}.- {product['Name']}")
            counter += 1
        index = int(input("\nEnter list value of the product: "))
        index -= 1
        if index < len(products) and index >= 0:
            print("\nBatch list: ")
            counter = 1
            for batch in products[index]['Batches']:
                print(f"{counter}.- {batch['SKU']} - {batch['Laboratory']} - ${batch['Price_value']} - Exp: {batch['Expiration_date']} - x{batch['Stock']}")
                counter += 1
            input("\nPress enter to continue...")
        else:
            input("\nSelected product is not registered in dB. Press enter to continue...")
    elif displayMode == 2:
        clear_console()
        print("--- San Pablo pharmaceutical ---")
        print("----- Products information -----")
        print("\nList of products:\n")
        counter = 1
        for product in products:
            stock = 0
            for batches in product['Batches']:
                stock += batches['Stock']
            print(f"{counter}.- {product['Name']} - Batches: {len(product['Batches'])} - x{stock}")
            counter += 1
        input("\nPress enter to continue...")
    elif displayMode == 3:
        clear_console()
        print("---- San Pablo pharmaceutical ----")
        print("------ Laboratory products -------")
        print("\nList of laboratories:\n")
        labs = list(laboratories)
        labs.pop(0)
        counter = 1
        for lab in labs:
            print(f"{counter}.- {lab}")
            counter += 1
        index = int(input("\nEnter list value of the laboratory: "))
        index -= 1
        counter = 1
        if index < len(products) and index >= 0:
            print("\nList of products:")
            for product in products:
                for batch in product['Batches']:
                    if labs[index] == batch['Laboratory']:
                        print(f"{counter}.- {product['Name']} - {batch['SKU']} - x{batch['Stock']}")
                        counter += 1
            input("\nPress enter to continue...")
        else:
            input("\nSelected product is not registered in dB. Press enter to continue...")
        
    else:
        print("Option not available")

def display_sales(sales, displayMode = 0):
    if displayMode == 0:
        print("--- San Pablo pharmaceutical ---")
        print("------- Sales information ------")
        print("\nList of sales:\n")
        print("\nList of sales:\n")
        counter = 1
        for sale in sales:
            print(f"{counter}.- {sale['Order_number']} - {sale['Total']}")
            counter += 1
        input("\nPress enter to continue...")
    elif displayMode == 1:
        print("--- San Pablo pharmaceutical ---")
        print("-- Specific sale information ---")
        print("\nList of sales:\n")
        counter = 1
        for sale in sales:
            print(f"{counter}.- {sale['Order_number']}")
            counter += 1
        index = int(input("\nEnter list value of the product: "))
        index -= 1
        if index < len(sales) and index >= 0:
            print(sales[index]['Order_number'])
            print(sales[index]['Order_date'])
            if sales[index]['Is_Billed']:
                print(f"Saled billed and paid using {sales[index]['Payment_type']}")
            else:
                print(f"Saled not billed and paid using {sales[index]['Payment_type']}")
            print("Products:")
            for product in sales[index]['Items_sold']:
                print(f"{product['Name']} {product['Presentation']} - {product['Laboratory']} - ${product['Price_value']} - x{product['Quantity_sold']}")
            print(f"Subtotal: ${sales[index]['Subtotal']}")
            print(f"Taxes   : ${sales[index]['Taxes_amout']}")
            print(f"Total   : ${sales[index]['Total']}")

            input("\nPress enter to continue...")
        else:
            input("\nSelected sale is not registered in dB. Press enter to continue...")
    else:
        print("Option not available")

def main_menu():
    clear_console()
    print("--- San Pablo pharmaceutical ---")
    print("1.- Add product")
    print("2.- Edit product (new)")
    print("3.- Add sale") 
    print("4.- Reports")
    print("5.- Exit\n")

def update_product_menu(products):

    submenu_running = True

    while submenu_running:
        clear_console()
        print("--- San Pablo pharmaceutical ---")
        print("-------- Update product --------")
        print("1.- Edit parent product")
        print("2.- Add/Edit product batch")
        print("3.- Return\n")

        option = int(input("Select your option: "))
        
        if option == 1 and len(products) == 0:
            input("\nThere are not products registered in the dB. Add some products to proceed. Press enter to continue...")
        elif option == 1 and len(products) > 0:
            products = update_product(products)
        elif option == 2:
            products = add_edit_batch(products)
        elif option == 3:
            input("\nReturning to previous menu. Press enter to continue...")
            submenu_running = False
        else:
            input("\nOption not valid. Choose a correct option. Press enter to continue...")

    return products

def reports_menu(products, sales):
    
    submenu_running = True
    
    while submenu_running:
        clear_console()
        print("--- San Pablo pharmaceutical ---")
        print("----------- Reports ------------")
        print("1.- Product reports")
        print("2.- Sale reports")
        print("3.- Return\n")
        
        option = int(input("Select your option: "))
        
        if option == 1 and len(products) == 0:
            input("\nThere are not products registered in the dB. Add some products to proceed. Press enter to continue...")
        elif option == 1 and len(products) > 0:
            product_reports_menu(products)
        elif option == 2 and len(sales) == 0:
            input("\nThere are not sales registered in the dB. Add some products to proceed. Press enter to continue...")
        elif option == 2 and len(sales) > 0:
            sale_reports_menu(sales)
        elif option == 3:
            input("\nReturning to previous menu. Press enter to continue...")
            submenu_running = False
        else:
            input("\nOption not valid. Choose a correct option. Press enter to continue...")
  
    return products, sales

def product_reports_menu(products):
    
    submenu_running = True
    
    while submenu_running:
        clear_console()
        print("--- San Pablo pharmaceutical ---")
        print("------- Product Reports --------")
        print("1.- See specific product")
        print("2.- List of all product")
        print("3.- List of products by laboratory")
        print("4.- List of soon to expiry products (Extra)")
        print("5.- Return\n")

        option = int(input("Select your option: "))

        if option == 1:
            display_products(products, 1)
        elif option == 2:
            display_products(products, 2)
        elif option == 3:
            display_products(products, 3)
        elif option == 4:
            pass
        elif option == 5:
            input("\nReturning to previous menu. Press enter to continue...")
            submenu_running = False
        else:
            input("\nOption not valid. Choose a correct option. Press enter to continue...")

    return products

def sale_reports_menu(sales):
    
    submenu_running = True

    while submenu_running:
        clear_console()
        print("--- San Pablo pharmaceutical ---")
        print("--------- Sale Reports ---------")
        print("1.- See specific sale")
        print("2.- List of sales")
        print("2.- List of sales by filter (Extra)")
        print("3.- List of sales by laboratory (Extra)")
        print("4.- List of sales by payment type")
        print("5.- List of sales according to billing (Extra: Amount of tax $)")
        print("6.- Return\n")

        option = int(input("Select your option: "))
        
        if option == 1:
            display_sales(sales, 1)
        elif option == 2:
            display_sales(sales, 0)
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            input("\nReturning to previous menu. Press enter to continue...")
            submenu_running = False
        else:
            input("\nOption not valid. Choose a correct option. Press enter to continue...")

    return sales

# Main program
# Flag to state that the program will run until it is false
program_running = True
product_id = 0
order_number = 1

while program_running:

    main_menu()

    option = int(input("Select your option: "))
    
    if option == 1:
        myShopProducts, product_recorded = add_product(myShopProducts, product_id)
        if product_recorded:
            product_id += 1

    elif option == 2 and len(myShopProducts) == 0:
        input("\nThere are not products registered in the dB. Add some products to proceed. Press enter to continue...")

    elif option == 2 and len(myShopProducts) > 0:
        myShopProducts = update_product_menu(myShopProducts)

    elif option == 3 and len(myShopProducts) == 0:
        input("\nThere are not products registered in the dB. Add some products to proceed. Press enter to continue...")

    elif option == 3 and len(myShopProducts) > 0:
        myShopProducts, mySalesRecord, sale_recorded = create_sale(myShopProducts, mySalesRecord, order_number)
        if sale_recorded:
            order_number += 1

    elif option == 4:
        myShopProducts, mySalesRecord = reports_menu(myShopProducts, mySalesRecord)
        
    elif option == 5:
        print("\nClosing application. Good bye!...\n")
        program_running = False

    else:
        input("\nOption not valid. Choose a correct option. Press enter to continue...")
    