import streamlit as st

def init_state(total_pages: int) -> None:
    if "page_index" not in st.session_state:
        st.session_state.page_index = 0

    if "basic" not in st.session_state:
        st.session_state.basic = {
            "name": "",
            "subtitle": "",
            "working_on": "",
            "python_projects": "",  # multi-line, one per line
            "learning": "",
            "collab": "",
            "help_with": "",
            "ask_me_about": "",
            "email": "",
            "hobbies": "",  # multi-line, one per line
        }

    if "social" not in st.session_state:
        # values can be full URLs or handles; builder normalizes
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

    # safety
    st.session_state.page_index = max(0, min(st.session_state.page_index, total_pages - 1))