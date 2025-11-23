from Order import Order

class Coffee:
    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name
    
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        
        if not (1 <= len(value) <= 3):
            raise ValueError("Name must be between 1 and 3 characters long")
        self.name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)