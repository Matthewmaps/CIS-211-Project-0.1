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
if page == '🏠 Home':
  st.markdown('<p class="main-header">Matthew Green</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Undergraduate Student | Medagar Evers College</p>', unsafe_allow_html=True)

  # Three columns for stats 
  co11, co12, col13 = st.columns(3)

  with col1:
    st.metric ('GPA', '3.5', '📚')
  with col2: 
    st.metric('Projects', '5', '💻')
  with col3:
    st.metric('skills', '10+', '🚀')

st.write('---')

st.write('---')

# Introduction with columns
col1, col2 = st.columns([2,1])
with col1:
     st.subheader('Welcome to my digital space!👋')
     st.write('''
                I am a Computer Information Systems student passionate about web development and emerging technologies. Currently learning
                HTML, CSS, JavaScript, and Python to build innovative solutions.
            
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emerging Technologies (CIS 211)
            
                🌱 **Fun Fact:** I can solve a Rubik's cube in under 2 minutes!
            ''')
with col2: 
  # Placeholder for image
  st.image('https://raw.githubusercontent.com/avinashjairam/cis211_project1/refs/heads/main/grumpy_cat.jfif', use_column_width=True)

  # About Page
  elif page == '👔 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2025 - Present: Medgar Evers College'):
    st.write('''
                - Major: Business Administration 
                - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
                - Activities: None
            ''')

  with st.expander('2023 - 2025: NYC Museum School'):
    st.write('''
                - Graduated with honors
                - AP Computer Science A (Score: 5)
                - Founded Coding Club
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Web Development', 'AI/Machine Learning', 'Photography', 'Basketball', 'Travel', 'Baseball']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('https://iprx-cms-content.ams1.vultrobjects.com/Blog_How_To_Crawl_4_capcha_ded9206d5f.png')

    with col2:
        st.subheader('🛒 E-Commerce Price Tracker')
        st.write('Python web scraper that monitors Amazon prices and sends alerts')
        st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')


  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg')
    with col2:
      st.subheader('📊 Student Grade Calulator')
      st.write('Interactive web app for calculating and visualizing grades')
      st.caption('**Technologies:** Python, Pandas, Plotly')

elif page == '🛠 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
    'Python' : 85,
    'HTML/CSS' : 70,
    'JavaScript' : 60,
    'SQL' : 50,
    'Technical Writing' : 40
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success('PowerPoint')
    st.info('Google Docs')
    st.warning('ChatGPT/AI Tools')
    
  with col3:
    st.success('Presentations')
    st.info('Writing')
    st.warning('Social Media')
    
      
            
