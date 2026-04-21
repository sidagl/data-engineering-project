import pandas as pd

def clean_data():
    # Load raw data
    df = pd.read_csv("data/raw/products.csv")

    # -----------------------------
    # 1. Clean Price
    # -----------------------------
    # Remove weird encoding + currency symbols
    df["price"] = df["price"].astype(str)
    df["price"] = df["price"].str.replace("Â£", "", regex=False)
    df["price"] = df["price"].str.replace("£", "", regex=False)
    df["price"] = df["price"].str.strip()

    # Convert to float
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # -----------------------------
    # 2. Clean Ratings (text → number)
    # -----------------------------
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["rating"] = df["rating"].map(rating_map)

    # -----------------------------
    # 3. Handle Missing Values
    # -----------------------------
    df = df.dropna(subset=["name"])   # name is important
    # df["price"].fillna(0, inplace=True)
    # df["rating"].fillna(0, inplace=True)

    df["price"] = df["price"].fillna(0)
    df["rating"] = df["rating"].fillna(0)

    # -----------------------------
    # 4. Standardization
    # -----------------------------
    df["name"] = df["name"].str.strip()

    # -----------------------------
    # 5. Add Timestamp (important!)
    # -----------------------------
    df["scraped_at"] = pd.Timestamp.now()

    # -----------------------------
    # 6. Remove Duplicates
    # -----------------------------
    df = df.drop_duplicates()

    # -----------------------------
    # 7. Save Cleaned Data
    # -----------------------------
    df.to_csv("data/cleaned/products_cleaned.csv", index=False)

    print("✅ Data cleaned successfully.")
    print(df.head())


if __name__ == "__main__":
    clean_data()