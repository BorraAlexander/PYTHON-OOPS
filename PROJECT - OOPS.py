class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
        self.you_save = price - deal_price 
    
    def get_deal_price(self):
        return self.deal_price
    
    def display_product_details(self):
        print("name : {}".format(self.name))
        print("price: {}".format(self.price))
        print("deal_price: {}".format(self.deal_price))
        print("rating : {}".format(self.rating))
        print("you_save : {}".format(self.you_save))

class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, rating, warrenty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warrenty_in_months = warrenty_in_months 
    
    def display_product_details(self):
        super().display_product_details()
        print("Warrenty : {}".format(self.warrenty_in_months))
        
class GroceryItem(Product):
    
    def __init__(self, name, price, deal_price, rating, expiry_in_days):
        super().__init__(name, price, deal_price, rating)
        self.expiry_in_days = expiry_in_days 
    
    def display_product_details(self):
        super().display_product_details()
        print("Expiry : {}".format(self.expiry_in_days))
    
class Laptop(ElectronicItem):
    def __init__(self, name, price, deal_price, rating, warrenty_in_months, ram, storage):
        super().__init__(name, price, deal_price, rating, warrenty_in_months)
        self.ram = ram
        self.storage = storage 
    
    def display_product_details(self):
        super().display_product_details()
        print("Ram  : {}".format(self.ram))
        print("Storage  : {}".format(self.Storage))
 
class Order:
    delivery_charges = {
        "normal":10,
        "prime_users":100
    }
    
    def __init__(self, delivery_method, address):
        self.items_in_cart = []
        self.delivery_method=delivery_method
        self.address=address 
    
    def add_items(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)
        
    def display_order_details(self):
        print("Delivery Method : {}".format(self.delivery_method))
        print("delivery Address : {}".format(self.address))
        print("Products")
        print("------------------------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            print("") 
        print("------------------------")
        total_bill = self.total_bill() 
        print("Total Bill : {}".format(total_bill))
    
    def total_bill(self):
        total_bill = 0 
        for product,quantity in self.items_in_cart:
            total_bill = total_bill + product.get_deal_price()*quantity 
        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        total_bill = total_bill + order_delivery_charges
        return total_bill
    
    @classmethod 
    def update_delivry_charges(cls, delivery_method, charges):
        cls.delivery_charges[delivery_method] = charges
        
    @staticmethod
    def greet():
        print("Thank you for purchesing, Visit again..")
        
Tv = ElectronicItem("Samsung", 36700, 36000, 4.8, "24 Months")
Milk = GroceryItem("Milk", 400, 370, 4.5, "best Before 24 hrs")
        
my_order = Order("prime_users", "badvel")
my_order.add_items(Tv, 1)
my_order.add_items(Milk, 2)
Order.update_delivry_charges("prime_users", 50)
my_order.display_order_details()
my_order.greet()

#lenova = Laptop("Lenova 678 modal", 67890, 65000, 4.9, "36 months", "64 BG", "1Tb SSD")
#lenova.display_product_details()