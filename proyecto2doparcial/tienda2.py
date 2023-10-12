import os
import platform
import producto2 as c

def true_false_loop(response, message):
    loop_control = False
    boolValue = False

    while loop_control == False:
        if response.lower() == "t" or response.lower() == "T":
            boolValue = True
            loop_control = True

        elif response.lower() == "f" or response.lower() == "F":
            boolValue = False
            loop_control = True

        else:
            response = input("Option not valid. Choose a correct option. Press enter to continue...")

    return boolValue

def clear_console():
    os_name = platform.system()

    if os_name == "Darwin" or os_name == "Linux":
        os.system('clear')

    else:
        os.system('cls')

def main_menu():
    print("\n")
    print ("\033[32m W e l c o m e    t o   S a n    P a b l o   P h a r m a c y \033[0m".center(100,"-"))
    print("\n")
    print("1.- Add product")
    print("2.- Edit product")
    print("3.- Add sale")
    print("4.- Reports")
    print("5.- Exit\n")

def check_product(products, name):
    for product in products:
        if product.Name.lower() == name.lower():
            return product
        
def check_sku(batches, sku):
    for batch in batches:
        return batch
 
 
def sub_menu():
    clear_console()
    print("\n")
    print ("\033[32m S U B M E N U \033[0m".center(100,"-"))
    print ("1. Products Report")
    print ("2. Sales Report")
    print ("3. Return")
def prodsubmenu():
    print("\n\t\033[37;42m    SUBMENU   \033[0m\033[36m \n")
    print("\t\033[37;42m Products Report \033[0m\033[36m ")
    print ("\n1. List all the inventory. ")
    print ("2. See specific product information.")
    print ("3. List products according to the laboratory.")
    print ("4. List products that are about to expire.")
    print ("5. Return to Submenu. ")
    print("Please choose a number: \033[0m") 

def salesubmenu():
    print("\n\t\033[37;42m    SUBMENU   \033[0m\033[36m \n")
    print("\n\t\033[37;42m  Sales Report \033[0m\033[36m \n")
    print ("\n1. See specific sale information.")
    print ("2. List all the sales.")
    print ("3. List all the sales filtered.")
    print ("4. List sales by payment type.")
    print ("5. List sales according to billing. ")
    print ("6. List sales.")
    print ("7. List all the sales according to the lab.")
    print ("8. Return to submenu")
    print ("Please choose a number: \033[0m")
          
def add_product(myC):
    clear_console()
    print ("\033[32m Add Product \033[0m".center(90,"-"))
    temporal_product= c.Product() #this create a temporal car
    #temporal_product.Id= productid
    temporal_product.Name = input("Input the name of the product: ") 
    temporal_product.Laboratory = input("Input the product laboratory: ")
    message = "Input if the product has iva (T/F): "
    temporal_product.Iva = true_false_loop(input(f"{message}"), message)
    myC.add_product(temporal_product)
    input("\nProduct added correctly. Press enter to continue...")
    return myC
    #return Company #this is for update the class

def add_batches(Batches):
   clear_console()
   print ("\033[32m Add Batches to a Product \033[0m".center(90,"-"))
   name_buscar = input("Enter the name of the product that you want to add batches: ")
   product = check_product(myCompany.productList, name_buscar)

   if product:
       temporal_batch = c.ProductBatches() #this create a temporal batch
       temporal_batch.sku = int(input("Input the SKU of the product: "))
       temporal_batch.presentation = input("Input the product presentation: ")
       temporal_batch.cost_value = int(input("Input the cost of the product: "))
       temporal_batch.price_value = float(input("Input the price of the product: "))
       if temporal_batch.price_value <= temporal_batch.cost_value:
           print("This price is not acceptable, please try again.")
           temporal_batch.price_value = int(input("Input the price of the product: "))
  
       temporal_batch.exp_year = int(input("Input the expiration year: "))
       temporal_batch.exp_month = int(input("Input the expiration month: "))
       if temporal_batch.exp_month > 12:
           print("This month doesn't exist. Please enter to continue")
           temporal_batch.exp_month = int(input("Input a valid month: "))
      
       temporal_batch.exp_day = int(input("Input the expiration day: "))
       if temporal_batch.exp_day > 31:
           print("This day doesn't exist. Please enter to continue")
           temporal_batch.exp_day = int(input("Input a valid day: "))
          
           
       temporal_batch.stock = float(input("Input the product stock: "))
       print(temporal_batch.stock)
  
       product.add_batches(temporal_batch)
              
       input("\nBatches added correctly. Press enter to continue...")
   else:
       print ("This product hasn't been added")
       return main_menu
 
 
def buscarproducto():
    print ("---------------SPECIFIC PRODUCT-------------------")
    temporal_batch=c.ProductBatches()
    print ("\nList of products: ")
    myCompany.simProduct()
    name = input("Enter the name of the product wanted: ")
    product = check_product(myCompany.productList, name)
    if product: 
            myCompany.show_productList({name}) 

def add_sales(ventas):
    clear_console()
    print ("\033[32m Add Sale \033[0m".center(90,"-"))
    temporal_sale= c.Venta()
    temporal_batch =c.ProductBatches()
    temporal_sale.order_date = input("\nEnter today's date (In the format YYYY-MM-DD): ")
    print ("\nList of products: ")
    myCompany.show_productList()
    sku_buscar = input("Enter the sku of the product that you want to bought: ")
    sku = check_sku(myCompany.batchesList, sku_buscar)
    if sku:
        
    
    
 
        
        
    

#REPORTS  
mySale= c.Company()
myCompany = c.Company("--- San Pablo pharmaceutical ---")
program_running = True
product = c.Product()  # create a new product object
submenu_running = True

while program_running:
    main_menu()
    option = int (input("Select an option: "))
    if option  == 1:
         myCompany = add_product(myCompany)
    if option == 2:
       myProduct = c.Company()  # create a new product object
       myProduct.add_batches(myProduct)  # add the product to the company
       add_batches(myProduct)  # add batches to the product
       
    if option == 3:
        mySale = add_sales(mySale)
    if option == 4:
        sub_menu()
        opt = int (input("Select an option: "))
        if opt == 1:
            prodsubmenu()
            opt2 = int (input ())
            if opt2 == 1:
                clear_console()
                print("\n -------------------INVENTORY -------------------: ")
                myCompany.show_productList()
            if opt2 == 2:
                clear_console()
                buscarproducto()
            if opt2 ==4:
                products_bylab()
            if opt2 == 7:
                 sub_menu()
                 opt = int (input("Select an option: "))
            
        if opt == 2:
            clear_console()
            salesubmenu()
            opt3 = int (input ())
            if opt3 == 2:
                print("\n------------------- SALES -------------------: ")
                mySale.show_salesList()
            if opt3 == 7:
                 sub_menu()
                 opt = int (input("Select an option: "))
        
    if option == 5:
        print("\nClosing application. Good bye!...\n")
        program_running = False
    
    #else:
    #else:
        #print("Option not valid. Please try again.")
