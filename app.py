"""import streamlit as st

# Title of the web app
st.title('Simple Streamlit App')

# Text input for the user
user_name = st.text_input("Enter your name:")

# If the user enters their name, display a greeting message
if user_name:
    st.write(f"Hello, {user_name}! Welcome to Streamlit.")
else:
    st.write("Please enter your name above.")

import streamlit as st

st.title('Hello, Streamlit!')
st.write("Welcome to Streamlit. This is your first app!")

-----------------------------------------------------------------




import streamlit as st

# Sidebar for navigation
st.sidebar.title('Navigation Bar')

# Set up page selection with a default of 'Home'
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Store user input in session state
if 'user_name' not in st.session_state:
    st.session_state.user_name = ''

# Home page: Get user input
if st.session_state.page == 'Home':
    st.title('Simple Streamlit App')
    
    # Get user input (name or any other input)
    user_name = st.text_input("Enter your name:", value=st.session_state.user_name)

    # Store the user input in session state for later pages
    st.session_state.user_name = user_name

    # When the user enters input, automatically navigate to Page 2
    if user_name:
        st.session_state.page = 'Page 2'
        st.rerun()  # Forces the app to rerun, applying the page change

    if not user_name:
        st.write("Please enter your name above.")

# Page 2: Display the entered name
if st.session_state.page == 'Page 2':
    st.title('New Page')
    if st.session_state.user_name:
        st.write(f"Welcome to new page, {st.session_state.user_name}!")
    else:
        st.write("You haven't entered your name yet. Go back to the Home page.")

# Page 3: Another page
if st.session_state.page == 'Page 3':
    st.title('Page 3')
    if st.session_state.user_name:
        st.write(f"Hello again, {st.session_state.user_name}!")
    else:
        st.write("No name entered yet. Please go back and enter your name.")


-===========================================================================

import streamlit as st

# Title of the web app
st.title('Simple Streamlit App')

# Text input for the user
user_name = st.text_input("Enter your name:",value="")

# If the user enters their name, display a greeting message
if user_name:
    st.write(f"Hello, {user_name}! Welcome to Streamlit.")
else:
    st.write("Please enter your name above.")
"""


import streamlit as st


def process_name(user_name):
    return f"{user_name}! Welcome to Streamlit."

# Title of the web app
st.title('Simple Streamlit App')


# Text input for the user
user_name = st.text_input("Enter your name:")


if user_name:
    # Pass the user input to the function
    greeting_message = process_name(user_name)
    
    # Display the result
    st.write(greeting_message)
    st.write(f"Hey, {greeting_message}")
    
