import streamlit as st

# Title of the dashboard
st.title("Multi-Page Streamlit Dashboard")

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page", ["Page 1", "Page 2", "Page 3"])

# Routing to different pages
if page == "Page 1":
    import page1
    page1.run()
elif page == "Page 2":
    import page2
    page2.run()
elif page == "Page 3":
    import page3
    page3.run()