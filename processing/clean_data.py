import pandas as pd

def clean_data():
    df = pd.read_csv("data/raw/products.csv")
    #Clean Price
    df["price"] = df["price"].astype(str)
    df["price"] = df["price"].str.replace("Â£", "", regex=False)
    df["price"] = df["price"].str.replace("£", "", regex=False)
    df["price"] = df["price"].str.strip()

    # Convert to float
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["rating"] = df["rating"].map(rating_map)
    # Handling Missing Values

    df = df.dropna(subset=["name"])   
    # df["price"].fillna(0, inplace=True)
    # df["rating"].fillna(0, inplace=True)

    df["price"] = df["price"].fillna(0)
    df["rating"] = df["rating"].fillna(0)

    #Standardization
    df["name"] = df["name"].str.strip()

    # Adding Timestamp
    df["scraped_at"] = pd.Timestamp.now()

    df = df.drop_duplicates()

    df.to_csv("data/cleaned/products_cleaned.csv", index=False)

    print("Data cleaned successfully.")
    print(df.head())


if __name__ == "__main__":
    clean_data()