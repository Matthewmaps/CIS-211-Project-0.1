import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Matthew Green | Portfolio',
  page_icon='🟢',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
    <style>
        .main-header{font-size: 42px; font-weight: bold; text-align:center;}
        .sub-header {font_size: 24px; text-align:center; color: #666;}
      </style>
      ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '👔 About', '💼 projects', '⚒️ Skills', '📝 Resume', '📩 Contact' ])

# Home Page
if page == '🏠 Home'
st.markdown('<p class="main-header">Matthew Green</p>', unsafe_allow_html=True)
st.markdown('<p classes="sub-header">Average Student | Medagar Evers College</p>', unsafe_allow_html=True



            
