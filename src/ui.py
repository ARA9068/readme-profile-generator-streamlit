import json
import uuid
import streamlit as st

from src.constants import SOCIAL_PLATFORMS, SKILLS
from src.readme_builder import build_readme


def apply_theme():
    if not st.session_state.get("dark_mode", False):
        return

    st.markdown(
        """
        <style>
        .stApp { background-color: #0e1117; color: #e6edf3; }
        .block-container { padding-top: 1.5rem; }

        /* General text */
        h1,h2,h3,h4,h5,h6,p,li,label,div,span { color: #e6edf3 !important; }

        /* Inputs */
        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea {
            background-color: #161b22 !important;
            color: #e6edf3 !important;
            border: 1px solid #30363d !important;
        }

        /* Buttons */
        .stButton button, .stDownloadButton button {
            background-color: #161b22 !important;
            color: #e6edf3 !important;
            border: 1px solid #30363d !important;
        }

        /* Alerts */
        div[data-testid="stAlert"] {
            background-color: #161b22 !important;
            border: 1px solid #30363d !important;
            color: #e6edf3 !important;
        }

        hr { border-color: #30363d !important; }

        /* ===== FORCE dark for ALL code-like blocks ===== */

        /* st.code wrapper (newer Streamlit) */
        div[data-testid="stCodeBlock"] {
            background: #161b22 !important;
            border: 1px solid #30363d !important;
            border-radius: 10px !important;
        }
        div[data-testid="stCodeBlock"] pre,
        div[data-testid="stCodeBlock"] code {
            background: #161b22 !important;
            color: #e6edf3 !important;
        }

        /* highlight.js fallback */
        pre, code, .hljs {
            background: #161b22 !important;
            color: #e6edf3 !important;
        }

        /* Monaco editor containers (sometimes used for st.code / st.json) */
        .monaco-editor,
        .monaco-editor .margin,
        .monaco-editor-background,
        .monaco-editor .inputarea.ime-input {
            background-color: #161b22 !important;
            color: #e6edf3 !important;
        }

        /* Ensure borders around code blocks are dark */
        pre {
            border: 1px solid #30363d !important;
            border-radius: 10px !important;
        }

        /* Inline code in markdown */
        .stMarkdown code {
            background: #161b22 !important;
            border: 1px solid #30363d !important;
            color: #e6edf3 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header(pages):
    # Theme toggle + title
    c1, c2 = st.columns([5, 1])
    with c1:
        st.title("🧩 GitHub README Profile Generator")
    with c2:
        label = "🌙 Dark" if not st.session_state.dark_mode else "☀️ Light"
        if st.button(label, use_container_width=True):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()  # immediate rerun so CSS applies with the new state

    idx = st.session_state.page_index
    labels = [p[0] for p in pages]
    st.progress((idx + 1) / len(pages), text=f"Step {idx+1}/{len(pages)} — {labels[idx]}")
    st.divider()


def _footer_spacer():
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)


def _go(delta: int, total_pages: int):
    # IMPORTANT: no st.rerun() here (avoids warning)
    st.session_state.page_index = max(0, min(st.session_state.page_index + delta, total_pages - 1))


def render_footer_nav(total_pages: int):
    _footer_spacer()
    st.divider()
    left, _, right = st.columns([1, 3, 1])

    with left:
        st.button(
            "⬅️ Previous",
            disabled=(st.session_state.page_index == 0),
            use_container_width=True,
            on_click=_go,
            args=(-1, total_pages),
        )
    with right:
        st.button(
            "Next ➡️",
            disabled=(st.session_state.page_index == total_pages - 1),
            use_container_width=True,
            on_click=_go,
            args=(+1, total_pages),
        )


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
    st.info("Tip: paste full URLs, or enter handles where suggested.")
    s = st.session_state.social

    with st.expander("✨ Fill with default placeholders", expanded=False):
        if st.button("Insert example placeholders", use_container_width=True):
            for p in SOCIAL_PLATFORMS:
                k = p["key"]
                if not s.get(k):
                    s[k] = p["placeholder"]
            # No st.rerun() needed

    cols = st.columns(2)
    for i, p in enumerate(SOCIAL_PLATFORMS):
        with cols[i % 2]:
            key = p["key"]
            label = f'{p["icon"]} {p["label"]}'
            s[key] = st.text_input(label, value=s.get(key, ""), placeholder=p["placeholder"])


def _skill_card(name: str, icon_url: str, selected: bool, key: str) -> bool:
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
    # IMPORTANT: do NOT HTML-escape, otherwise <img> becomes &lt;img&gt; in clipboard
    element_id = f"copy_{uuid.uuid4().hex}"
    js_text = json.dumps(text)

    st.components.v1.html(
        f"""
        <div style="display:flex; gap:10px; align-items:center; margin: 10px 0;">
          <button id="{element_id}" style="
              padding:10px 14px; border-radius:10px; border:1px solid #ccc;
              cursor:pointer; background:white; font-weight:600;">
            {button_label}
          </button>
          <span id="{element_id}_status" style="font-size: 12px; color: #666;"></span>
        </div>
        <script>
          const btn = document.getElementById("{element_id}");
          const status = document.getElementById("{element_id}_status");
          const text = {js_text};
          btn.addEventListener("click", async () => {{
            try {{
              await navigator.clipboard.writeText(text);
              status.textContent = "Copied!";
              setTimeout(() => status.textContent = "", 1500);
            }} catch (e) {{
              status.textContent = "Clipboard blocked by browser.";
              setTimeout(() => status.textContent = "", 2500);
            }}
          }});
        </script>
        """,
        height=60,
    )


def page_preview_generate():
    st.subheader("4) Preview & generate")

    if st.button("⚙️ Generate README", type="primary", use_container_width=True):
        st.session_state.generated_md = build_readme(
            basic=st.session_state.basic,
            social=st.session_state.social,
            selected_skills=st.session_state.skills,
        )

    md = st.session_state.get("generated_md", "").strip()

    if not md:
        st.warning("Click **Generate README** to create your final Markdown.")
        return

    left, right = st.columns([1, 1])

    with left:
        st.markdown("### 👀 Preview (rendered like GitHub)")
        # Render HTML inside markdown (so <img> becomes icons)
        st.markdown(md, unsafe_allow_html=True)

    with right:
        st.markdown("### 🧾 Generated Markdown")
        st.code(md, language="markdown")
        _copy_to_clipboard_button(md, "📋 Copy README")
        st.download_button(
            "⬇️ Download README.md",
            data=(md + "\n").encode("utf-8"),
            file_name="README.md",
            mime="text/markdown",
            use_container_width=True,
        )