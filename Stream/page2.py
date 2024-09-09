import streamlit as st
import pandas as pd
import numpy as np

def run():
    st.subheader("Data Overview for Page 2")

    # Sample Dataset for Page 2
    data2 = {
        'Type': ['X', 'Y', 'Z'],
        'Amount': [15, 25, 35]
    }

    df2 = pd.DataFrame(data2)

    # Bar chart
    st.bar_chart(df2.set_index('Type'))

    # Line chart
    st.line_chart(df2['Amount'])

    # Area chart
    st.area_chart(df2['Amount'])

    # Box plot using matplotlib
    st.subheader("Box Plot")
    st.pyplot(create_box_plot(df2))

    # Random histogram
    st.subheader("Random Histogram")
    st.bar_chart(np.random.randn(100))

    # Pie chart
    st.subheader("Pie Chart")
    st.pyplot(create_pie_chart(df2))


def create_box_plot(data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 6))
    plt.boxplot(data['Amount'])
    plt.title("Box Plot of Amounts")
    return plt

def create_pie_chart(data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 6))
    plt.pie(data['Amount'], labels=data['Type'], autopct='%1.1f%%')
    return plt