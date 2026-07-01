from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "processed"

st.title("Customer Intelligence")
st.caption("RFM Analysis")

st.subheader("Overview")

st.write("""
Customers are segmented using the RFM model:

• Recency
• Frequency
• Monetary Value

This helps identify high-value customers, customers at risk,
and opportunities for personalized marketing campaigns.
""")

rfm = pd.read_csv(DATA_DIR / "customer_segments.csv")

segment = (
    rfm["Segment"]
    .value_counts()
    .reset_index()
)

segment.columns = [
    "Segment",
    "Customers"
]

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Customers",
        f"{rfm.shape[0]:,}"
    )

with c2:
    st.metric(
        "Segments",
        segment.shape[0]
    )

with c3:
    st.metric(
        "Largest Segment",
        segment.iloc[0]["Segment"]
    )

st.divider()

fig = px.bar(
    segment,
    x="Segment",
    y="Customers",
    text_auto=True
)

fig.update_layout(
    template="simple_white",
    height=500,
    margin=dict(l=20,r=20,t=20,b=20)
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Segment Interpretation")

st.info("""
🏆 Champions
Highest-value customers with frequent purchases.

❤️ Loyal Customers
Consistent repeat buyers.

🌱 Potential Loyalists
Customers likely to become loyal.

⚠️ At Risk
Customers showing reduced activity.

❌ Lost Customers
Inactive customers requiring win-back strategies.
""")

st.subheader("Business Recommendations")

st.success("""
• Reward Champions with exclusive loyalty benefits.

• Upsell Loyal Customers using personalized offers.

• Convert Potential Loyalists with targeted campaigns.

• Re-engage At Risk customers through discounts.

• Win back Lost Customers using email marketing and promotional incentives.
""")

with st.expander("View Customer Segments"):
    st.dataframe(rfm, use_container_width=True)

csv = rfm.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Segmentation",
    csv,
    "customer_segments.csv",
    "text/csv"
)

st.divider()

st.caption("""
RetainIQ • Customer Segmentation Dashboard

Built using SQL • PostgreSQL • Python • RFM Analysis
""")