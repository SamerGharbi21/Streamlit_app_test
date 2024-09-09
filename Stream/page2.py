import streamlit as st
import pandas as pd

def run():
    st.subheader("Data Overview for Page 2")

    # Sample Dataset 2
    data2 = {
        'Type': ['X', 'Y', 'Z'],
        'Amount': [15, 25, 35]
    }

    df2 = pd.DataFrame(data2)

    st.write(df2)
    st.line_chart(df2.set_index('Type'))