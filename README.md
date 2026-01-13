# 📄 AI Paper Evaluator

An Open-Source AI-powered Examination & Automated Paper Evaluation System.

---

## 📑 Project Overview
**AI Paper Evaluator** simplifies the grading process by using LLMs to evaluate student answer sheets against an instructor's key. It supports multiple roles and provides detailed AI-driven feedback.



## 🛠️ Modules & Roles

| Role | Icon | Responsibility |
| :--- | :---: | :--- |
| **Admin** | 👑 | User management and system access control. |
| **Instructor** | 👨‍🏫 | Creating exams, uploading Q-Papers and Answer Keys. |
| **Invigilator** | 📤 | Bulk uploading scanned student answer sheets. |
| **Student** | 🎓 | Checking marks and receiving AI feedback. |

---

## 🚀 Folder Structure
Organized for scalability and open-source contributions:

```text
AI-Paper-Evaluator/
├── app.py                # Main Entry Point (Streamlit)
├── requirements.txt      # Project Dependencies
├── .env                  # Private API Keys
├── engine/               # Core AI & Processing Logic
│   ├── pdf_parser.py     # PDF Text Extraction logic
│   └── evaluator.py      # AI Evaluation & Prompting
├── modules/              # UI Logic for different roles
    ├── admin_ui.py
    ├── instructor_ui.py
    ├── invigilator_ui.py
    └── student_ui.py
```
## 🛠️ Tech Stack
Frontend: Streamlit

AI: Google Gemini / OpenAI API

OCR/Parser: pdfplumber / PyPDF2

Backend: Python 3.12
---
⚙️ Installation & Setup
Follow these steps to get the project running locally:

1. Clone the repository
2. Install dependencies
3. Launch the Application
