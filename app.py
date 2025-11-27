import streamlit as st
from jamaibase import JamAI, types as t

# ===========================================================
#  HARDCODED JAMAI CREDENTIALS
#  Make sure your repo is private if storing secrets here.
# ===========================================================

JAMAI_PROJECT_ID = "proj_80340c2a0317eee7bc3aae55"
JAMAI_PAT = "jamai_pat_49188da586bc90838807d00bb0d2ce9b585633f7d9ab07ca"

# ===========================================================
#  INITIALIZE JAMAI CLIENT
# ===========================================================

client = JamAI(
    project_id=JAMAI_PROJECT_ID,
    token=JAMAI_PAT
)

# ===========================================================
#  AVAILABLE ACTION TABLES
# ===========================================================

ACTION_TABLES = {
    "Scholarship Assistant": "scholarships_assistant",
    "Assignment Assistant": "assignment_assistant",
    "SOP Assistant": "SOP_assistant",
    "FAQ Assistant": "FAQ_assistant"
}

# ===========================================================
#  STREAMLIT PAGE CONFIG & UI
# ===========================================================

st.set_page_config(page_title="UM Multifunction AI Assistant", layout="centered")

st.title("🎓 UM Multifunction AI Assistant")
st.write("Select a module and enter your question.")

selected_module = st.selectbox(
    "Choose a module:",
    list(ACTION_TABLES.keys())
)

user_query = st.text_area("Enter your question here:", height=150)

submit = st.button("Get Answer")

# ===========================================================
#  JAMAI QUERY FUNCTION
# ===========================================================

def run_jamai(table_id: str, query: str):
    """
    Sends user query to JamAI table and returns only 'response' field.
    """
    try:
        response = client.tables.query(
            table_id=table_id,
            query={
                "input": {
                    "user_query": query,
                    "input": query   # for FAQ_assistant (uses 'input' instead of 'user_query')
                }
            }
        )

        # Extract only the model_outputs.response field
        outputs = response.rows[0].model_outputs
        return outputs.get("response", "No response field found in table.")

    except Exception as e:
        return f"❌ Error: {str(e)}"


# ===========================================================
#  PROCESS USER QUERY
# ===========================================================

if submit:
    if not user_query.strip():
        st.warning("Please enter a question.")
    else:
        table_id = ACTION_TABLES[selected_module]
        st.write(f"🧠 Using module: **{selected_module}**")

        with st.spinner("Thinking..."):
            output = run_jamai(table_id, user_query)

        st.success("Response:")
        st.write(output)
