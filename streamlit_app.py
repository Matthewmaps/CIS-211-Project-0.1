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
