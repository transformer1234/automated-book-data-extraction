import pandas as pd
import os

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def clean_data():
    input_path = "./data/raw/books_raw.csv"
    output_dir = "./data/processed"
    output_path = f"{output_dir}/books_clean.csv"

    if not os.path.exists(input_path):
        raise FileNotFoundError("Raw file not found. Run scraper.py first.")

    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(input_path)

    # Convert rating text to numeric
    df["rating"] = df["rating"].map(RATING_MAP)

    # Sort data (optional)
    df = df.sort_values(by="price", ascending=False)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")


if __name__ == "__main__":
    clean_data()
