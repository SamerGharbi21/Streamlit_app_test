import streamlit as st
import pandas as pd
import numpy as np

def run():
    st.subheader("Data Overview for Page 3")

    # Sample Dataset for Page 3
    data3 = {
        'Year': [2018, 2019, 2020, 2021],
        'Sales': [100, 150, 200, 250]
    }

    df3 = pd.DataFrame(data3)

    # Bar chart
    st.bar_chart(df3.set_index('Year'))

    # Line chart
    st.line_chart(df3['Sales'])

    # Area chart
    st.area_chart(df3['Sales'])

    # Histogram
    st.subheader("Histogram")
    st.bar_chart(np.random.randn(100))

    # Pie chart
    st.subheader("Pie Chart")
    st.pyplot(create_pie_chart(df3))

    # Scatter plot
    st.subheader("Scatter Plot")
    create_scatter_plot(df3)


def create_pie_chart(data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 6))
    plt.pie(data['Sales'], labels=data['Year'], autopct='%1.1f%%')
    return plt

def create_scatter_plot(data):
    import matplotlib.pyplot as plt

    x = data['Year']
    y = data['Sales']

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y)
    plt.title("Sales Scatter Plot")
    return plt