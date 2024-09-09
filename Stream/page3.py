import streamlit as st
import pandas as pd

def run():
    st.subheader("Data Overview for Page 3")

    # Sample Dataset 3
    data3 = {
        'Year': [2018, 2019, 2020, 2021],
        'Sales': [100, 150, 200, 250]
    }

    df3 = pd.DataFrame(data3)

    st.write(df3)
    st.area_chart(df3.set_index('Year'))