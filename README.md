# GitHub README Profile Generator (Streamlit)

A simple Streamlit web app that helps anyone generate a clean GitHub Profile README.md.

## Features
- 4-step wizard (Basic Info → Social Links → Skills → Preview/Generate)
- Previous/Next navigation in the footer
- Skill selection via icons
- Empty fields are automatically excluded from the generated README
- Copy-to-clipboard + download README.md

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py