import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(pages=3):
    results = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            name = book.h3.a["title"]

            try:
                price = book.find("p", class_="price_color").text
            except:
                price = None

            try:
                rating = book.p["class"][1]  # rating stored as class
            except:
                rating = None

            results.append({
                "name": name,
                "price": price,
                "rating": rating,
                "source": "books"
            })

        time.sleep(1)

    return results


def save_to_csv(data):
    keys = ["name", "price", "rating", "source"]

    with open("data/raw/products.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    data = scrape_books(pages=3)
    save_to_csv(data)
    print("Scraping completed successfully.")