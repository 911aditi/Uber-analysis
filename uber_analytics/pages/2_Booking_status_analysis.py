import streamlit as st
import pandas as pd
import plotly.express as px
import os

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "cleaned_data.csv")
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df

df = load_data()

st.markdown("#### Explore the Booking status and revenue related trends and insights here 👇")

st.sidebar.title("🔎 Filters")

booking_status_options = sorted(df['Booking Status'].unique())

selected_booking_status = st.sidebar.multiselect(
    "Booking Status",
    options=booking_status_options,
    default=booking_status_options
)

payment_options = sorted(df['Payment Method'].unique())

selected_payment = st.sidebar.multiselect(
    "Payment Method",
    options=payment_options,
    default=payment_options
)

min_date = pd.to_datetime("2024-01-01")
max_date = pd.to_datetime("2024-12-31")

selected_date_range = st.sidebar.date_input(
    "Booking Date (2024 only)",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

time_of_day_options = sorted(df['Time_of_Day'].unique())

selected_time_of_day = st.sidebar.multiselect(
    "Time of Day",
    options=time_of_day_options,
    default=time_of_day_options)

@st.cache_data(show_spinner=False)
def apply_sidebar_filters(df,booking_status,payment_method,date_range,time_of_day):
    filtered = df.copy()

    # Booking Status
    if booking_status:
        filtered = filtered.loc[filtered['Booking Status'].isin(booking_status)]

    # Payment Method
    if payment_method:
        filtered = filtered.loc[filtered['Payment Method'].isin(payment_method)]

    # Date Range
    if len(selected_date_range) == 2:
        start_date, end_date = map(pd.to_datetime, selected_date_range)
        filtered = filtered.loc[
            (filtered['Date'] >= start_date) &
            (filtered['Date'] <= end_date)
        ]

    # Time of Day
    if time_of_day:
        filtered = filtered.loc[filtered['Time_of_Day'].isin(time_of_day)]

    return filtered

df_filtered = apply_sidebar_filters(df,selected_booking_status,selected_payment,selected_date_range,selected_time_of_day)

st.markdown("<p style='color:#4FC3F7; text-align: left; font-size:18px; font-weight:bold'>Booking Status distribution: </p>", unsafe_allow_html=True)
fig = px.bar(df_filtered,x='Booking Status')
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
- Shows share of completed, customer cancellations, driver cancellations, incomplete rides.
- Most of the rides have been completed.""")

st.markdown("<p style='color:#4FC3F7; text-align: left; font-size:18px; font-weight:bold'>Daily Booking Trends: </p>", unsafe_allow_html=True)
df_daily = df_filtered.groupby('Date').size().reset_index(name='Total_Bookings')
fig = px.line(
    df_daily,
    x='Date',
    y='Total_Bookings',
    title='Total Bookings Over Time',
    markers=True
)
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
- Highlights peaks/troughs in demand across the year.
- Highest number of booking were seen on Nov 8 that is 14.""")

st.markdown("<p style='color:#4FC3F7; text-align: left; font-size:18px; font-weight:bold'>Bookings by Time of Day vs Day of Week: </p>", unsafe_allow_html=True)
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
time_order = ['Morning', 'Afternoon', 'Evening', 'Night']
df_filtered['Day'] = pd.Categorical(df_filtered['Day'], categories=day_order, ordered=True)
df_filtered['Time_of_Day'] = pd.Categorical(df_filtered['Time_of_Day'], categories=time_order, ordered=True)
pivot = df_filtered.pivot_table(index='Day',columns='Time_of_Day',aggfunc='size',fill_value=0,observed=False)
fig = px.imshow(pivot,text_auto=True,aspect='auto',color_continuous_scale='YlOrRd')
fig.update_layout(
    xaxis_title='Time of Day',
    yaxis_title='Day',
    coloraxis_colorbar_title='Number of Bookings'
)
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Reveals ride demand patterns 
            - Mondays are the busiest among all days sepically Monday afternoons and evenings.""")

st.markdown("<p style='color:#4FC3F7; text-align: left; font-size:18px; font-weight:bold'>Payment Method share: </p>", unsafe_allow_html=True)
df_completed = df_filtered[df_filtered['payment_status']=='Paid'].copy()
df_completed['Payment_Method_Clean'] = df_completed['Payment Method'].replace({'Credit Card': 'Card','Debit Card': 'Card'})
fig = px.pie(
    df_completed,
    names='Payment_Method_Clean',
    color='Payment_Method_Clean'
)
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Shows how customers prefer to pay 
            - UPI is the most commonly used payment method.""")


st.markdown("<p style='color:#4FC3F7; text-align: left; font-size:18px; font-weight:bold'>Booking Value vs Ride Distance: </p>", unsafe_allow_html=True)
fig = px.scatter(df_filtered,x='Ride Distance',y='Booking Value')
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Checks if longer rides always bring higher revenue.
            - Not always true that longer rides bring higher revenue.""")

 
st.markdown("<p style='color:#4FC3F7; text-align: left; font-size:18px; font-weight:bold'>Incomplete Rides by Reason: </p>", unsafe_allow_html=True)
fig = px.scatter(df_filtered,x='Ride Distance',y='Booking Value')
df_new = df_filtered[df_filtered['Incomplete Rides Reason']!='Not Applicable'].copy()
r_count = (df_new['Incomplete Rides Reason'].value_counts().reset_index())
r_count.columns = ['Reason', 'Count']
fig = px.bar(r_count,x='Reason',y='Count',labels = {'Reason':'Incomplete Rides Reason','Count':'Count of rides'})
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.write("""
- Helps track operational problems 
- Rides were mostly incomplete due to Vehicle Breakdown and Other issues.
""")










