from datetime import datetime, timedelta
import time
import os

# VARIABLES AND LISTS
opc = 0
subl_prod=0
x = 1
band= 0
band2=0
option2 = 0
product = {} 
sales = []
nombre = []
identificador= []
codeBar = []
presentation = []
laboratory =[]
stock = []
cost =[]
sale_Value =[]
expirationd=[]
iva =[]
registro_ventas = []
yes_iva =[]
no_iva = []
card_cash=[]
bill =[]
registro_productos=[]
specific_S=[]
registro_s=[]
subtotal_prod=[]
subtotal=[]
fechas_convertidas = []

# FUNCTIONS  

def clear_console():
  os.system('clear')

def main ():

    print("""\n\t\033[37;42m MENÚ \033[0m\033[36m \n
  1. Add product
  2. Create a Sale
  3. Reports
  4. Exit\033[0m
  
  Please choose a number:""")


    opc = int(input())
    if opc == 1:
         
         addproducts ()
           
    elif (opc == 2):
            sales ()
    
    elif (opc == 3):
            submenureports()
       
    elif (opc==4):
        print("\033[31m You have exited the program \033[0m ")
        exit
    else:
        print("\033[31m ERROR. Enter a valid number\033[0m ")
        return main()
    
def addproducts():
    

    option2= int(input("How many products you want to register?: "))
    for i in range (0, option2,1): 
        print(f"\nID:{i+1}")
        nombre.append(str(input(f"Enter the name of the product : ")))
        codeBar.append(str(input(f"Enter de Bar code of the product  : ")))
        presentation.append(str(input(f"Enter the presentation of the product (ex. tablet 500mg) : ")))
        laboratory.append(str(input("Enter the manufacturer/laboratory of the product: ")))
        stock.append(int(input("Enter the stock/quantity of existent product in the pharmacy: ")))
        cost.append(float(input("Enter the cost value of the product: $ ")))
        sale_Value.append(float(input("Enter the sale value of the product: $ ")))
        if sale_Value <= cost:
            print("The sale value is minor or equal than the cost. Please try again.")
            sale_Value.append(float(input("Enter the sale value of the product: $ ")))
        expirationd.append(input("Enter the expiration date: (In the format YYYY-MM-DD) "))
        iva.append(int(input("Does your product have taxes? \n 1.TRUE \n 2.FALSE \nEnter an option: ")))
        if iva == 1:
         yes_iva.append()
        if iva == 2:
            no_iva.append()

    for i in expirationd: # Converting the date entered by the user from a string, to the desired date format with 'datetime'.
        form_fecha = datetime.strptime(i, "%Y-%m-%d")
        fechas_convertidas.append(form_fecha) # Save them to a new list.

    return main()
   
def sales():
    clear_console()
    
    
    option3= int(input("How many sales you want to register?: "))
    for i in range (0, option3):
     print (f"\n-------SALE {i+1}-------")
     fecha_Registrada = input("\nEnter today's date (In the format YYYY-MM-DD): ")
     print ("\nList of products: ")
     x = 1 
     for s in nombre:
        
        print (f"{x}.- {s} ")
        x+=1 
        eleccion = int(input("Enter the number of the product wanted:"))
    
     print (f"{nombre[eleccion-1]}: x{stock[eleccion-1]} price: {sale_Value[eleccion-1]}")
     cant = int(input("Enter the quantity of the product you want: "))
         
     if(cant > stock[eleccion-1] and cant > 0):
            print(f"\033[31m ERROR. We don't have this stock, the maximum is: {stock[eleccion-1]} try again.\033[0m")
            cant = int(input("Enter the quantity of the product you want: "))
     else:
        option2 = int(input(("\n Do you want to add another product to the sale?  \n 1.- YES \n 2.- NO \nEnter an option:")))
     stock[eleccion-1]= (stock[eleccion-1]-cant) 
        #if option2 == 1:
               
     if option2 == 2:
         subl_prod = cant*sale_Value[eleccion-1]
         subtotal_prod.append(subl_prod)
        
         print(f"{i+1}.- {nombre[eleccion-1]}")
         print(f"The total price of this product is: {subl_prod} ")
         print(f"Your total of the sale is:", (subl_prod)*1.16)
    
     print("\nHow do you want to pay?")
     card_cash.append(int(input(" 1.Cash \n 2.Card \nEnter an option:")))
     
         
     print("\nDo you want your sale to be billed?")
     bill.append(int(input(" 1.YES \n 2.NO \nEnter an option:")))
    
    
    

     specific_S =[f"{nombre[eleccion-1]}, {sale_Value[eleccion-1]}"]
        #{Total[eleccion-1]}}
     registro_s.append(specific_S)
   
     v= 1
     
     venta = [f"{i+1} ||  {nombre[eleccion-1]}  ||      {cant}      ||   ${sale_Value[eleccion-1]}  ||  {iva[eleccion-1]} || "]
     registro_ventas.append(venta) 
        
    
    return main()   
        
     
     
def specific_sales():
    print("---------SPECIFIC SALES---------")
    y= 1
    for i in registro_s:
       print (f"{y}.- {i}")
       y+=1
    dif_sales= int(input("Enter the number of sale for more information: "))
    print (registro_ventas[dif_sales-1])      
    
    return submenureports() 

        
def see_sales():
   
       print ("---------------- SALES -----------------------".center(100,"-"))
       fecha_actual = datetime.now()
       print (f"\n {fecha_actual}")
       print("\n")
       for i in registro_ventas:
        print ("\n")
        print ( " NO.||    DATE    ||      NAME      ||   QUANTITY   ||    PRICE   || TOTAL OF PRODUCT ||")
        print ("-----------------------------------------------------------------------------------------------------")
        print (i)
        return2 = (int(input(("Do you want to go back to the submenu or Menu? \n1.Yes \n2.No "))))
        if return2 == 1:
             return submenureports()
        elif return2 ==2:
             exit
        

def salesbypayment():
   pay=(int(input("What lists do you want to see: \n1.Cash\n2.Card. \nEnter your option: ")))
   counter = 0
   for i in card_cash:
       if i == pay:
           
           print(registro_ventas[counter])
           pass
       else:
           pass
       counter += 1
   return submenureports()

def salesbilled():
    billed=(int(input("What lists do you want to see: \n1.Billed\n2.Not Billed. \nEnter your option: ")))
    counter = 0
    print("The lists that are: ")
    for c in bill:
       if c == billed:
           print(registro_ventas[counter])
           pass
       else:
           pass
       counter += 1
    return submenureports()      
                 
def specific_product():
    print ("---------------SPECIFIC PRODUCT-------------------")
    x = 1 
    for i in nombre: # show the user the available products.
        print (f"{x}.- {i}")
        x+=1 
    # enter the position we want to access in each of the product lists and prints the item in that position.
    elección = int(input("Enter the number of the product that you want for more information:")) 
    print (f"""\t{nombre[elección-1]}: 
      - codebar: {codeBar[elección-1]}
      - presentation: {presentation[elección-1]}
      - laboratory: {laboratory[elección-1]}
      - stock: x{stock[elección-1]}
      - cost: ${cost[elección-1]} / price: ${sale_Value[elección-1]}
      - expiration date: {expirationd[elección-1]}
      - IVA: {iva[elección-1]}""")
      
    option = int(input(("\nDo you want to see another product ?  \n 1.- YES \n 2.- NO \nEnter an option (1 / 2):")))
    if option == 1:
        return specific_product()
    elif option == 2:
       return submenureports()
    else:
        print("ERROR. This number doesn't belong to the options.")
        counterprod= 0
    
def inventory ():
    print ("\n -------------------INVENTORY -------------------: ")
    p = 1 
    elección = 1
    for i in nombre: # Taking the list of names as a reference, the elements of each list are printed by position.
            print(f"{p}.- {i}, BarCode: {codeBar[elección-1]}, presentation: {presentation[elección-1]}, laboratory: {laboratory[elección-1]}, stock: x{stock[elección-1]}, cost: ${cost[elección-1]} / price: ${sale_Value[elección-1]}, expiration date: {expirationd[elección-1]}, IVA: {iva[elección-1]}")
            elección+=1 # increases the position by 1 by 1 in order to print the next product.
            p+=1 
    print("\nYou have exited the inventory")
    return submenureports()

def products_bylab(): 
    lab_buscar = input("Enter the name of the laboratory that you want: ") # the lab you are looking for
    print("-------------------------------------------------------------")
    print("\n The products associated with this laboratory are: ")
    posiciones = [] 
    
    for i in range(len(laboratory)): 
        if laboratory[i] == lab_buscar: #compare the lab of each product, with the lab entered
            posiciones.append(i) # saves the positions of the elements that match the entered lab.

            if len(posiciones) > 0: # if there are items in the list, print the same position in the list [name]
                print(f"\n- {nombre[i]}")
                
    if not posiciones: # if there are no items in the list.
            print(f"Non-existent.")
    
    option=int(input("\nDo you want to see another product according to their laboratory?  \n 1.- YES \n 2.- NO \nEnter an option (1 / 2):"))
    if option == 1:
       return products_bylab()
    elif option == 2:
       return submenureports()
    else:
      print("ERROR. This number doesn'tbelong  to the options.")    
    return submenureports()

def about_to_expire():
    print("\n\033[34m The products that are about to expire or have already expired are:\n\033[0m")
    hoy = datetime.today()  # Actual date with the datetime module.
    limite = hoy + timedelta(days=5)  # Define a time limit, between the current date and the product dates.

    proximos_productos = [] # List in which the positions of dates that are less than or equal to the limit are stored. 
    for i in range(len(fechas_convertidas)):

        if fechas_convertidas[i] <= limite:
            proximos_productos.append(i) 
            print(f"\t- {nombre[i]} // Expiration date in: {fechas_convertidas[i]}") #print the position in name and date that corresponds to the list of next_products.
    
    if not proximos_productos: # if the list is empty, there are no products to expire.
            print(f"Non-existent.")
    
    option = int(input(("\n\033[30m Do you want to perform another action in the submenu  or menu?  \n 1.- YES \n 2.- EXIT \nEnter an option (1 / 2):\033[0m")))
    
    if option == 1:
        return submenureports()
        
    elif option == 2:
        print("\033[31m You have exited the program. \033[0m")
    else:
      print("ERROR. This number doesn'tbelong  to the options.")
        #print("No hay productos próximos a caducar.")
 

def submenureports():
   print("""\n\t\033[37;42m SUBMENU \033[0m\033[36m \n  
 1. See specific sale information.
 2. List all the sales.
 3. List all the sales filtered.
 4. List sales by payment type.
 5. List sales according to billing. 
 6. List sales.
 7. See specific product information.
 8. List all the inventory.
 9. List products according to the laboratory.
 10. List products that are about to expire.
 11. List all the sales according to the lab.
 12. EXIT
  \n Please choose a number \033[0m""")
   opt = int(input())

   if opt == 1: # See specific sale information
      return specific_sales()
   elif opt == 2: # List all the sales
       return see_sales()
   #elif opt == 3: # List all the sales filtered
   elif opt == 4: # List sales by payment type
        return salesbypayment() 
   elif opt == 5: # List sales according to billing
       return salesbilled()
   elif opt == 6: #List sales
       return see_sales()
   elif opt == 7: # See specific product information
    return specific_product()
   elif opt == 8: # List all the inventory
       return inventory()
   elif opt == 9: # List products according to the lab
       return products_bylab()
   elif opt == 10: #List products that are about to expire
        return about_to_expire()
   #elif opt == 10: # List all the sales according to the lab.
   elif opt == 12: # EXIT
      print("\033[31m You have exited Reports. \033[0m")
      return main()

   elif opt <= 0 or opt>=13: # Invalid value
      print ("\033[31m ERROR. This number doesn't belong to the options, enter a valid number. \033[0m")
      print(" ")
      return submenureports()

# MAIN PROGRAM
print("\n")
print ("\033[32m W e l c o m e    t o   S a n    P a b l o   P h a r m a c y \033[0m".center(100,"-"))
main()