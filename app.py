import streamlit as st
import requests
import os

JAMAI_API_KEY = os.getenv("jamai_pat_49188da586bc90838807d00bb0d2ce9b585633f7d9ab07ca")

def call_jamai(prompt):
    url = "https://api.jamai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {JAMAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "jamba-1.5-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

st.title("JamAI + Streamlit Demo")

user_input = st.text_input("Ask something:")

if st.button("Send"):
    reply = call_jamai(user_input)
    st.write(reply)
