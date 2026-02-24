import streamlit as st

from src.state import init_state
from src.ui import (
    render_header,
    render_footer_nav,
    page_basic_info,
    page_social_links,
    page_skills,
    page_preview_generate,
)

PAGES = [
    ("Basic info", page_basic_info),
    ("Links & social", page_social_links),
    ("Skills", page_skills),
    ("Preview & generate", page_preview_generate),
]

st.set_page_config(
    page_title="GitHub README Profile Generator",
    page_icon="🧩",
    layout="wide",
)

init_state(total_pages=len(PAGES))

# Header + progress
render_header(PAGES)

# Current page content
_, page_fn = PAGES[st.session_state.page_index]
page_fn()

# Footer navigation
render_footer_nav(total_pages=len(PAGES))