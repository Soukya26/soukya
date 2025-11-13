# 🧠 Diligent Task — E-commerce Data Analysis

## 📌 Overview
This project simulates an **e-commerce database system** to demonstrate data generation, storage, and SQL-based analytics.  
It was developed as part of a **Diligent Data Analytics task** using Python and SQLite.

---

## 🧰 Tools & Technologies
- **Python** (pandas, sqlite3)
- **SQLite**
- **CSV files**
- **VS Code / Jupyter Notebook**

---

## 🗂️ Project Files
| File | Description |
|------|--------------|
| `generate_data.py` | Generates random customer, product, order, and payment data |
| `load_to_sqlite.py` | Loads generated CSV files into an SQLite database |
| `query.py` | Runs SQL queries joining multiple tables |
| `ecommerce.db` | The SQLite database created from CSV data |
| `customers.csv`, `orders.csv`, `order_items.csv`, `products.csv`, `payments.csv` | Sample data files used for analysis |

---
---

## 🧠 Prompts Used

### 1️⃣ Prompt to Generate Synthetic E-commerce Data
> “Generate synthetic e-commerce data for around 5 tables — customers, products, orders, order_items, and payments.  
> Each table should have realistic columns (like customer_id, name, email, product_id, order_date, amount, etc.).  
> Save each table as a CSV file for further analysis.”

### 2️⃣ Prompt to Load Data into SQLite Database
> “Write Python code to read multiple CSV files (customers, products, orders, order_items, payments) using pandas  
> and load them into an SQLite database called `ecommerce.db`.  
> Each CSV should become a corresponding table in the database.”

### 3️⃣ Prompt to Generate SQL Query for Analysis
> “Write a SQL query that joins all the tables (orders, customers, order_items, products, payments)  
> to display combined e-commerce insights such as customer name, product name, order date, quantity,  
> payment method, and payment status — limited to 10 rows.”

---

✅ These prompts were executed in **Cursor IDE** to create, load, and query the data successfully.


## ⚙️ How to Run the Project

1. **Generate Data**
   ```bash
   python generate_data.py
