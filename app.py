import streamlit as st

# 1. Page Config
st.set_page_config(page_title="AI Paper Evaluator", page_icon="📝", layout="wide")

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 35px;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True) # Corrected this line

# 3. Sidebar with Roles & Icons
st.sidebar.title("Navigation")
role = st.sidebar.radio(
    "Select Your Role:",
    ["👑 Admin", "👨‍🏫 Instructor", "📤 Invigilator", "🎓 Student"]
)

# 4. Main Header
st.markdown('<p class="main-title">GradeMind AI - Paper Evaluator</p>', unsafe_allow_html=True) # Corrected this line
st.divider()

# 5. Role Logic (Remaining same)
if "👑 Admin" in role:
    st.subheader("👑 Admin Control Panel")
    col1, col2 = st.columns(2)
    with col1:
        st.button("➕ Add New Student")
    with col2:
        st.button("➕ Add New Instructor")

elif "👨‍🏫 Instructor" in role:
    st.subheader("👨‍🏫 Instructor Portal")
    st.file_uploader("Upload Question Paper 📄", type=['pdf', 'docx'])
    st.file_uploader("Upload Answer Key (Standard) 🔑", type=['pdf', 'docx'])

elif "📤 Invigilator" in role:
    st.subheader("📤 Invigilator Portal")
    st.info("Please upload the scanned answer sheets for bulk evaluation.")
    st.file_uploader("Upload Student Sheets 📚", accept_multiple_files=True, type=['pdf', 'png', 'jpg'])

elif "🎓 Student" in role:
    st.subheader("🎓 Student Result Portal")
    roll_no = st.text_input("Enter your Roll Number (e.g., 22CSE01)")
    if st.button("Fetch My Result 🚀"):
        st.warning(f"Searching for {roll_no}... Database connection coming soon!")