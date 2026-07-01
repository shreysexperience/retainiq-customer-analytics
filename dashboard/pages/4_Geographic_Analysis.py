from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "processed"

st.title("Geographic Analysis")
st.caption("Revenue distribution across Brazilian states")

st.subheader("Overview")

st.write("""
This analysis explores how revenue is distributed across Brazilian states.
It identifies the regions generating the highest sales and highlights where
customer demand is strongest, helping businesses prioritize regional
marketing and retention strategies.
""")

# Load data
orders = pd.read_csv(DATA_DIR / "orders_clean.csv")
payments = pd.read_csv(DATA_DIR / "payments_clean.csv")
customers = pd.read_csv(DATA_DIR / "customers_clean.csv")

# Merge datasets
master = (
    orders
    .merge(payments, on="order_id")
    .merge(customers, on="customer_id")
)

# Revenue by state
state = (
    master
    .groupby("customer_state")["payment_value"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

# KPIs
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("States Covered", state.shape[0])

with c2:
    st.metric("Highest Revenue State", state.iloc[0]["customer_state"])

with c3:
    st.metric(
        "Highest Revenue",
        f"R$ {state.iloc[0]['payment_value']:,.0f}"
    )

st.divider()

# Chart
fig = px.bar(
    state,
    x="customer_state",
    y="payment_value",
    text_auto=".2s"
)

fig.update_layout(
    template="simple_white",
    height=520,
    margin=dict(l=20, r=20, t=20, b=20),
    xaxis_title="Brazilian State",
    yaxis_title="Revenue (R$)"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Business Insights")

st.success(f"""
• **{state.iloc[0]['customer_state']}** generates the highest revenue.

• Revenue is concentrated in a small number of states.

• Understanding regional demand enables targeted marketing campaigns.

• High-performing regions can be prioritized for customer retention initiatives.
""")

with st.expander("View Processed Data"):
    st.dataframe(state, use_container_width=True)

csv = state.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Analysis",
    csv,
    "geographic_analysis.csv",
    "text/csv"
)