import streamlit as st
import pandas as pd

def run():
    st.subheader("Data Overview for Page 1")

    # Sample Dataset 1
    data1 = {
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 30, 40]
    }

    df1 = pd.DataFrame(data1)

    st.write(df1)
    st.bar_chart(df1.set_index('Category'))