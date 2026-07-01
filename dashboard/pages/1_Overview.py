from pathlib import Path

import streamlit as st
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "processed"

orders = pd.read_csv(DATA_DIR / "orders_clean.csv")
payments = pd.read_csv(DATA_DIR / "payments_clean.csv")
customers = pd.read_csv(DATA_DIR / "customers_clean.csv")

orders_count = orders["order_id"].nunique()
customer_count = customers["customer_unique_id"].nunique()
revenue = payments["payment_value"].sum()

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Orders", f"{orders_count:,}")

with c2:
    st.metric("Customers", f"{customer_count:,}")

with c3:
    st.metric("Revenue", f"R$ {revenue:,.0f}")

st.divider()

st.subheader("About")

st.write("""
RetainIQ analyzes customer purchasing behavior using SQL,
PostgreSQL, Python, Cohort Analysis and RFM Segmentation.

The dashboard helps understand:

- Revenue trends
- Order trends
- Customer retention
- Customer segmentation
""")

st.divider()

st.subheader("Business Objective")

st.write("""
RetainIQ analyzes customer purchasing behavior using SQL, PostgreSQL,
Python, Cohort Analysis, and RFM Segmentation.

The dashboard helps businesses understand customer retention,
revenue trends, geographic performance, and high-value customer segments.
""")

st.subheader("Key Insights")

st.info("""
• Revenue exceeded R$16 Million

• Nearly 100,000 orders analyzed

• Over 96,000 unique customers

• Strong concentration of revenue from São Paulo

• Health & Beauty is the highest revenue category
""")

st.subheader("Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("""
    **Database**
    - PostgreSQL
    - SQL
    """)

with col2:
    st.write("""
    **Analysis**
    - Python
    - Pandas
    """)

with col3:
    st.write("""
    **Visualization**
    - Plotly
    - Streamlit
    """)

    st.divider()

st.caption("""
Dataset: Brazilian Olist E-Commerce Dataset

Period: 2016–2018

≈100K Orders
≈96K Customers
""")