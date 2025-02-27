# streamlit_app.py
import streamlit as st

# Title of the app
st.title("Simple Streamlit App in Docker with uv")

st.write("This is a basic Streamlit application running inside a Docker container, built with Alpine Linux and uv.")
st.write("It demonstrates a simple input and output.")

# Text input widget
name = st.text_input("Enter your name", "Streamlit User")

# Greeting message based on input
if name:
    st.write(f"Hello, {name}! Welcome to the Streamlit app.")
else:
    st.write("Please enter your name above.")

st.markdown("---") # Separator line

st.markdown("Below is a simple slider example:")

# Slider widget
age = st.slider("What is your age?", 0, 120, 25) # (label, min, max, default_value)

st.write(f"You selected age: {age}")

st.markdown("---") # Separator line

st.markdown("This app is running with:")
st.write(f"- **Streamlit Version:** `{st.__version__}`")
st.write("- **Built in a Docker container based on Alpine Linux**")
st.write("- **Package installation potentially accelerated by `uv`**")

st.success("🎉 You've successfully run a Streamlit app in Docker!")