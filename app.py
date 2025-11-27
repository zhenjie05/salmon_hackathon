import streamlit as st
from jamaibase import JamAI, types as t

# --- HARDCODED CREDENTIALS ---
PROJECT_ID = "proj_80340c2a0317eee7bc3aae55"
PAT = "jamai_pat_49188da586bc90838807d00bb0d2ce9b585633f7d9ab07ca"

# Initialize JamAI client
client = JamAI(project_id=PROJECT_ID, pat=PAT)

st.set_page_config(page_title="AI Assistant", layout="wide")

st.title("🎓 Multi-Assistant Chatbot")

# --- Chat History Setup ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of {"role": "...", "content": "..."}

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Assistant:** {chat['content']}")

# --- User Input Box ---
user_query = st.text_input("Ask something:")

# --- Get response from JamAI SELECT Function ---
def query_assistant(query):
    response = client.select.rows(
        table_id="scholarships_assistant",
        inputs={"user_query": query},
        outputs=["response"]
    )
    final_response = response.rows[0]["response"]
    return final_response

# --- Submit ---
if st.button("Send"):
    if user_query.strip():
        # Add user question to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_query})

        # Get assistant final response ONLY
        final_response = query_assistant(user_query)

        # Add ONLY final response (no AI internal response)
        st.session_state.chat_history.append({"role": "assistant", "content": final_response})
        
        st.rerun()
