from __future__ import annotations

from typing import Dict, Set, Tuple
from src.constants import SKILLS, SOCIAL_PLATFORMS

def _clean(s: str) -> str:
    return (s or "").strip()

def _lines(multiline: str) -> list[str]:
    items = [x.strip() for x in (multiline or "").splitlines()]
    return [x for x in items if x]

def _as_url(value: str, template: str | None) -> str:
    v = _clean(value)
    if not v:
        return ""
    if v.startswith("http://") or v.startswith("https://"):
        return v
    if template:
        return template.format(handle=v.lstrip("@"))
    # fallback: treat as url-ish
    return v

def build_readme(basic: Dict[str, str], social: Dict[str, str], selected_skills: Set[str]) -> str:
    name = _clean(basic.get("name", ""))
    subtitle = _clean(basic.get("subtitle", ""))

    md: list[str] = []

    # Header
    if name:
        md.append(f"# Hi 👋, I'm {name}")
    else:
        md.append("# Hi 👋")

    if subtitle:
        md.append(f"### {subtitle}")

    md.append("")  # spacer

    # About bullets (only include if filled)
    bullets: list[Tuple[str, str]] = [
        ("🔭 I’m currently working on", basic.get("working_on", "")),
        ("🧠 I’m currently learning", basic.get("learning", "")),
        ("👯 I’m looking to collaborate on", basic.get("collab", "")),
        ("🤝 I’m looking for help with", basic.get("help_with", "")),
        ("💬 Ask me about", basic.get("ask_me_about", "")),
        ("📫 How to reach me", basic.get("email", "")),
    ]

    about_lines = []
    for label, value in bullets:
        v = _clean(value)
        if v:
            # email: if looks like an email, format as mailto
            if label.startswith("📫") and "@" in v and " " not in v:
                about_lines.append(f"- {label}: [{v}](mailto:{v})")
            else:
                about_lines.append(f"- {label}: **{v}**")

    projects = _lines(basic.get("python_projects", ""))
    if projects:
        about_lines.append("")
        about_lines.append("#### 🐍 Python Projects")
        for p in projects:
            about_lines.append(f"- {p}")

    hobbies = _lines(basic.get("hobbies", ""))
    if hobbies:
        about_lines.append("")
        about_lines.append("#### 🎯 Hobbies")
        for h in hobbies:
            about_lines.append(f"- {h}")

    if about_lines:
        md.append("## 👨‍💻 About me")
        md.extend(about_lines)
        md.append("")

    # Social links
    social_items = []
    for p in SOCIAL_PLATFORMS:
        key = p["key"]
        url = _as_url(social.get(key, ""), p.get("template"))
        if url:
            social_items.append((p["label"], p["icon"], url))

    if social_items:
        md.append("## 🌐 Connect with me")
        for label, icon, url in social_items:
            md.append(f"- {icon} [{label}]({url})")
        md.append("")

    # Skills
    if selected_skills:
        md.append("## 🛠️ Skills")
        # Render as icons (HTML) + fallback text
        # Keep it simple and GitHub-friendly
        skill_icon_map = {}
        for _, items in SKILLS.items():
            for name, icon_url in items:
                skill_icon_map[name] = icon_url

        icons = []
        for s in sorted(selected_skills):
            icon_url = skill_icon_map.get(s)
            if icon_url:
                icons.append(f'<img src="{icon_url}" alt="{s}" width="40" height="40" />')
        if icons:
            md.append("".join(icons))
            md.append("")
        md.append(", ".join(sorted(selected_skills)))
        md.append("")

    return "\n".join(md).strip() + "\n"