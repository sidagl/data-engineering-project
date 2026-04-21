import sqlite3
import pandas as pd

def store_data():
    conn = sqlite3.connect("database/products.db")

    df = pd.read_csv("data/cleaned/products_cleaned.csv")
    df.to_sql("products", conn, if_exists="replace", index=False)

    conn.commit()

    # ✅ ADD THIS PART (verification)
    test_df = pd.read_sql("SELECT * FROM products LIMIT 5", conn)
    print("\n📊 Sample data from DB:")
    print(test_df)

    conn.close()
    print("✅ Data stored in database successfully.")


if __name__ == "__main__":
    store_data()