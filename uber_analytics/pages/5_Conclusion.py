import streamlit as st

st.markdown("""
<style>
.conclusion-card {
    background-color: #0F1C2E;   /* deep blue instead of grey */
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 16px;
    border-left: 4px solid #4FC3F7;  /* accent highlight */
    box-shadow: 0px 6px 18px rgba(0,0,0,0.25);
}
.card-title {
    color: #81D4FA;   /* soft cyan */
    font-size: 18px;
    font-weight: 600;
}
.card-text {
    color: #E3F2FD;   /* off-white for readability */
    font-size: 15px;
    line-height: 1.6;
}
.kpi {
    font-weight: 600;
    color: #4FC3F7;   /* highlight KPIs */
}
</style>
""", unsafe_allow_html=True)


st.title("📌 Conclusion & Insights")

# Overall Conclusion
st.markdown("""
<div class="conclusion-card">
    <div class="card-title">🚖 Overall Conclusion</div>
    <div class="card-text">
        The analysis of Uber ride data reveals strong demand with
        <span class="kpi">2100 total bookings</span> and
        <span class="kpi">₹9.7 Lakh</span> in total revenue.
        However, a substantial number of cancellations and incomplete rides
        indicate the need for better operational efficiency, especially during peak hours.
    </div>
</div>
""", unsafe_allow_html=True)

# Key Insights
insights = [
    ("📊 KPI Performance", "Only 1.3k out of 2.1k bookings were completed, showing scope for improving ride fulfillment."),
    ("💳 Payment Preference", "UPI is the most commonly used payment mode, highlighting user preference for digital payments."),
    ("🚗 Travel Mode", "Auto is the most popular mode of transport, especially for short-distance city travel."),
    ("⏰ Peak Demand", "Monday afternoons and evenings experience the highest ride demand."),
    ("❌ Cancellations", "Higher driver pickup time leads to increased cancellations, most of which are driver-initiated.")
]

for title, text in insights:
    st.markdown(f"""
    <div class="conclusion-card">
        <div class="card-title">{title}</div>
        <div class="card-text">{text}</div>
    </div>
    """, unsafe_allow_html=True)

st.success(
    "📈 Improving driver availability and reducing pickup time during peak hours can significantly lower cancellations and increase customer satisfaction."
)
