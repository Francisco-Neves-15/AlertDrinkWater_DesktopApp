import winsound
from plyer import notification
import os
import json
# My
from config import BASE_DIR
from modules import language

ICON_PATH = os.path.join(BASE_DIR, 'image', 'icon.ico')
SOUND_PATH = os.path.join(BASE_DIR, 'audio', 'SFX_waterdrip.wav')

SOUNDS_FOLDER_PATH = os.path.join(BASE_DIR, 'audio')
SOUNDS_DESC_FILE = os.path.join(BASE_DIR, 'audios.json')

def sound_configs():
    global SOUND_PATH

    question = language.langString.get('question_whichSound', "question_whichSound")
    err = language.langString.get('question_whichSound_e', "question_whichSound_e")

    text_noSound = language.langString.get('sound_none', "sound_none")

    # Carrega o JSON com os dados dos sons
    try:
        with open(SOUNDS_DESC_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"✖ Erro ao carregar o arquivo de sons: {e}")
        return

    audios = list(data['audios'].items())  # lista de tuplas: (path, [id, nome_exibicao])
    lang_code = language.SELECT_LANG
    lang_data = data.get(lang_code, {})

    # Pergunta
    while True:

        print(f"\n❔ {question}")
        # Exibe a lista formatada com as descrições
        max_len = max(len(os.path.basename(p)) for p, _ in audios)
        for i, (path, (sound_id, _)) in enumerate(audios, start=0):
            descricao = lang_data.get(sound_id, "Descrição indisponível.")
            if i == 0:
                print(f"{i}. {text_noSound:<{max_len}} | {descricao}")
            else:
                print(f"{i}. {os.path.basename(path):<{max_len}} | {descricao}")

        try:
            val = int(input("\n→ "))
            if 0 <= val <= len(audios):
                break
            else:
                print(f"❌ {err}")
        except ValueError:
            print(f"❌ {err}")

    # Define o caminho escolhido
    try:
        if val == 0:
            selected_path = "none"
            SOUND_PATH = selected_path
        else:
            selected_path = os.path.join(BASE_DIR, audios[val][0])
            SOUND_PATH = selected_path

        print(f"\n✅: {os.path.basename(SOUND_PATH)}")
    except Exception as e:
        print(f"❌", e)


def sound_play():
    global SOUND_PATH
    path = SOUND_PATH
    if path != "none":
        try:
            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except Exception as e:
            print(e)
    else:
        text_soundMute = language.langString.get('sound_muted', "sound_muted")
        print("\n", text_soundMute)


def box_notif_water():
    title = language.langString.get('boxNotif_title', "boxNotif_title")
    msg = language.langString.get('boxNotif_msg', "boxNotif_msg")
    duration = language.langString.get('duration', 5)
    try:
        notification.notify(
            title=f"{title}",
            message=msg,
            timeout=duration,
            app_icon=ICON_PATH
        )
    except Exception as e:
        err = language.langString.get('error_notif', "error_notif")
        print(f"✖ {err}: {e}")