from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "processed"

st.title("Product Categories")
st.caption("Revenue generated across product categories")

st.subheader("Overview")

st.write("""
This analysis identifies the highest-performing product categories based on
total revenue. Understanding category performance helps businesses optimize
inventory planning, pricing strategies, marketing investments, and product
portfolio decisions.
""")

# Load data
orders = pd.read_csv(DATA_DIR / "orders_clean.csv")
payments = pd.read_csv(DATA_DIR / "payments_clean.csv")
items = pd.read_csv(DATA_DIR / "order_items_clean.csv")
products = pd.read_csv(DATA_DIR / "products_clean.csv")
categories = pd.read_csv(DATA_DIR / "categories_clean.csv")

# Merge datasets
master = (
    orders
    .merge(payments, on="order_id")
    .merge(items, on="order_id")
    .merge(products, on="product_id")
    .merge(categories, on="product_category_name")
)

# Revenue by category
category = (
    master
    .groupby("product_category_name_english")["payment_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# KPI Cards
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Categories Analyzed", category.shape[0])

with c2:
    st.metric(
        "Top Category",
        category.iloc[0]["product_category_name_english"].replace("_", " ").title()
    )

with c3:
    st.metric(
        "Highest Revenue",
        f"R$ {category.iloc[0]['payment_value']:,.0f}"
    )

st.divider()

# Chart
fig = px.bar(
    category,
    x="payment_value",
    y="product_category_name_english",
    orientation="h",
    text_auto=".2s"
)

fig.update_layout(
    template="simple_white",
    height=600,
    margin=dict(l=20, r=20, t=20, b=20),
    xaxis_title="Revenue (R$)",
    yaxis_title=""
)

fig.update_yaxes(categoryorder="total ascending")

st.plotly_chart(fig, use_container_width=True)

st.subheader("Business Insights")

st.success(f"""
• **{category.iloc[0]['product_category_name_english'].replace('_',' ').title()}** is the highest revenue-generating category.

• Revenue is concentrated within a few product categories.

• High-performing categories should receive greater inventory allocation and marketing investment.

• Lower-performing categories may require promotional campaigns or portfolio optimization.
""")

with st.expander("View Processed Data"):
    st.dataframe(category, use_container_width=True)

csv = category.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Analysis",
    csv,
    "product_category_analysis.csv",
    "text/csv"
)

st.divider()

st.caption("""
RetainIQ • Product Performance Dashboard

Built using PostgreSQL • SQL • Python • Pandas • Plotly • Streamlit
""")