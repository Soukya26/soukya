import sqlite3
import pandas as pd

# Connect to SQLite DB (it will create one if not exists)
conn = sqlite3.connect('ecommerce.db')

# List of CSVs to load
csv_files = ['customers.csv', 'products.csv', 'orders.csv', 'order_items.csv', 'payments.csv']

for file in csv_files:
    df = pd.read_csv(file)
    table_name = file.split('.')[0]
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Loaded {file} into table {table_name}")

conn.close()
print("✅ All files loaded successfully into ecommerce.db")
