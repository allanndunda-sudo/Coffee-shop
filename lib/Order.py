from Customer import Customer
from Coffee import Coffee


class Order:
    all = []
    def __init__(self,customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self.customer
    @customer.setter  
    def customer(self, value):
        if not isinstance(value, str):
            raise ValueError("Customer name must be a string")
        
        self.customer = value
    @property
    def coffee(self):
        return self.coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string")
        
        self.coffee = value
    
    @property
    def price(self):
        return self.price
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        
        if (1 <= value <= 10.0) is False:
            raise ValueError("Price must be between 1 and 10.0")
        
        self._price = value