import streamlit as st

def init_state(total_pages: int) -> None:
    if "page_index" not in st.session_state:
        st.session_state.page_index = 0

    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    if "generated_md" not in st.session_state:
        st.session_state.generated_md = ""  # only filled after clicking Generate

    if "basic" not in st.session_state:
        st.session_state.basic = {
            "name": "",
            "subtitle": "",
            "working_on": "",
            "python_projects": "",
            "learning": "",
            "collab": "",
            "help_with": "",
            "ask_me_about": "",
            "email": "",
            "hobbies": "",
        }

    if "social" not in st.session_state:
        st.session_state.social = {
            "website": "",
            "github": "",
            "linkedin": "",
            "twitter": "",
            "instagram": "",
            "kaggle": "",
            "devto": "",
            "medium": "",
            "stackoverflow": "",
            "youtube": "",
        }

    if "skills" not in st.session_state:
        st.session_state.skills = set()

    st.session_state.page_index = max(0, min(st.session_state.page_index, total_pages - 1))