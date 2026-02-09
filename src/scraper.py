import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def extract_book_data(soup):
    books = soup.find_all("article", class_="product_pod")
    book_list = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.replace("£", "")
        rating = book.p["class"][1]   # Example: "Three"
        stock = book.find("p", class_="instock availability").text.strip()
        link = book.h3.a["href"]
        full_link = "http://books.toscrape.com/catalogue/" + link

        book_list.append({
            "title": title,
            "price": float(price[1:]),
            "rating": rating,
            "stock": stock,
            "product_link": full_link
        })

    return book_list


def scrape_all_books():
    all_books = []
    total_pages = 50  # Books to Scrape has 50 pages

    for page in range(1, total_pages + 1):
        print(f"Scraping page {page}...")

        url = BASE_URL.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to load page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        page_books = extract_book_data(soup)
        all_books.extend(page_books)

    return all_books


def save_data_to_csv(data):
    os.makedirs("../data/raw", exist_ok=True)  # Ensure folder exists
    df = pd.DataFrame(data)
    df.to_csv("../data/raw/books_raw.csv", index=False)
    print("\nSaved scraped data to data/raw/books_raw.csv")


if __name__ == "__main__":
    print("Starting scraper...\n")
    books = scrape_all_books()
    save_data_to_csv(books)
    print("\nScraping complete!")
