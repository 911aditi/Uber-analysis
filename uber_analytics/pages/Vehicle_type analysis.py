import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data(show_spinner=False)
def load_data():
    return pd.read_csv(r"C:\Users\imadi\OneDrive\Desktop\python\cleaned_data.csv")

df = load_data()

st.markdown("#### Explore the Vehicle Type related Insights here👇")

st.sidebar.header("🔎 Filters")

vehicle_options = sorted(df['Vehicle Type'].dropna().unique())
selected_vehicle = st.sidebar.multiselect(
    "Select Vehicle Type",
    options=vehicle_options,
    default=vehicle_options
)

status_options = sorted(df['Booking Status'].dropna().unique())

selected_status = st.sidebar.multiselect(
    "Booking Status",
    options=status_options,
    default=status_options
)

fil_df = df[
    (df['Vehicle Type'].isin(selected_vehicle))&
    (df['Booking Status'].isin(selected_status))
]

st.markdown("<p style='color:brown; text-align: left; font-size:18px; font-weight:bold'>Bookings by Vehicle Type: </p>", unsafe_allow_html=True)
df_completed = fil_df[fil_df['ride_status']=='Completed']
fig = px.bar(df_completed,x='Vehicle Type',labels={'count':'Number of bookings'})
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Compares popularity of Autos, Go Mini, Sedans, Bikes, UberXL, etc.
            - Most popular vehicle is auto while the least popular is UberXL.""")

st.markdown("<p style='color:brown; text-align: left; font-size:18px; font-weight:bold'>Vehicle type vs Booking Status: </p>", unsafe_allow_html=True)
fil_df['Booking_Status_Grouped'] = fil_df['Booking Status'].replace({
    'Cancelled by Customer': 'Cancelled',
    'Cancelled by Driver': 'Cancelled'
})
fig = px.bar(fil_df,x='Vehicle Type',barmode='group',color='Booking_Status_Grouped',labels={'count':'Number of bookings'})
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Shows which vehicles have higher success/cancellation rates.
            - Highest number of rides are booked for auto and most cancellations are also for auto.""")

st.markdown("<p style='color:brown; text-align: left; font-size:18px; font-weight:bold'>Average ride distance by Vehicle Type: </p>", unsafe_allow_html=True)
df_avg = fil_df.groupby('Vehicle Type',observed=True)['Ride Distance'].mean().reset_index()
fig = px.bar(df_avg,x='Vehicle Type',y='Ride Distance',labels={'Ride Distance': 'Average Ride Distance'})
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Shows which vehicles are used for short vs long trips.
            - All types of vehicles have almost the same average ride distance.""")

st.markdown("<p style='color:brown; text-align: left; font-size:18px; font-weight:bold'>Booking Value by Vehicle Type: </p>", unsafe_allow_html=True)
fig = px.bar(fil_df,x='Vehicle Type',y='Booking Value')
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Reveals which fleet contributes the most to revenue.
            - Auto contributes the highest to the total booking value.""")
