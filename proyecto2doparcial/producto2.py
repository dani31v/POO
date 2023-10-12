import os
import platform

class Product:
    count = 0

    def __init__(self, i = "", n = "", lab = "", iva = False):
        self.Id = Product.count
        Product.count += 1
        self.Name = n
        self.Laboratory = lab
        self.Iva = iva
        self.batches = []

    def printProductData(self):
        print(f"{self.Id} - {self.Name} - {self.Laboratory} - {self.Iva} -")
        for temporal_batch in self.batches:
            print(f"SKU: {temporal_batch.sku}")
            print(f"Presentation: {temporal_batch.presentation}")
            print(f"Cost: {temporal_batch.cost_value}")
            print(f"Price: {temporal_batch.price_value}")
            print(f"Expiration Date: {temporal_batch.exp_year}-{temporal_batch.exp_month}-{temporal_batch.exp_day}")
            print(f"Stock: {temporal_batch.stock}")
            print()

    def add_batches(self,batch):
      self.batches.append(batch)

    def update_batch(self, product_name, batch_id, new_stock):
        for product in self.products:
            if product.name == product_name:
                for batch in product.batches:
                    if batch.id == batch_id:
                        batch.stock = new_stock
                        print(f"Batch {batch_id} for product {product_name} has been updated with new stock: {new_stock}")
                        break
                    else:
                        print(f"Batch {batch_id} for product {product_name} not found.")
                        break
            else:
                print(f"Product {product_name} not found.")


class ProductBatches:
   
    def __init__(self, sk = 0, pres = "", cost = 0.0, price = 0.0, year = " ", month = " ", day = " ", st = 0):
        self.sku = sk
        self.presentation = pres
        self.cost_value = cost
        self.price_value = price
        self.exp_year = year
        self.exp_month = month
        self.exp_day = day
        self.stock = st
        
        
class Venta(Product):
    count = 0
    def __init__ (self,ord_num = 0, subtotal = 0.0, taxes = 0.0, total = 0.0, payment = "", billed = False):
        Venta.count += 1
        self.stock = 0
        self.order_number = Venta.count
        self.name= ""
        self.order_date = ""
        self.items_sold = []
        self.subtotal = subtotal
        self.taxes_amount = taxes
        self.total = total
        self.payment_type = payment
        self.is_billed = billed
        
    def printProductSale(self):
        print(f"{self.order_number}.-")
        print(f"Date: {self.order_date}")
        print(f"Name: {self.name}")
        print(f"Qty: {self.items_sold}")
        
    
        #- {self.subtotal}- {self.total} - {self.payment_type} - {self.is_billed } ")
    
class Company:
    def __init__(self, cn = ""):
        self.name = cn
        self.productList = []
        self.batchesList = []
        self.salesList = []
        
    def add_product(self, product):
        self.productList.append(product)
    
    def show_productList(self):
        for product in self.productList:
            product.printProductData()
            print()
        
    def add_batches(self, bacth):
        self.batchesList.append(bacth)
    def add_sales(self,ventas):
        self.salesList.append(ventas)
    def show_salesList(self):
        for venta in self.salesList:
            venta.printProductSale()
        print()
    

   

    


        