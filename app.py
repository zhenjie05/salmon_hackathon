from __future__ import annotations
import streamlit as st
from jamaibase import JamAI, types as t

# ==============================
# CONFIG (HARDCODED CREDENTIALS)
# ==============================
PROJECT_ID = "proj_80340c2a0317eee7bc3aae55"
PAT = "jamai_pat_49188da586bc90838807d00bb0d2ce9b585633f7d9ab07ca"

# === your table IDs ===
SCHOLAR_TABLE = "scholarships_assistant"
ASSIGN_TABLE = "assignment_assistant"
SOP_TABLE = "SOP_assistant"
FAQ_TABLE = "FAQ_assistant"

# === input column names ===
INPUT_COL = {
    "scholarships_assistant": "user_query",
    "assignment_assistant": "user_query",
    "SOP_assistant": "user_query",
    "FAQ_assistant": "input",
}

# === output column that you want to show ===
OUTPUT_COL = {
    "scholarships_assistant": "response",
    "assignment_assistant": "response",
    "SOP_assistant": "response",
    "FAQ_assistant": "response",
}

# ==============================
# HELPER: stream response
# ==============================
def run_table(client, table_id: str, user_query: str, stream: bool = True) -> str:
    """Send user_query to selected table and return streamed response text."""
    req = t.MultiRowAddRequest(
        table_id=table_id,
        data=[{INPUT_COL[table_id]: user_query}],
        stream=stream
    )

    # removed streaming UI display
    accumulated = ""

    if stream:
        for chunk in client.table.add_table_rows(t.TableType.ACTION, req):
            if getattr(chunk, "output_column_name", "") == OUTPUT_COL[table_id]:
                accumulated += getattr(chunk, "text", "")

        # return final result (non-stream)
        final = client.table.add_table_rows(
            t.TableType.ACTION,
            t.MultiRowAddRequest(
                table_id=table_id,
                data=[{INPUT_COL[table_id]: user_query}],
                stream=False
            )
        )
        row0 = final.rows[0]
        return getattr(row0.columns.get(OUTPUT_COL[table_id]), "text", "")

    resp = client.table.add_table_rows(t.TableType.ACTION, req)
    row0 = resp.rows[0]
    return getattr(row0.columns.get(OUTPUT_COL[table_id]), "text", "")

# ==============================
# UI
# ==============================

st.title("🇲🇾 Malaysian Student Assistant (JamAI Base)")
st.caption("Select one assistant → ask any question → get instant response.")

# Sidebar — Table names only
with st.sidebar:
    st.subheader("Tables Overview")
    st.text(f"{SCHOLAR_TABLE}")
    st.text(f"{ASSIGN_TABLE}")
    st.text(f"{SOP_TABLE}")
    st.text(f"{FAQ_TABLE}")

# Create client using hardcoded credentials
try:
    client = JamAI(project_id=PROJECT_ID, token=PAT)
except Exception as e:
    st.error(f"JamAI config error: {e}")
    st.stop()

# Assistant selector
assistant_choice = st.selectbox(
    "Choose an assistant:",
    [
        "Scholarship Assistant",
        "Assignment Assistant",
        "University SOP Assistant",
        "FAQ Assistant"
    ]
)

# Mapping for table selection
mapping = {
    "Scholarship Assistant": SCHOLAR_TABLE,
    "Assignment Assistant": ASSIGN_TABLE,
    "University SOP Assistant": SOP_TABLE,
    "FAQ Assistant": FAQ_TABLE
}
selected_table = mapping[assistant_choice]

# ==============================
# Chat History Initialization
# ==============================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {
        SCHOLAR_TABLE: [],
        ASSIGN_TABLE: [],
        SOP_TABLE: [],
        FAQ_TABLE: []
    }

# ==============================
# Show Chat History for Assistant
# ==============================
st.subheader(f"💬 Chat with {assistant_choice}")

history = st.session_state.chat_history[selected_table]

for msg in history:
    if msg["role"] == "user":
        st.markdown(f"**🧑‍🎓 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 AI:** {msg['content']}")

# ==============================
# User Input Area
# ==============================
user_query = st.text_area("Enter your question:")

if st.button("Generate Response", type="primary"):
    if not user_query.strip():
        st.warning("Please enter a question.")
        st.stop()

    # Add to chat history (user)
    history.append({"role": "user", "content": user_query})

    with st.spinner("Thinking..."):
        final_answer = run_table(client, selected_table, user_query, stream=True)

    # Save assistant response
    history.append({"role": "assistant", "content": final_answer})

    st.success("Done!")
    st.markdown("### Final Response")
    st.write(final_answer)

# Update chat history
st.session_state.chat_history[selected_table] = history
