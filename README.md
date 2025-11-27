# Malaysian Student Assistant (JamAI Base Hackathon Project)

An AI-powered Streamlit application built using **JamAI Base** to help Malaysian students with:

- 🎓 Scholarship information & guidance  
- 📚 Assignment assistance  
- 🏫 University SOP writing  
- ❓ General education-related FAQs  

This project demonstrates a real Malaysian use case of GenAI with **JamAI Base Knowledge & Action Tables**, following hackathon requirements.

---

## 🚀 Features

### 🧠 1. Four AI Assistants (Action Tables)
Each assistant is powered by a separate **JamAI Base Action Table**:

| Assistant | Table ID | Purpose |
|----------|----------|---------|
| **Scholarship Assistant** | `scholarships_assistant` | Helps students understand PTPTN, JPA, MARA, etc. |
| **Assignment Assistant** | `assignment_assistant` | Helps generate ideas, explanations, or writing tips |
| **University SOP Assistant** | `SOP_assistant` | Helps draft or refine university application SOP essays |
| **FAQ Assistant** | `FAQ_assistant` | Handles general questions from students |

Each table processes:
- `intent detection`
- `context building`
- `extracted info`
- **final response** (shown to user)

---

## 💬 2. Chat Interface with History

Each assistant has its **own chat history**, stored using Streamlit `session_state`.

This gives the user a smooth conversational experience when switching between assistants.

---

## ⚡ 3. Powered by JamAI Base

Uses:

- Action Tables  
- MultiRowAddRequest  
- Streaming text response  
- Structured CoT (Chain of Thought stored but not shown)  

The app shows only the **final response** to the user.

---

## 💻 Streamlit App

We developed an interactive **Streamlit web application** that connects directly to **JamAI Base Tables** to provide AI-powered assistance for Malaysian students.

The app allows users to:

- Select between **four AI assistants**  
  - 🎓 Scholarship Assistant  
  - 📝 Assignment Assistant  
  - 🏛️ University SOP Assistant  
  - ❓ FAQ Assistant  
- Enter questions naturally (chat-style input)
- Receive instant, AI-generated **final responses** powered by JamAI Base
- View **chat history** stored per assistant
- Switch assistants seamlessly at any time

### 🚀 Open the Streamlit App Locally
[🌐 Malaysian Student Assistant (Demo)](https://salmonhackathon-xzpn5emsvf9aqvhjrtp6bx.streamlit.app/#chat-with-scholarship-assistant)

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend / UI | Streamlit |
| Backend AI | JamAI Base Action Tables |
| Language | Python |
| Deployment | Any Streamlit environment |




