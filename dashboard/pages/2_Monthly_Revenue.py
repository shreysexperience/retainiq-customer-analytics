from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "processed"

orders = pd.read_csv(DATA_DIR / "orders_clean.csv")
payments = pd.read_csv(DATA_DIR / "payments_clean.csv")

# Convert datetime
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Merge datasets
master = orders.merge(payments, on="order_id")

# Calculate monthly revenue
monthly = (
    master
    .groupby(master["order_purchase_timestamp"].dt.to_period("M"))["payment_value"]
    .sum()
    .reset_index()
)

monthly["order_purchase_timestamp"] = (
    monthly["order_purchase_timestamp"]
    .astype(str)
)

# Plot
fig = px.line(
    monthly,
    x="order_purchase_timestamp",
    y="payment_value",
    markers=True
)

fig.update_layout(
    template="simple_white",
    height=500,
    margin=dict(l=20, r=20, t=20, b=20),
    xaxis_title="Month",
    yaxis_title="Revenue (R$)"
)

fig.update_traces(line_width=3)

# Show chart
st.plotly_chart(fig, use_container_width=True)

# Optional table
with st.expander("View Data"):
    st.dataframe(monthly, use_container_width=True)

st.subheader("Business Insights")

st.success("""
• Revenue shows consistent growth.

• Sales increase during promotional months.

• Seasonal peaks indicate higher customer activity.

• Business can plan inventory around high-demand periods.
""")

with st.expander("View Monthly Revenue Table"):
    st.dataframe(monthly, use_container_width=True)

st.download_button(
    "Download Revenue Data",
    monthly.to_csv(index=False),
    "monthly_revenue.csv",
    "text/csv"
)