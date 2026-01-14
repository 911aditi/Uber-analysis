import streamlit as st

st.markdown("""
### 🚕 Executive Summary
<strong>High demand exists, but cancellations during peak hours are limiting revenue potential.</strong>
""", unsafe_allow_html=True)

st.markdown("""
<div class="insight-card">
<h4>📉 Ride Fulfilment Issue</h4>
<p>A significant portion of users do not complete rides, indicating operational inefficiencies during high-demand periods.</p>
</div>

<div class="insight-card">
<h4>💳 Payment Behavior</h4>
<p>Users strongly prefer digital payments, reinforcing the importance of seamless UPI-based checkout experiences.</p>
</div>

<div class="insight-card">
<h4>🚗 Vehicle Preference</h4>
<p>Auto rides dominate short-distance travel, highlighting affordability and last-mile connectivity needs.</p>
</div>

<div class="insight-card">
<h4>⏰ Time-based Demand</h4>
<p>Evening hours experience peak demand, requiring better driver allocation and surge optimization.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.insight-card {
    background-color: #0f172a;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 16px;
    border-left: 4px solid #38bdf8;
}

.insight-card h4 {
    color: #7dd3fc;
    margin-bottom: 6px;
    font-size: 20px;
}

.insight-card p {
    color: #e5e7eb;
    font-size: 18px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

