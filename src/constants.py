SOCIAL_PLATFORMS = [
    {
        "key": "website",
        "label": "Website",
        "icon": "🌐",
        "placeholder": "https://your-site.com",
        "template": None,
    },
    {
        "key": "github",
        "label": "GitHub",
        "icon": "🐙",
        "placeholder": "username or https://github.com/username",
        "template": "https://github.com/{handle}",
    },
    {
        "key": "linkedin",
        "label": "LinkedIn",
        "icon": "💼",
        "placeholder": "handle or https://www.linkedin.com/in/handle",
        "template": "https://www.linkedin.com/in/{handle}",
    },
    {
        "key": "twitter",
        "label": "X (Twitter)",
        "icon": "🐦",
        "placeholder": "handle or https://x.com/handle",
        "template": "https://x.com/{handle}",
    },
    {
        "key": "instagram",
        "label": "Instagram",
        "icon": "📸",
        "placeholder": "handle or https://instagram.com/handle",
        "template": "https://instagram.com/{handle}",
    },
    {
        "key": "kaggle",
        "label": "Kaggle",
        "icon": "📊",
        "placeholder": "handle or https://kaggle.com/handle",
        "template": "https://kaggle.com/{handle}",
    },
    {
        "key": "devto",
        "label": "Dev.to",
        "icon": "🧑‍💻",
        "placeholder": "handle or https://dev.to/handle",
        "template": "https://dev.to/{handle}",
    },
    {
        "key": "medium",
        "label": "Medium",
        "icon": "✍️",
        "placeholder": "handle or https://medium.com/@handle",
        "template": "https://medium.com/@{handle}",
    },
    {
        "key": "stackoverflow",
        "label": "Stack Overflow",
        "icon": "🧠",
        "placeholder": "user id or full URL",
        "template": None,
    },
    {
        "key": "youtube",
        "label": "YouTube",
        "icon": "▶️",
        "placeholder": "channel URL",
        "template": None,
    },
]

# Devicon CDN for skill icons in both UI + README output
# (You can add more very easily.)
SKILLS = {
    "Languages": [
        ("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"),
        ("JavaScript", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"),
        ("TypeScript", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg"),
        ("C++", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"),
        ("Java", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"),
    ],
    "Frameworks & Libraries": [
        ("Streamlit", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg"),
        ("FastAPI", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg"),
        ("Django", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg"),
        ("Flask", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"),
        ("PyTorch", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg"),
        ("TensorFlow", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"),
        ("OpenCV", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg"),
        ("NumPy", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg"),
        ("Pandas", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"),
        ("scikit-learn", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg"),
    ],
    "Tools": [
        ("Git", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"),
        ("Docker", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"),
        ("Linux", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"),
        ("VS Code", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"),
    ],
    "Databases": [
        ("PostgreSQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"),
        ("MySQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"),
        ("MongoDB", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg"),
    ],
    "Cloud": [
        ("AWS", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg"),
        ("Azure", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg"),
        ("GCP", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg"),
    ],
}