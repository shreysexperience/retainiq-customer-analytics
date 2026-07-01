from pathlib import Path

import streamlit as st
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "processed"
IMAGE_DIR = BASE_DIR / "images"

st.title("Customer Retention")
st.caption("Cohort Analysis of Customer Retention")

st.subheader("Overview")

st.write("""
Customer Cohort Analysis measures how many customers return to make
another purchase after their first order.

This helps evaluate customer loyalty and long-term retention by tracking
repeat purchasing behavior across monthly cohorts.
""")

retention = pd.read_csv(DATA_DIR / "cohort_retention.csv")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Cohorts", retention.shape[0])

with c2:
    st.metric("Months Tracked", retention.shape[1]-1)

with c3:
    st.metric("Retention Metric", "Monthly")

st.divider()

st.subheader("Retention Heatmap")

st.image(
    IMAGE_DIR / "cohort_heatmap.png",
    use_container_width=True
)

st.subheader("Business Insights")

st.success("""
• Customer retention declines after the first purchase.

• The largest drop occurs during the first few months.

• Improving repeat purchases can significantly increase customer lifetime value.

• Loyalty campaigns and personalized recommendations may improve retention.
""")

with st.expander("View Cohort Table"):
    st.dataframe(retention, use_container_width=True)

csv = retention.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Cohort Data",
    csv,
    "cohort_retention.csv",
    "text/csv"
)

st.divider()

st.caption("""
RetainIQ • Customer Retention Dashboard

Built using PostgreSQL • SQL • Python • Cohort Analysis
""")