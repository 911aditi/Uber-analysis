import streamlit as st
import pandas as pd
st.markdown("<h1 style='color:white; background-color:black; text-align: center; border:2 px dashed black;'>Uber Analysis Dashboard - Delhi NCR(2024)</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvaTq0VuKb4rMZ9qdjHURATsyJ-g6YI9ykYQ&s", width=300)

st.markdown("<p style='color:white; text-align:center; font-size:18px'>Exploring 1000+ Uber ride records from Delhi NCR to understand peak travel hours, popular vehicle types, and ride status trends. </p>", unsafe_allow_html=True)

st.subheader("🎯 Project Objectives")

st.write("""
- Identify daily booking and customer demand trends
- Analyze which payment methods are mostly used
- Examine vehicle type popularity and ride distance distribution
- Explore booking value trends and time-of-day demand patterns
""")

st.subheader("📈Visualizations Included")

st.write("""
- **Bar Chart:** Booking Status Distribution
- **Line Chart:** Daily Booking Trends
- **Heatmap:** Bookings by Time of Day vs Day of Week
- **Pie Chart:** Payment Method Share
- **Scatter Plots:** Booking Value vs Ride Distance
- **Box Plot:** Driver Ratings by Vehicle Type

""")
