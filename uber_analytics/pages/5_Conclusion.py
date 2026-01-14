import streamlit as st

st.markdown("""
<style>
.conclusion-card {
    background-color: #73C2FF;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 16px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
}
.card-title {
    color: #1f4e79;
    font-size: 18px;
    font-weight: 600;
}
.card-text {
    color: #2f2f2f;
    font-size: 15px;
    line-height: 1.6;
}
.kpi {
    font-weight: 600;
    color: #0b5394;
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
        <span class="kpi">1.5 lakh total bookings</span> and
        <span class="kpi">₹7.2 Crore</span> in total revenue.
        However, a substantial number of cancellations and incomplete rides
        indicate the need for better operational efficiency, especially during peak hours.
    </div>
</div>
""", unsafe_allow_html=True)

# Key Insights
insights = [
    ("📊 KPI Performance", "Only 93k out of 1.5 lakh bookings were completed, showing scope for improving ride fulfillment."),
    ("💳 Payment Preference", "UPI is the most commonly used payment mode, highlighting user preference for digital payments."),
    ("🚗 Travel Mode", "Auto is the most popular mode of transport, especially for short-distance city travel."),
    ("⏰ Peak Demand", "Evenings—particularly Monday and Saturday—experience the highest ride demand."),
    ("❌ Cancellations", "Higher driver pickup time leads to increased cancellations, most of which are driver-initiated."),
    ("⭐ Service Quality", "Go Mini shows higher rating variation, indicating potential quality improvement areas.")
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
