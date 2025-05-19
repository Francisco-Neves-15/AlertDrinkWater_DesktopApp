import json
import os
langString = {}

SELECT_LANG = "en-US"

OPTION_MAP = {
    "1": "en-US",
    "2": "pt-BR",
    "3": "fr-FR"
}

def language_config(BASE_DIR):
    global langString, SELECT_LANG
    print("""
| 🌐/❔ |  A/あ |
| 1. English    |
| 2. Português  |
| 3. Français   |
| -more coming- |
| ... 1,2,3 ... |
""")
    while True:
        choice = input("→ ")
        if choice in OPTION_MAP:
            code = OPTION_MAP[choice]
            SELECT_LANG = code
            break
        print("❌ Invalid option. Try again.")

    path = os.path.join(BASE_DIR, "strings.json")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        langString = data.get(code, {})
    except Exception as e:
        print(f"✖ Error loading language: {e}")
        langString = {}
