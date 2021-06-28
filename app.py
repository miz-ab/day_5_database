import main
import day5
import streamlit as st

PAGES = {
    "Home Page": main,
    "Detail": day5
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()