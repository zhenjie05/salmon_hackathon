from __future__ import annotations
import streamlit as st
from jamaibase import JamAI, types as t

# ==============================
# CONFIG
# ==============================
PROJECT_ID = "YOUR_PROJECT_ID"
PAT = "YOUR_PAT"

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

    placeholder = st.empty()
    accumulated = ""

    # stream mode
    if stream:
        for chunk in client.table.add_table_rows(t.TableType.ACTION, req):
            if getattr(chunk, "output_column_name", "") == OUTPUT_COL[table_id]:
                text = getattr(chunk, "text", "")
                accumulated += text
                placeholder.markdown(accumulated)

        # get final full result (non-stream)
        final = client.table.add_table_rows(
            t.TableType.ACTION,
            t.MultiRowAddRequest(
                table_id=table_id,
                data=[{INPUT_COL[table_id]: user_query}],
                stream=False
            )
        )
        row0 = final.rows[0]
        final_text = getattr(row0.columns.get(OUTPUT_COL[table_id]), "text", "")
        return final_text

    # no streaming
    resp = client.table.add_table_rows(t.TableType.ACTION, req)
    row0 = resp.rows[0]
    return getattr(row0.columns.get(OUTPUT_COL[table_id]), "text", "")


# ==============================
# UI
# ==============================

st.title("🇲🇾 Malaysian Student Assistant (JamAI Base)")
st.caption("Select one assistant → ask any question → get instant response.")

# Sidebar config
with st.sidebar:
    st.subheader("JamAI Base Settings")
    PROJECT_ID = st.text_input("Project ID", PROJECT_ID)
    PAT = st.text_input("PAT", PAT, type="password")

    st.markdown("---")
    st.subheader("Tables Overview (Read Only)")
    st.text(f"{SCHOLAR_TABLE}")
    st.text(f"{ASSIGN_TABLE}")
    st.text(f"{SOP_TABLE}")
    st.text(f"{FAQ_TABLE}")

# Create client
try:
    client = JamAI(project_id=PROJECT_ID, token=PAT)
except Exception as e:
    st.error(f"JamAI config error: {e}")
    st.stop()

# Main UI
assistant_choice = st.selectbox(
    "Choose an assistant:",
    [
        "Scholarship Assistant",
        "Assignment Assistant",
        "University SOP Assistant",
        "FAQ Assistant"
    ]
)

mapping = {
    "Scholarship Assistant": SCHOLAR_TABLE,
    "Assignment Assistant": ASSIGN_TABLE,
    "University SOP Assistant": SOP_TABLE,
    "FAQ Assistant": FAQ_TABLE
}
selected_table = mapping[assistant_choice]

user_query = st.text_area("Enter your question (BM or English):")

if st.button("Generate Response", type="primary"):
    if not user_query.strip():
        st.warning("Please enter a question.")
        st.stop()

    st.subheader("AI Response (Streaming)")
    with st.spinner("Thinking..."):
        final_answer = run_table(client, selected_table, user_query, stream=True)

    st.success("Done!")
    st.markdown("### Final Response")
    st.write(final_answer)
