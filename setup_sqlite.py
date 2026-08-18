import pandas as pd
import sqlite3

# 1. A robust, realistic dataset for testing complex AI SQL queries
data = {
    "transaction_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015],
    "customer_name": [
        "Emma Watson", "James Smith", "Olivia Johnson", "Emma Watson", "William Brown",
        "Sophia Davis", "James Smith", "Lucas Miller", "Olivia Johnson", "Mia Wilson",
        "William Brown", "Alexander Taylor", "Emma Watson", "Mia Wilson", "James Smith"
    ],
    "product_category": [
        "Electronics", "Home & Kitchen", "Electronics", "Clothing", "Electronics",
        "Books", "Clothing", "Home & Kitchen", "Books", "Electronics",
        "Home & Kitchen", "Clothing", "Electronics", "Books", "Clothing"
    ],
    "amount": [1200.50, 45.99, 899.00, 120.00, 350.75, 25.50, 65.00, 150.25, 15.99, 999.99, 85.00, 55.50, 200.00, 32.00, 45.00],
    "purchase_date": [
        "2026-08-01", "2026-08-01", "2026-08-02", "2026-08-03", "2026-08-03",
        "2026-08-04", "2026-08-05", "2026-08-06", "2026-08-07", "2026-08-08",
        "2026-08-09", "2026-08-10", "2026-08-10", "2026-08-11", "2026-08-12"
    ]
}

df = pd.DataFrame(data)

# 2. Connect and write to the database
conn = sqlite3.connect("sales_data.db")
df.to_sql("transactions", conn, if_exists="replace", index=False)

# 3. Test that it worked
results = pd.read_sql("SELECT * FROM transactions LIMIT 5", conn)
print("Database 'sales_data.db' generated successfully with realistic test data!")
print("Here is a preview of the first 5 rows:")
print(results)

conn.close()