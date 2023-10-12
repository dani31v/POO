from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QInputDialog, QMessageBox, QPlainTextEdit, QTableWidget, QTableWidgetItem, QInputDialog, QMessageBox, QDialog, QLabel
from PyQt6.QtCore import Qt
from models import *
import sys
import pandas as pd
from datetime import datetime, timedelta

class SalesFilterWindow(QDialog):
    def __init__(self, sales, inventory):
        super().__init__()
        self.setWindowTitle("Filtered Sales")
        self.setStyleSheet("background-color: #E8D9F7; color:  white and black ;")
        etiqueta = QLabel("San Pablo Pharmacy", self)
        etiqueta.setGeometry(50, 50, 200, 30)
        ancho = 800
        alto = 600
        self.resize(ancho, alto)
        self.sales = sales
        self.inventory = inventory
        
        # Add your UI elements and layout for the filtered sales window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
                
        # Example: Adding a label
        self.label = QLabel("Filtered Sales")
        self.layout.addWidget(self.label)

        self.sales_text_edit = QPlainTextEdit()
        self.layout.addWidget(self.sales_text_edit)
        self.sales_text_edit.setStyleSheet("background-color: white and black")
        
        # Add labels, table widgets, buttons, etc., as needed
        self.order_number_button = QPushButton("Order number")
        self.order_number_button.clicked.connect(self.order_number)
        self.layout.addWidget(self.order_number_button)
        self.order_number_button.setStyleSheet("background-color: white and black;color: #C7AAE2")

        self.order_date_button = QPushButton("Date")
        self.order_date_button.clicked.connect(self.order_date)
        self.layout.addWidget(self.order_date_button)
        self.order_date_button.setStyleSheet("background-color: white and black;color: #C7AAE2")

        self.order_month_button = QPushButton("Month")
        self.order_month_button.clicked.connect(self.order_month)
        self.layout.addWidget(self.order_month_button)
        self.order_month_button.setStyleSheet("background-color: white and black;color: #C7AAE2")

        self.order_year_button = QPushButton("Year")
        self.order_year_button.clicked.connect(self.order_year)
        self.layout.addWidget(self.order_year_button)
        self.order_year_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        

        self.order_name_button = QPushButton("Name")
        self.order_name_button.clicked.connect(self.order_name)
        self.layout.addWidget(self.order_name_button)
        self.order_name_button.setStyleSheet("background-color: white and black;color: #C7AAE2")

        self.payment_type_button = QPushButton("Payment Type")
        self.payment_type_button.clicked.connect(self.payment_type)
        self.layout.addWidget(self.payment_type_button)
        self.payment_type_button.setStyleSheet("background-color: white and black;color: #C7AAE2")

        self.order_bill_button = QPushButton("Bill")
        self.order_bill_button.clicked.connect(self.order_bill)
        self.layout.addWidget(self.order_bill_button)
        self.order_bill_button.setStyleSheet("background-color: white and black;color: #C7AAE2")

        self.laboratory_button = QPushButton("Laboratory")
        self.laboratory_button.clicked.connect(self.laboratory)
        self.layout.addWidget(self.laboratory_button)
        self.laboratory_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit)
        self.layout.addWidget(self.exit_button)
        self.exit_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
    def exit(self):
            self.close()
    
    def order_number(self):
        order_number, ok = QInputDialog.getInt(
            self, "Order Number", "Enter the order number:")
        if ok:
            sales = self.filter_sales_by_order_number(order_number)
            self.display_sales(sales)

    def filter_sales_by_order_number(self, order_number):
        filtered_sales = []
        for sale in self.sales:
            if sale.order_number == order_number:
                filtered_sales.append(sale)
        return filtered_sales

    def display_sales(self, sales):
        self.sales_text_edit.clear()
        for sale in sales:
            self.sales_text_edit.appendPlainText(f"Order Number: {sale.order_number}")
            self.sales_text_edit.appendPlainText(f"Date: {sale.date}")
            self.sales_text_edit.appendPlainText(f"Name: {sale.products}")
            self.sales_text_edit.appendPlainText(f"Amount: {sale.amount}")
            self.sales_text_edit.appendPlainText(f"Subtotal: {sale.subtotal}")
            self.sales_text_edit.appendPlainText(f"Total: {sale.total}")
            self.sales_text_edit.appendPlainText(f"Payment Type: {sale.payment_type}")
            self.sales_text_edit.appendPlainText(f"Billed: {sale.billed}")
            self.sales_text_edit.appendPlainText("\n")

    def order_date(self):
        date, ok = QInputDialog.getText(
            self, "Order Date", "Enter the order date (dd/mm/yyyy):")
        if ok:
            sales = self.filter_sales_by_date(date)
            self.display_sales(sales)


    def filter_sales_by_date(self, date):
        filtered_sales = []
        search_date = datetime.strptime(date, "%d/%m/%Y").date()
        for sale in self.sales:
            if sale.date == search_date:
                filtered_sales.append(sale)
        return filtered_sales

    def order_month(self):
        month, ok = QInputDialog.getInt(
            self, "Order Month", "Enter the order month (1-12):")
        if ok:
            sales = self.filter_sales_by_month(month)
            self.display_sales(sales)

    def filter_sales_by_month(self, month):
        filtered_sales = []
        for sale in self.sales:
            sale_month = sale.date.month
            if sale_month == month:
                filtered_sales.append(sale)
        return filtered_sales


    def order_year(self):
        year, ok = QInputDialog.getInt(
            self, "Order Year", "Enter the order year:")
        if ok:
            sales = self.filter_sales_by_year(year)
            self.display_sales(sales)

    def filter_sales_by_year(self, year):
        filtered_sales = []
        for sale in self.sales:
            sale_year = sale.date.year
            if sale_year == year:
                filtered_sales.append(sale)
        return filtered_sales
    
    def order_name(self):
        name, ok = QInputDialog.getText(
            self, "Order Name", "Enter the product name:")
        if ok:
            sales = self.filter_sales_by_name(name)
            self.display_sales(sales)

    def filter_sales_by_name(self, name):
        filtered_sales = []
        for sale in self.sales:
            if name.lower() in sale.products.lower():
                filtered_sales.append(sale)
        return filtered_sales

    def payment_type(self):
        payment_types = ['Cash', 'Card']  # Update with your payment types
        payment_type, ok = QInputDialog.getItem(
            self, "Payment Type", "Select payment type:", payment_types, 0, False)
        if ok:
            sales = self.filter_sales_by_payment_type(payment_type)
            self.display_sales(sales)

    def filter_sales_by_payment_type(self, payment_type):
        filtered_sales = []
        for sale in self.sales:
            if sale.payment_type.lower() == payment_type.lower():
                filtered_sales.append(sale)
        return filtered_sales

    def order_bill(self):
        options = ['Billed', 'Not Billed']  # Update with your bill options
        bill_status, ok = QInputDialog.getItem(
            self, "Order Bill", "Select bill status:", options, 0, False)
        if ok:
            sales = self.filter_sales_by_bill_status(bill_status)
            self.display_sales(sales)

    def filter_sales_by_bill_status(self, bill_status):
        filtered_sales = []
        for sale in self.sales:
            if (bill_status == 'Billed' and sale.billed) or (bill_status == 'Not Billed' and not sale.billed):
                filtered_sales.append(sale)
        return filtered_sales

    def laboratory(self):
        laboratory, ok = QInputDialog.getText(
            self, "Laboratory", "Enter the laboratory name:")
        if ok:
            sales = self.filter_sales_by_laboratory(laboratory)
            self.display_sales(sales)

    def filter_sales_by_laboratory(self, laboratory):
        filtered_sales = []
        for sale in self.sales:
            products = sale.products.split(", ")
            for product in products:
                if self.inventory[int(product) - 1].laboratory.lower() == laboratory.lower():
                    filtered_sales.append(sale)
                    break
        return filtered_sales

class ProductFilterWindow(QDialog):
    def __init__(self,inventory):
        super().__init__()
        self.setWindowTitle("Filtered Products")
        self.setStyleSheet("background-color: #E8D9F7; color:  white and black;")
        etiqueta = QLabel("San Pablo Pharmacy", self)
        etiqueta.setGeometry(50, 50, 200, 30)
        ancho = 800
        alto = 600
        self.resize(ancho, alto)
        self.inventory = inventory
        
        # Add your UI elements and layout for the filtered sales window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
                
        # Example: Adding a label
        self.label = QLabel("Filtered Products")
        self.layout.addWidget(self.label)
        
        self.prod_text_edit = QPlainTextEdit()
        self.layout.addWidget(self.prod_text_edit)
        self.prod_text_edit.setStyleSheet("background-color: white and black")
       
        
        # Add labels, table widgets, buttons, etc., as needed
        self.sku_button = QPushButton("SKU")
        self.sku_button.clicked.connect(self.sku)
        self.layout.addWidget(self.sku_button)
        self.sku_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.name_button = QPushButton("Name")
        self.name_button.clicked.connect(self.name)
        self.layout.addWidget(self.name_button)
        self.name_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.Laboratory_button = QPushButton("Laboratory")
        self.Laboratory_button.clicked.connect(self.laboratory)
        self.layout.addWidget(self.Laboratory_button)
        self.Laboratory_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.Presentation_button = QPushButton("Presentation")
        self.Presentation_button.clicked.connect(self.presentation)
        self.layout.addWidget(self.Presentation_button)
        self.Presentation_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.Expiration_button = QPushButton("Expiration date")
        self.Expiration_button.clicked.connect(self.expiration_date)
        self.layout.addWidget(self.Expiration_button)
        self.Expiration_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.soontoexpire_button = QPushButton("Products soon to expire")
        self.soontoexpire_button.clicked.connect(self.products_soon_to_expire)
        self.layout.addWidget(self.soontoexpire_button)
        self.soontoexpire_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit)
        self.layout.addWidget(self.exit_button)
        self.exit_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
    def exit(self):
            self.close()
    
        
    def sku(self):
        sku, ok = QInputDialog.getText(
            self, "SKU", "Enter the sku of the product:")
        if ok:
            products = self.filter_products_by_sku(sku)
            self.display_product(products)
           

    def filter_products_by_sku(self, sku):
        filtered_product = []
        for product in self.inventory:
            if product.sku == sku:
                filtered_product.append(product)
        return filtered_product
    
    def name(self):
        name, ok = QInputDialog.getText(
            self, "Name", "Enter the name of the product:")
        if ok:
            products = self.filter_products_by_name(name)
            self.display_product(products)
           

    def filter_products_by_name(self, name):
        filtered_product = []
        for product in self.inventory:
            if product.name == name:
                filtered_product.append(product)
        return filtered_product
    
    def laboratory(self):
        laboratory, ok = QInputDialog.getText(
            self, "Laboratory", "Enter the laboratory you want to search:")
        if ok:
            products = self.filter_products_by_lab(laboratory)
            self.display_product(products)
           

    def filter_products_by_lab(self, laboratory):
        filtered_product = []
        for product in self.inventory:
            if product.laboratory == laboratory:
                filtered_product.append(product)
        return filtered_product
    
    def presentation(self):
        presentation, ok = QInputDialog.getText(
            self, "Presentation", "Enter the presentation:")
        if ok:
            products = self.filter_products_by_presentation(presentation)
            self.display_product(products)
           
    def filter_products_by_presentation(self, presentation):
        filtered_product = []
        for product in self.inventory:
            if product.presentation == presentation :
                filtered_product.append(product)
        return filtered_product
    
    def expiration_date(self):
        expiration_date, ok = QInputDialog.getText(
            self, "Expirtaion Date", "Enter the date in format (DD/MM/YYYY):")
        if ok:
            products = self.filter_products_by_exp_date(expiration_date)
            self.display_product(products)
           
    def filter_products_by_exp_date(self, expiration_date):
        filtered_product = []
        exp_date = datetime.strptime(expiration_date, "%d/%m/%Y")
        for product in self.inventory:
            if product.expiration_date == exp_date :
                filtered_product.append(product)
        return filtered_product
    
    def products_soon_to_expire(self,expiration_date):
        filtered_product = []
        for product in self.inventory:
                if product.expiration_date <= datetime.now()+timedelta(days=60):
                    filtered_product.append(product)
                    self.display_product(filtered_product)

        

    def filter_products_soon_to_expire(self,expiration_date):
        filtered_product = []
        for product in self.inventory:
                if product.expiration_date <= datetime.now()+timedelta(days=60):
                    filtered_product.append(product)
        return filtered_product
    
    def display_product(self, inventory):
        self.prod_text_edit.clear()
        for product in inventory:
            self.prod_text_edit.appendPlainText(f"Sku: {product.sku}")
            self.prod_text_edit.appendPlainText(f"Name: {product.name}")
            self.prod_text_edit.appendPlainText(f"Presentation: {product.presentation}")
            self.prod_text_edit.appendPlainText(f"Laboratory: {product.laboratory}")
            self.prod_text_edit.appendPlainText(f"Stock: {product.stock}")
            self.prod_text_edit.appendPlainText(f"Cost Value: {product.cost_value}")
            self.prod_text_edit.appendPlainText(f"Sale Value: {product.sale_value}")
            self.prod_text_edit.appendPlainText(f"Expiration Date: {product.expiration_date}")
            self.prod_text_edit.appendPlainText(f"IVA : {product.iva}")
            self.prod_text_edit.appendPlainText("")




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product and Sales Management")
        self.setStyleSheet("background-color: #E8D9F7;")
        etiqueta = QLabel("San Pablo Pharmacy", self)
        etiqueta.setGeometry(0, 0, 200, 30)
        ancho = 800
        alto = 600
        self.resize(ancho, alto)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
    

        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)
        self.table_widget.setStyleSheet("background-color: white and black;")

        self.sales_table_widget = QTableWidget()
        self.layout.addWidget(self.sales_table_widget)
        self.sales_table_widget.setStyleSheet("background-color: white and black; ")

        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.clicked.connect(self.add_product)
        self.layout.addWidget(self.add_product_button)
        self.add_product_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.create_sale_button = QPushButton("Create sale")
        self.create_sale_button.clicked.connect(self.create_sale)
        self.layout.addWidget(self.create_sale_button)
        self.create_sale_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.show_all_products_button = QPushButton("Show all products")
        self.show_all_products_button.clicked.connect(self.show_all_products)
        self.layout.addWidget(self.show_all_products_button)
        self.show_all_products_button.setStyleSheet("background-color: white and black;color: #C7AAE2")

        self.show_all_sales_button = QPushButton("Show all sales")
        self.show_all_sales_button.clicked.connect(self.list_all_sales)
        self.layout.addWidget(self.show_all_sales_button)
        self.show_all_sales_button.setStyleSheet("background-color: white and black;color: #C7AAE2")

        self.show_sales_filtered_button = QPushButton("Show sales filtered")
        self.show_sales_filtered_button.clicked.connect(self.sales_filtered)
        self.layout.addWidget(self.show_sales_filtered_button)
        self.show_sales_filtered_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        self.show_products_filtered_button = QPushButton("Show products filtered")
        self.show_products_filtered_button.clicked.connect(self.products_filtered)
        self.layout.addWidget(self.show_products_filtered_button)
        self.show_products_filtered_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
        
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit)
        self.layout.addWidget(self.exit_button)
        self.exit_button.setStyleSheet("background-color: white and black;color: #C7AAE2")
        
    


        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.options.display.width = 0

        inventory_df = pd.read_excel(
            "DB/Inventory.xlsx", sheet_name="Inventory")
        sales_df = pd.read_excel("DB/Sales.xlsx", sheet_name="Sales")

        self.inventory = inventory_df.values.tolist()
        self.sales = sales_df.values.tolist()

        for i in range(len(self.inventory)):
            self.inventory[i] = Product(name=str(self.inventory[i][2]), presentation=self.inventory[i][3], laboratory=self.inventory[i][4],
                                        stock=self.inventory[i][5], cost_value=self.inventory[i][6], sale_value=self.inventory[i][7],
                                        expiration_date=self.inventory[i][8], iva=self.inventory[i][9])
        for i in range(len(self.sales)):
            self.sales[i] = Sale(order_number=self.sales[i][1], products=self.sales[i][3], amount=self.sales[i][4], subtotal=self.sales[i][5],
                                 total=self.sales[i][6], payment_type=self.sales[i][7], billed=self.sales[i][8])

    def add_product(self):
        name, ok = QInputDialog.getText(
            self, 'Add product', 'Please enter the product name:')
            
        if ok:
            presentation, ok = QInputDialog.getText(
                self, 'Add product', 'Please enter the product presentation:')
            if ok:
                laboratory, ok = QInputDialog.getText(
                    self, 'Add product', 'Please enter the laboratory:')
                if ok:
                    stock, ok = QInputDialog.getText(
                        self, 'Add product', 'Please enter the stock:')
                    if ok:
                        cost_value, ok = QInputDialog.getDouble(
                            self, 'Add product', 'Please enter the cost value:')
                        if ok:
                            sale_value, ok = QInputDialog.getDouble(
                                self, 'Add product', 'Please enter the sale value:')
                            if ok:
                                expiration_date, ok = QInputDialog.getText(
                                    self, 'Add product', 'Please enter the expiration date (dd/mm/yyyy):')
                                if ok:
                                    iva, ok = QInputDialog.getItem(
                                        self, 'Add product', 'The product has taxes?', ['y', 'n'], 0, False)
                                    if ok:
                                        if iva == "y":
                                            iva = True
                                        else:
                                            iva = False
                                        product = Product(name, presentation, laboratory, int(stock), float(
                                            cost_value), float(sale_value), expiration_date, iva)
                                        self.inventory.append(product)
                                        QMessageBox.information(
                                            self, 'Product added', 'Product added successfully!')
                                        self.show_all_products()  

    def create_sale(self):
        if len(self.inventory) == 0:
            QMessageBox.warning(
                self, 'No products', 'There are no products in the inventory, please add a product first.')
            return
        else:
            sales_bought = []

            self.show_all_products()
            order_number, ok = QInputDialog.getText(
                self, 'Create sale', 'Please enter the ids of the products to sell separated by comas:')
            if not ok:
                return
            order_number = order_number.split(",")
            products = []
            for order in order_number:
                products.append(self.inventory[int(order) - 1])

            for product in products:
                QMessageBox.information(
                    self, 'Product selected', f'Product selected: {product.name}')
                amount, ok = QInputDialog.getInt(
                    self, 'Create sale', 'Please enter the amount of the product to sell:')
                if not ok or amount > product.stock:
                    QMessageBox.warning(
                        self, 'Not enough stock', 'There is not enough stock of the product.')
                    return
                product.stock -= amount
                subtotal = product.sale_value * amount
                if product.iva:
                    total = subtotal * 1.16
                else:
                    total = subtotal
                payment_type, ok = QInputDialog.getText(
                    self, 'Create sale', 'Please enter the payment type (cash/card):')
                if not ok:
                    return
                billed, ok = QInputDialog.getItem(
                    self, 'Create sale', 'Was the order billed?', ['y', 'n'], 0, False)
                if not ok:
                    return
                order_number = len(self.sales) + 1
                sale = Sale(order_number, product, amount,
                            subtotal, total, payment_type, billed == 'y')
                sales_bought.append(sale)
                QMessageBox.information(self, 'Sale created', 'Sale created successfully!\n' +
                                        f'Total to pay: {total}\n' +
                                        f'Total taxes: {total - subtotal}')

            products_names = ', '.join([product.name for product in products])
            amounts = ', '.join([str(sale.amount) for sale in sales_bought])
            subtotal = sum([sale.subtotal for sale in sales_bought])
            total = sum([sale.total for sale in sales_bought])
            payment_type = sales_bought[0].payment_type
            billed = sales_bought[0].billed

            final_sale = Sale(len(self.sales) + 1,
                              products_names,
                              amounts,
                              subtotal,
                              total,
                              payment_type,
                              billed)

            self.sales.append(final_sale)
            self.show_all_products()
    def exit(self):
            self.close()

    def show_all_products(self):
        products = []
        for product in self.inventory:
            products.append(
                [product.sku, product.name, product.presentation, product.laboratory, product.stock, product.cost_value,
                 product.sale_value, product.expiration_date, product.iva])

        self.table_widget.setRowCount(len(products))
        self.table_widget.setColumnCount(9)
        self.table_widget.setHorizontalHeaderLabels(["sku", "name", "presentation", "laboratory", "stock", "cost_value", "sale_value",
                                                     "expiration_date", "iva"])
    

        for i, product in enumerate(products):
            for j, field in enumerate(product):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(field)))
               
                

    def list_all_sales(self):
        sales_data_frame = []
        for sale in self.sales:
            sales_data_frame.append(
                [sale.order_number, sale.date, sale.products, sale.amount, sale.subtotal, sale.total,
                 sale.payment_type, sale.billed])

        self.sales_table_widget.setRowCount(len(sales_data_frame))
        self.sales_table_widget.setColumnCount(8)
        self.sales_table_widget.setHorizontalHeaderLabels(["order_number", "date", "name", "amount",
                                                           "subtotal", "total", "payment_type", "billed"])

        for i, sale in enumerate(sales_data_frame):
            for j, field in enumerate(sale):
                self.sales_table_widget.setItem(
                    i, j, QTableWidgetItem(str(field)))

    def list_all_products(self):
        products_df = []
        for product in self.inventory:
            products_df.append(
                [product.sku, product.name, product.presentation, product.laboratory, product.stock, product.cost_value,
                 product.sale_value, product.expiration_date, product.iva])

        self.products_table_widget.setRowCount(len(products_df))
        self.products_table_widget.setColumnCount(9)
        self.products_table_widget.setHorizontalHeaderLabels(["sku", "name", "presentation", "laboratory", "stock", "cost_value", "sale_value",
                                                              "expiration_date", "iva"])

        for i, product in enumerate(products_df):
            for j, field in enumerate(product):
                self.products_table_widget.setItem(
                    i, j, QTableWidgetItem(str(field)))

    def sales_filtered(self):
        sales_filter_window = SalesFilterWindow(self.sales, self.inventory)
        sales_filter_window.exec() 
        
    def products_filtered(self):
        products_filter_window = ProductFilterWindow(self.inventory)
        products_filter_window.exec() 



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

