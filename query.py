import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('ecommerce.db')

# SQL query joining multiple tables
query = """
SELECT 
    c.name AS customer_name,
    p.product_name,
    o.order_date,
    oi.quantity,
    pay.payment_method,
    pay.payment_status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN payments pay ON o.order_id = pay.order_id
LIMIT 10;
"""

# Run query and load result into dataframe
df = pd.read_sql_query(query, conn)
print("✅ Sample Joined Output:")
print(df)

conn.close()
