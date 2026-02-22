# 📚 Books to Scrape — Web Scraping & Data Dashboard Project

A complete end-to-end **data science project** that scrapes book data from  
[Books to Scrape](http://books.toscrape.com), cleans the dataset, and builds an **interactive dashboard** using **Streamlit + Plotly**.

This project demonstrates skills in:
- Web scraping  
- Data cleaning & preprocessing  
- Exploratory data analysis  
- Dashboard development

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- streamlit, plotly
- beautifulsoup4

## How to run this project
### Dependencies
```bash
pip install -r requirements.txt
```
### Data extraction
```bash
python src/scraper.py
```
### Data cleaning
```bash
python src/clean_data.py
```
### Dashboard
```bash
streamlit run src/dashboard.py
```