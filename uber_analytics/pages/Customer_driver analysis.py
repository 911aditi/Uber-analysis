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
st.markdown("#### Explore the Customer Driver related Insights here👇")

df['Driver Ratings'] = pd.to_numeric(df['Driver Ratings'], errors='coerce')
df['Customer Rating'] = pd.to_numeric(df['Customer Rating'], errors='coerce')

st.sidebar.header("🔎 Filters")

min_date = pd.to_datetime("2024-01-01").date()
max_date = pd.to_datetime("2024-12-31").date()

selected_date_range = st.sidebar.date_input(
    "Booking Date (2024 only)",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date)

status_options = sorted(df['Booking Status'].dropna().unique())
selected_status = st.sidebar.multiselect(
    "Booking Status",
    options=status_options,
    default=status_options
)

driver_min, driver_max = st.sidebar.slider(
    "Driver Rating Range",
    min_value=float(df['Driver Ratings'].min()),
    max_value=float(df['Driver Ratings'].max()),
    value=(0.0, 5.0),
    step=0.1
)

customer_min, customer_max = st.sidebar.slider(
    "Customer Rating Range",
    min_value=float(df['Customer Rating'].min()),
    max_value=float(df['Customer Rating'].max()),
    value=(0.0, 5.0),
    step=0.1
)

@st.cache_data(show_spinner=False)
def apply_filters(df,status,d_min, d_max,c_min, c_max,start_date, end_date):
    filtered = df.copy()

    # Booking status
    if status:
        filtered = filtered[filtered['Booking Status'].isin(status)]

    # Rating range
    filtered = filtered[
        filtered['Driver Ratings'].between(d_min, d_max) &
        filtered['Customer Rating'].between(c_min, c_max)
    ]

    # Date Range
    if len(selected_date_range) == 2:
        start_date, end_date = map(pd.to_datetime, selected_date_range)
        filtered = filtered.loc[
            (filtered['Date'] >= start_date) &
            (filtered['Date'] <= end_date)]

    return filtered

start_date, end_date = selected_date_range

df_filtered = apply_filters(
    df,
    selected_status,
    driver_min, driver_max,
    customer_min, customer_max,
    start_date, end_date
)

df_filtered['Date'] = pd.to_datetime(df_filtered['Date']).dt.date
df_filtered['Avg CTAT'] = pd.to_numeric(df_filtered['Avg CTAT'], errors='coerce')
df_filtered['Avg VTAT'] = pd.to_numeric(df_filtered['Avg VTAT'], errors='coerce')

st.markdown("<p style='color:#73C2FF; text-align: left; font-size:18px; font-weight:bold'>Average VTAT over time: </p>", unsafe_allow_html=True)
df_daily = (df_filtered[['Date', 'Avg VTAT']].drop_duplicates(subset='Date').sort_values('Date'))
   
fig = px.line(df_daily,
    x='Date',
    y='Avg VTAT',
    markers=True,
    labels={'Avg VTAT': 'Average VTAT'}
)
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Tracks whether drivers are reaching customers faster or slower across the year.
            - Average time for driver to reach pickup location varies between 2-20 minutes but mostly lies between 5-10 minutes.""")


st.markdown("<p style='color:#73C2FF; text-align: left; font-size:18px; font-weight:bold'>Average CTAT over time: </p>", unsafe_allow_html=True)
df_daily = (df_filtered[['Date', 'Avg CTAT']].drop_duplicates(subset='Date').sort_values('Date'))

fig = px.line(df_daily,
    x='Date',
    y='Avg CTAT',
    markers=True,
    title='Average CTAT Over Time',
    labels={'Avg CTAT': 'Average CTAT'}
)
fig.update_traces(line=dict(color='blue', width=2),marker=dict(color='blue'))
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Helps monitor trip duration changes 
            - Average trip duration from pickup to destination (in minutes) varies from 15 to 45 minutes.
           """)

st.markdown("<p style='color:#73C2FF; text-align: left; font-size:18px; font-weight:bold'>Customer Cancellation Reasons: </p>", unsafe_allow_html=True)
cancel_df = df_filtered[df_filtered['Reason for cancelling by Customer'] != 'Not Applicable'].copy()
reason_pct = (cancel_df['Reason for cancelling by Customer'].value_counts(normalize=True).reset_index())
reason_pct.columns = ['Reason', 'Percentage']
reason_pct['Percentage'] = reason_pct['Percentage'] * 100
fig = px.bar(reason_pct,x='Reason',y='Percentage',title='Customer Cancellation Reasons (% of Cancelled Rides)',text='Percentage',labels = {'Reason':'Reason for cancellation by customer','Percentage':'% of cancelled rides'})
fig.update_traces(texttemplate='%{text:.1f}%')
fig.update_layout(xaxis_tickangle=-45)
fig.update_layout(
    width=800,
    height=500,
    margin=dict(l=60, r=40, t=60, b=120)
)
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Identifies top issues from customers.
            - Most rides were cancelled by the customers due to wrong address.""")

st.markdown("<p style='color:#73C2FF; text-align: left; font-size:18px; font-weight:bold'>Driver Cancellation Reasons: </p>", unsafe_allow_html=True)
cancel_df = df_filtered[df_filtered['Driver Cancellation Reason'] != 'Not Applicable'].copy()
reason_pct = (cancel_df['Driver Cancellation Reason'].value_counts(normalize=True).reset_index())
reason_pct.columns = ['Reason', 'Percentage']
reason_pct['Percentage'] = reason_pct['Percentage'] * 100
fig = px.bar(reason_pct,x='Reason',y='Percentage',text='Percentage',labels = {'Reason':'Reason for cancellation by driver','Percentage':'% of cancelled rides'})
fig.update_traces(texttemplate='%{text:.1f}%')
fig.update_layout(xaxis_tickangle=-45)
fig.update_layout(
    width=800,
    height=500,
    margin=dict(l=60, r=40, t=60, b=120)
)
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Shows why drivers cancel
            - Most rides were cancelled by drivers due to customer related issue.""")

st.markdown("<p style='color:#73C2FF; text-align: left; font-size:18px; font-weight:bold'>Cancellation Share (Customer vs Driver): </p>", unsafe_allow_html=True)
cancelled = df_filtered[df_filtered['Booking Status'].isin(['Cancelled by Customer','Cancelled by Driver'])].copy()
s_count = cancelled['Booking Status'].value_counts().reset_index()
s_count.columns = ['Booking Status','Count']
fig = px.pie(s_count,names='Booking Status',values='Count')
fig.update_traces(textinfo='percent')
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Quick snapshot of responsibility.
            - Majority of cancellations are done by driver.""")

st.markdown("<p style='color:#73C2FF; text-align: left; font-size:18px; font-weight:bold'>Driver Ratings by Vehicle Type: </p>", unsafe_allow_html=True)
df_clean = df_filtered[df_filtered['Driver Ratings']!=0].copy()
fig = px.box(df_clean,x= 'Vehicle Type',y='Driver Ratings')
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Compares how satisfied drivers are across different categories.
            - Ratings mostly lie between 4.1 and 4.3 that means they are consistently high over all vehicle types. This indicates a good driver performance overall.
            - Go Mini shows slightly more rating dispersion → potential areas for quality monitoring.""")

st.markdown("<p style='color:#73C2FF; text-align: left; font-size:18px; font-weight:bold'>Customer Ratings by Vehicle Type: </p>", unsafe_allow_html=True)
df_clean = df_filtered[df_filtered['Customer Rating']!=0].copy()
fig = px.box(df_clean,x= 'Vehicle Type',y='Customer Rating')
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Reveals passenger satisfaction across vehicle categories.
            - Customer satisfaction remains consistently high across all ride categories with median around 4-4.5, indicating standardized service quality across the platform.""")

st.markdown("<p style='color:#73C2FF; text-align: left; font-size:18px; font-weight:bold'>VTAT Distribution for Cancelled vs Completed Rides: </p>", unsafe_allow_html=True)
# Create ride outcome column
df_filtered['ride_outcome'] = df_filtered.apply(lambda x: 'Cancelled' if x['Cancelled Rides by Customer'] == 1 
                             or x['Cancelled Rides by Driver'] == 1
                             else 'Completed',axis=1)
df_filtered.groupby('ride_outcome')['Avg VTAT'].mean()
fig = px.box(df_filtered,x='ride_outcome',y='Avg VTAT',color='ride_outcome')
st.plotly_chart(fig)
st.markdown("##### CONCLUSION📊")
st.markdown("""
            - Checks if higher Average VTAT impact cancellation rate.
            - This shows that higher time taken by dirver to reach pickup location leads to higher cancellations.""")






