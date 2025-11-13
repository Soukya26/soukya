# generate_data.py
import pandas as pd
from faker import Faker
import random

fake = Faker()

# Customers
customers = pd.DataFrame({
    'customer_id': range(1, 21),
    'name': [fake.name() for _ in range(20)],
    'email': [fake.email() for _ in range(20)],
    'city': [fake.city() for _ in range(20)]
})
customers.to_csv('customers.csv', index=False)

# Products
products = pd.DataFrame({
    'product_id': range(1, 11),
    'product_name': [fake.word() for _ in range(10)],
    'category': [random.choice(['Electronics','Clothing','Books']) for _ in range(10)],
    'price': [round(random.uniform(10, 500), 2) for _ in range(10)]
})
products.to_csv('products.csv', index=False)

# Orders
orders = pd.DataFrame({
    'order_id': range(1, 31),
    'customer_id': [random.choice(customers['customer_id']) for _ in range(30)],
    'order_date': [fake.date_this_year() for _ in range(30)],
    'total_amount': [round(random.uniform(50, 1000), 2) for _ in range(30)]
})
orders.to_csv('orders.csv', index=False)

# Order Items
order_items = pd.DataFrame({
    'order_id': [random.choice(orders['order_id']) for _ in range(50)],
    'product_id': [random.choice(products['product_id']) for _ in range(50)],
    'quantity': [random.randint(1, 5) for _ in range(50)]
})
order_items.to_csv('order_items.csv', index=False)

# Payments
payments = pd.DataFrame({
    'payment_id': range(1, 31),
    'order_id': orders['order_id'],
    'payment_method': [random.choice(['UPI','Card','COD']) for _ in range(30)],
    'payment_status': [random.choice(['Success','Pending','Failed']) for _ in range(30)]
})
payments.to_csv('payments.csv', index=False)
