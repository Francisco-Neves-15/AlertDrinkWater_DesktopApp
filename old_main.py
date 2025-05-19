import time
import os
import sys
import json

import winsound
from plyer import notification

# === Configurações ===
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# === Configurações Idioma ===
DEFAULT_STRNOTFIND = "⚠ Missing Text"
langString = {}

def language_config():
    print("""
| 🌐❔ | A/あ |
   | 1. EN |
   | 2. PT |
   | 3. FR |
| ... 1,2,3 ... |
""")
    option_map = {
        "1": "en-US",
        "2": "pt-BR",
        "3": "fr-FR"
    }

    while True:
        selected = input("→ ")
        if selected in option_map:
            lang_code = option_map[selected]
            break
        else:
            print("❌ Invalid Option. Numbers Only -OR- Out of Range")

    try:
        # Caminho para o JSON
        json_path = os.path.join(BASE_DIR, "strings.json")
        with open(json_path, "r", encoding="utf-8") as f:
            all_languages = json.load(f)
        
        if lang_code in all_languages:
            global langString
            langString = all_languages[lang_code]
        else:
            print("⚠ Language file not found")
            langString = {}
    except Exception as e:
        print("✖ Error to load the Language:")
        print(f"   {type(e).__name__}: {e}")
        langString = {}

configsNotif = {}

def sound_configs(caminho):
    winsound.PlaySound(caminho, winsound.SND_FILENAME | winsound.SND_ASYNC)

def get_configsNotif():
    return {
        "title": f"💧 {langString.get("boxNotif_title", DEFAULT_STRNOTFIND)}",
        "msg": langString.get("boxNotif_msg", DEFAULT_STRNOTFIND),
        "duration": 5,
        "icon": os.path.join(BASE_DIR, "image/icon.ico"),
        "sound": os.path.join(BASE_DIR, "alert.wav"),
    }

def box_notif_water():
    try:
        notification.notify(
            title=configsNotif["title"],
            message=configsNotif["msg"],
            timeout=configsNotif["duration"],
            app_icon=configsNotif["icon"],
        )
    except Exception as e:
        print(f"✖ {langString.get("error_notif", DEFAULT_STRNOTFIND)}:")
        print(f"   {type(e).__name__}: {e}")

def print_summary(total_times, total_timeHMS, interval):
    title = langString.get("summary_title", DEFAULT_STRNOTFIND)
    alerted_label = langString.get("summary_alerted", DEFAULT_STRNOTFIND)
    times_label = langString.get("summary_times", DEFAULT_STRNOTFIND)
    total_time_label = langString.get("summary_total_time", DEFAULT_STRNOTFIND)
    seconds_label = langString.get("summary_seconds", DEFAULT_STRNOTFIND)
    youInterval = langString.get("summary_youInterval", DEFAULT_STRNOTFIND)
    minutes_lable = langString.get("summary_minutes", DEFAULT_STRNOTFIND)

    # Define a largura total da "caixa"
    WIDTH = 32

    print()
    print("=" * WIDTH)
    print(f"💧 {title} 💧".center(WIDTH))
    print("=" * WIDTH)
    print(f"{alerted_label:<12} {str(total_times).center(10)} {times_label}")
    print(f"{total_time_label:<12} {str(total_timeHMS).center(10)} {minutes_lable}")
    print("=" * WIDTH)
    print(f"{youInterval:<1}: {str(interval).center(2)} {minutes_lable}")
    print("=" * WIDTH)

def loop(minutes):
    delaySec = minutes * 1

    total_times = 0
    total_timeHMS = 0

    while True:
        # Play the Soud
        sound_configs(configsNotif["sound"])
        # Notif the Box
        box_notif_water()
        #
        total_times += 1
        #
        total_timeHMS += delaySec
        #
        print_summary(total_times, total_timeHMS, minutes)
        # Wait
        time.sleep(delaySec)

def get_userInfos():
    while True:
        try:
            print(langString.get("question_interval", "Quantos minutos?"))
            user_delay = int(input("→ "))
            break
        except ValueError:
            print(langString.get("question_interval_e", "Erro de número"))
    return user_delay

def main():
    language_config()
    global configsNotif
    configsNotif = get_configsNotif()
    try:
        user_delay = get_userInfos()
        loop(user_delay)

    except Exception as e:
        print(f"✖ {langString.get("error_program", DEFAULT_STRNOTFIND)}:")
        print(f"   {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
