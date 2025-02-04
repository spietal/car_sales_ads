import pandas as pd
import plotly.express as px
import streamlit as st

vehicles=pd.read_csv('vehicles_us.csv')

fig1 = px.histogram(vehicles, x='price', title='Distribution of Price')
st.plotly_chart(fig1)



st.header('Correlation Investigation: Price, Mileage, and Market Duration')

# Create a checkbox to select which scatter plot to show
show_price_scatter = st.checkbox('Show Price vs. Days on Market')

if show_price_scatter:
    # Scatter plot for Price vs. Days on the Market
    fig = px.scatter(vehicles, x='price', y='days_listed', title='Price vs. Days on Market')
    st.plotly_chart(fig)
else:
    # Scatter plot for Odometer vs. Days on the Market
    fig = px.scatter(vehicles, x='odometer', y='days_listed', title='Odometer vs. Days on Market')
    st.plotly_chart(fig)
