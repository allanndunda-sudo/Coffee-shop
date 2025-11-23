from Order import Order
from Coffee import Coffee

class Customer:
    def __init__(self, name):
        self.name = name
        

    def name(self):
        return self.name
    
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters long")
        self.name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):

        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee class")
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        
        new_order = Order(self, coffee, price)
        return new_order
    
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee class")
        coffee_orders = [order for order in Order.all if order.coffee == coffee]

        if not coffee_orders:
            return None
        customer_totals = {}
        for order in coffee_orders:
            customer_totals[order.customer] = customer_totals.get(order.customer, 0) + order.price

        most_spent_customer = max(customer_totals, key=customer_totals.get)
        return most_spent_customer