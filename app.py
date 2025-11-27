import streamlit as st
from jamai_backend import ask_jamai

st.title("JamAI Backend + Streamlit Frontend")

prompt = st.text_input("Ask something:")
if st.button("Send"):
    answer = ask_jamai(prompt)
    st.write(answer)

