import streamlit as st
import random
title = st.text_input('User Name', '')
password = st.text_input('Password','')
columns = st.columns((2, 1, 2))
button_pressed = columns[1].button('Log in')