# Coffee-shop
This is a simple Python object-oriented program that simulates a coffee ordering system.
It allows you to:

Create Customers and Coffees

Place Orders linking Customers to Coffees

Track spending and order history

Identify the most devoted customer (most money spent on a specific coffee)

Customer

Initialize with a name (1–15 characters)

Create orders with create_order(coffee, price)

View all orders with orders()

View unique coffees ordered with coffees()

Class method most_aficionado(coffee) returns the customer who spent the most on a coffee

Coffee

Initialize with a name (minimum 3 characters)

View all orders with orders()

View unique customers who ordered it with customers()

Order

Initialize with a Customer, Coffee, and price (1.0–10.0)

Validates input types and ranges