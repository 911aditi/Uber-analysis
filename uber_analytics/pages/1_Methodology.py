import streamlit as st
import pandas as pd
import os

st.title("Methodology")

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "cleaned_data.csv")
    return pd.read_csv(file_path)

df = load_data()

def abbreviate_number(num):
    if num >= 10**7:  # Crore
        return f"{num/10**7:.1f} Cr"
    elif num >= 10**5:  # Lakh
        return f"{num/10**5:.1f} L"
    elif num >= 10**3:  # Thousand
        return f"{num/10**3:.1f} K"
    else:
        return str(num)

total_bookings = len(df)
completed_rides = (df['ride_status'] == 'Completed').sum()
cancelled_rides = (df['ride_status'] == 'Cancelled').sum()
total_revenue = df['Booking Value'].sum()

st.markdown("### 📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Bookings", abbreviate_number(total_bookings))
col2.metric("Completed Rides", abbreviate_number(completed_rides))
col3.metric("Cancelled Rides", abbreviate_number(cancelled_rides))
col4.metric("Total Revenue (₹)", abbreviate_number(total_revenue))

st.markdown("### 🔍 Data Preview")
st.dataframe(df.head(50), width='stretch')

st.markdown('### Dataset Description')
st.markdown("<p style='color:black; text-align:left; font-size:18px'>The dataset contains 50,000+ Uber ride records from 2024 across the Delhi NCR region. Key attributes include ride date and time, time of day, vehicle type,ride distance, booking value, and ride status. These features enable analysis of customer demand patterns, peak hours, and mobility trends.</p>", unsafe_allow_html=True)

st.markdown("<p style='color:black; text-align:left; font-size:18px'>Some important columns used in the analysis along with their description are:</p>", unsafe_allow_html=True)
schema_df = pd.DataFrame({
    "Column Name": [
        "Booking Status", "Time_of_Day", "Vehicle Type",
        "Ride Distance", "Booking Value", "Avg VTAT" , "Avg CTAT"
    ],
    "Description": [
        "Status of booking(Completed, Cancelled, or Incomplete) ",
        "Morning/Afternoon/Evening/Night",
        "Type of vehicle booked by the customer",
        "Distance of the ride",
        "Fare amount for the ride",
        "Average time for driver to reach pickup location (in minutes)",
        "Average trip duration from pickup to destination (in minutes)"
    ],
    "Source": [
        "Original", "Derived", "Original",
        "Original", "Original", "Original","Original"
    ]
})

st.dataframe(schema_df, width='stretch')

st.subheader("🛠 Data Processing & Feature Engineering")
st.write("""
- **Time_of_Day:** Derived from 'Time' to categorize rides into Morning/Afternoon/Evening/Night
- **Ride Status:** Combined original flags to classify rides as Completed, Cancelled, or Incomplete
- **Payment Status:** To clearly state where payment was made or not 
- All irrelevant columns were removed for clarity and performance
""")