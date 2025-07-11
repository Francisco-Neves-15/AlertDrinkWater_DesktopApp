import time

from config           import BASE_DIR
from modules.language import language_config
from modules.notifier import sound_play, sound_configs
from modules.summary  import print_summary, print_greetings
from modules.utils    import get_user_interval

APP_VERSION = 2.2

def loop(minutes):
    total_times = 0
    total_secs = 0
    delay = minutes * 60

    while True:
        sound_play()
        # box_notif_water()
        print_summary(total_times, total_secs, minutes)
        total_times += 1
        total_secs += delay
        time.sleep(delay)


def main():
    language_config(BASE_DIR)
    sound_configs()
    print_greetings(APP_VERSION)
    print("")
    interval = get_user_interval()
    try:
        loop(interval)
    except Exception as e:
        err = "❌ Fail to Run the Program"
        print(f"✖ {err}: {e}")

if __name__ == '__main__':
    main()