from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "processed"

orders = pd.read_csv(DATA_DIR / "orders_clean.csv")

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Monthly orders
monthly = (
    orders
    .groupby(orders["order_purchase_timestamp"].dt.to_period("M"))
    ["order_id"]
    .nunique()
    .reset_index()
)

monthly["order_purchase_timestamp"] = (
    monthly["order_purchase_timestamp"]
    .astype(str)
)

fig = px.line(
    monthly,
    x="order_purchase_timestamp",
    y="order_id",
    markers=True
)

fig.update_layout(
    template="simple_white",
    height=500,
    margin=dict(l=20, r=20, t=20, b=20),
    xaxis_title="Month",
    yaxis_title="Orders"
)

fig.update_traces(line_width=3)

st.plotly_chart(fig, use_container_width=True)

with st.expander("View Data"):
    st.dataframe(monthly, use_container_width=True)

st.subheader("Business Insights")

st.success("""
• Order volume closely follows revenue.

• Peak ordering months align with major shopping events.

• Stable order growth reflects customer demand.
""")    