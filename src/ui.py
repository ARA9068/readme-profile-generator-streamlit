import html
import uuid
import streamlit as st
import streamlit.components.v1 as components

from src.constants import SOCIAL_PLATFORMS, SKILLS
from src.readme_builder import build_readme

def render_header(pages):
    st.title("🧩 GitHub README Profile Generator")
    idx = st.session_state.page_index
    labels = [p[0] for p in pages]
    st.progress((idx + 1) / len(pages), text=f"Step {idx+1}/{len(pages)} — {labels[idx]}")
    st.divider()

def _footer_spacer():
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

def render_footer_nav(total_pages: int):
    _footer_spacer()
    st.divider()
    left, mid, right = st.columns([1, 3, 1])

    with left:
        st.button(
            "⬅️ Previous",
            disabled=(st.session_state.page_index == 0),
            use_container_width=True,
            on_click=lambda: _go(-1, total_pages),
        )
    with right:
        st.button(
            "Next ➡️",
            disabled=(st.session_state.page_index == total_pages - 1),
            use_container_width=True,
            on_click=lambda: _go(+1, total_pages),
        )

def _go(delta: int, total_pages: int):
    st.session_state.page_index = max(0, min(st.session_state.page_index + delta, total_pages - 1))
    st.rerun()

def page_basic_info():
    st.subheader("1) Basic information")

    b = st.session_state.basic
    c1, c2 = st.columns(2)

    with c1:
        b["name"] = st.text_input("👤 Your Name", value=b["name"], placeholder="e.g., Jane Doe")
        b["subtitle"] = st.text_input("🏷️ Subtitle", value=b["subtitle"], placeholder="e.g., ML Engineer | Python Developer")
        b["working_on"] = st.text_input("🔭 I’m currently working on", value=b["working_on"], placeholder="e.g., a Streamlit app")
        b["learning"] = st.text_input("🧠 I’m currently learning", value=b["learning"], placeholder="e.g., MLOps, Docker")

    with c2:
        b["collab"] = st.text_input("👯 I’m looking to collaborate on", value=b["collab"], placeholder="e.g., open-source Python tools")
        b["help_with"] = st.text_input("🤝 I’m looking for help with", value=b["help_with"], placeholder="e.g., cloud deployment")
        b["ask_me_about"] = st.text_input("💬 Ask me about", value=b["ask_me_about"], placeholder="e.g., Python, Computer Vision")
        b["email"] = st.text_input("📫 How to reach me (Email)", value=b["email"], placeholder="e.g., you@example.com")

    st.markdown("### 🐍 Python Projects (one per line)")
    b["python_projects"] = st.text_area(
        "📌 Project list",
        value=b["python_projects"],
        placeholder="Project A\nProject B\nProject C",
        label_visibility="collapsed",
        height=120,
    )

    st.markdown("### 🎯 Hobbies (one per line)")
    b["hobbies"] = st.text_area(
        "🏖️ Hobbies",
        value=b["hobbies"],
        placeholder="Hiking\nReading\nPhotography",
        label_visibility="collapsed",
        height=120,
    )

def page_social_links():
    st.subheader("2) Links & social media")

    st.info("Tip: you can paste full URLs, or just enter handles where suggested.")
    s = st.session_state.social

    # Offer quick defaults
    with st.expander("✨ Fill with default placeholders", expanded=False):
        if st.button("Insert example placeholders", use_container_width=True):
            for p in SOCIAL_PLATFORMS:
                k = p["key"]
                if not s.get(k):
                    s[k] = p["placeholder"]
            st.rerun()

    cols = st.columns(2)
    for i, p in enumerate(SOCIAL_PLATFORMS):
        with cols[i % 2]:
            key = p["key"]
            label = f'{p["icon"]} {p["label"]}'
            s[key] = st.text_input(label, value=s.get(key, ""), placeholder=p["placeholder"])

def _skill_card(name: str, icon_url: str, selected: bool, key: str) -> bool:
    # Simple clickable card: checkbox + icon + label
    checked = st.checkbox(" ", value=selected, key=key, label_visibility="collapsed")
    st.image(icon_url, width=42)
    st.caption(name)
    return checked

def page_skills():
    st.subheader("3) Skills (click icons to select)")
    st.write("Selected skills will appear in your README. Unselected will be excluded.")

    selected = set(st.session_state.skills)

    for category, items in SKILLS.items():
        st.markdown(f"### {category}")
        cols = st.columns(6)
        for idx, (name, icon_url) in enumerate(items):
            with cols[idx % 6]:
                key = f"skill_{category}_{name}"
                is_selected = name in selected
                checked = _skill_card(name, icon_url, is_selected, key)
                if checked:
                    selected.add(name)
                else:
                    selected.discard(name)

    st.session_state.skills = selected

def _copy_to_clipboard_button(text: str, button_label: str = "📋 Copy README"):
    # Streamlit-safe clipboard button via small HTML/JS component
    element_id = f"copy_{uuid.uuid4().hex}"
    safe_text = html.escape(text)

    components.html(
        f"""
        <div style="display:flex; gap:10px; align-items:center; margin: 10px 0;">
          <button id="{element_id}" style="
              padding:10px 14px; border-radius:10px; border:1px solid #ccc;
              cursor:pointer; background:white; font-weight:600;">
            {button_label}
          </button>
          <span id="{element_id}_status" style="font-size: 12px; color: #666;"></span>
        </div>
        <textarea id="{element_id}_text" style="position:absolute; left:-9999px; top:-9999px;">{safe_text}</textarea>
        <script>
          const btn = document.getElementById("{element_id}");
          const status = document.getElementById("{element_id}_status");
          const ta = document.getElementById("{element_id}_text");
          btn.addEventListener("click", async () => {{
            try {{
              await navigator.clipboard.writeText(ta.value);
              status.textContent = "Copied!";
              setTimeout(() => status.textContent = "", 1500);
            }} catch (e) {{
              // fallback
              ta.select();
              document.execCommand("copy");
              status.textContent = "Copied!";
              setTimeout(() => status.textContent = "", 1500);
            }}
          }});
        </script>
        """,
        height=60,
    )

def page_preview_generate():
    st.subheader("4) Preview & generate")

    md = build_readme(
        basic=st.session_state.basic,
        social=st.session_state.social,
        selected_skills=st.session_state.skills,
    )

    left, right = st.columns([1, 1])

    with left:
        st.markdown("### 👀 Preview")
        st.markdown(md)

    with right:
        st.markdown("### 🧾 Generated Markdown")
        st.code(md, language="markdown")
        _copy_to_clipboard_button(md, "📋 Copy README")
        st.download_button(
            "⬇️ Download README.md",
            data=md.encode("utf-8"),
            file_name="README.md",
            mime="text/markdown",
            use_container_width=True,
        )