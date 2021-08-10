import streamlit as st
#from main import demo
from upload import upload_image
from about_page import show_devs


page = st.sidebar.selectbox("Explore and About", ("Main", "About"))


if page == "Main":
    upload_image()
else:
    show_devs() 