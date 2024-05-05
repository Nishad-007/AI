import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.title('1. _TEXT_ :blue[search] 🖼️🔎')
st.markdown('search IMAGE using TEXT')


st.title('2. _IMAGE_ :blue[search] 🖼️🔎')
st.markdown('search IMAGE using IMAGE')

