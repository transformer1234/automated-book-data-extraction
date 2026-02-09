import streamlit as st
import pandas as pd
import plotly.express as px

DATA_PATH = "../data/processed/books_clean.csv"

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

st.title("📚 Books Dashboard — Books to Scrape")
st.write("Interactive dashboard built with **Streamlit** and **Plotly**.")

# -----------------------------
# Search Feature
# -----------------------------
st.header("🔍 Search Books by Title")
search_query = st.text_input("Enter a keyword:")

if search_query:
    filtered = df[df["title"].str.contains(search_query, case=False)]
    if len(filtered) == 1:
        st.write(f"Found {len(filtered)} book:")
    else:
        st.write(f"Found {len(filtered)} books:")
    st.dataframe(filtered)
else:
    st.write("Type a keyword to search.")

st.markdown("---")

# -----------------------------
# Price Distribution
# -----------------------------
st.header("💰 Price Distribution of Books")

fig_price = px.histogram(df, x="price", nbins=30)
fig_price.update_layout(xaxis_title="Price (£)", yaxis_title="Count")

st.plotly_chart(fig_price)

st.markdown("---")

# -----------------------------
# Rating Distribution
# -----------------------------
st.header("⭐ Rating Distribution")

fig_rating = px.bar(
    df["rating"].value_counts().sort_index(),
    labels={"index": "Rating", "value": "Count"},
)
st.plotly_chart(fig_rating)

st.markdown("---")

# -----------------------------
# Average Price by Rating
# -----------------------------
st.header("📈 Average Price by Rating")

avg_price = df.groupby("rating")["price"].mean().reset_index()

fig_avg = px.line(avg_price, x="rating", y="price", markers=True)
fig_avg.update_layout(xaxis_title="Rating", yaxis_title="Average Price (£)")

st.plotly_chart(fig_avg)

st.markdown("---")

# -----------------------------
# Top 20 Most Expensive Books
# -----------------------------
st.header("🏆 Top 20 Most Expensive Books")

top20 = df.sort_values("price", ascending=False).head(20)
fig_top20 = px.bar(
    top20,
    x="title",
    y="price",
    labels={"title": "Book Title", "price": "Price (£)"},
)
fig_top20.update_layout(xaxis_tickangle=45)

st.plotly_chart(fig_top20)
