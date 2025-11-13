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

## ⚙️ How to Run the Project

1. **Generate Data**
   ```bash
   python generate_data.py
