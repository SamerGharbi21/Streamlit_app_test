import streamlit as st
import pandas as pd
import numpy as np

def run():
    st.subheader("Data Overview for Page 1")

    # Sample Dataset for Page 1
    data1 = {
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 30, 40]
    }

    df1 = pd.DataFrame(data1)

    # Bar chart
    st.bar_chart(df1.set_index('Category'))

    # Line chart
    st.line_chart(df1['Values'])

    # Area chart
    st.area_chart(df1['Values'])

    # Histogram
    st.subheader("Histogram")
    st.bar_chart(np.random.randn(100))

    # Pie chart (using the data from the dataframe)
    st.subheader("Pie Chart")
    st.write('Pie Chart of Values')
    st.pyplot(create_pie_chart(df1))

    # Random scatter plot (using matplotlib)
    st.subheader("Scatter Plot")
    create_scatter_plot(df1)


def create_pie_chart(data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 6))
    plt.pie(data['Values'], labels=data['Category'], autopct='%1.1f%%')
    return plt

def create_scatter_plot(data):
    import matplotlib.pyplot as plt

    x = np.random.rand(10)
    y = np.random.rand(10)

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y)
    plt.title("Random Scatter Plot")
    st.pyplot(plt)