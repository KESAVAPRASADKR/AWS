# Importing necessary libraries
import streamlit as st

# Title of the app
st.title('Simple Streamlit App')

# Header/Subheader
st.header('This is a header')
st.subheader('This is a subheader')

# Text
st.text('Hello, world! This is some plain text.')

# Markdown
st.markdown('### This is a Markdown header')
st.markdown('**This** is some _Markdown_.')

# Displaying a number
st.write('Displaying a number:', 42)

# Displaying a dataframe
import pandas as pd
df = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [10, 20, 30]
})
st.write('Displaying a dataframe:', df)

# Checkbox
if st.checkbox('Show dataframe'):
    st.write(df)

# Selectbox
option = st.selectbox(
    'Which number do you like best?',
    df['Column 1']
)
st.write('You selected:', option)

# Slider
number = st.slider('Pick a number', min_value=1, max_value=10, value=5)
st.write('You selected:', number)

# Button
if st.button('Say hello'):
    st.write('Hello there!')

# Sidebar
st.sidebar.header('About')
st.sidebar.text('This is a Streamlit app example.')

# Display the app
st.write('This is a simple Streamlit app example.')
