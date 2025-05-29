import streamlit as st

# Define the pages
main_page = st.Page("intro.py", title="Introduction")
page_2 = st.Page("dashboards.py", title="Dashboards")
page_3 = st.Page("chatbot.py", title="Chatbot")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()