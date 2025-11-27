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

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend / UI | Streamlit |
| Backend AI | JamAI Base Action Tables |
| Language | Python |
| Deployment | Any Streamlit environment |

---

## 📦 Project Structure


