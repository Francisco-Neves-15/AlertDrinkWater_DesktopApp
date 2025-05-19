import sys
# My
from modules import language
from modules.utils import get_fullTimeFormat

def clear_last_lines(n):
    for _ in range(n):
        # Move o cursor para a linha anterior
        sys.stdout.write('\033[F')   # Cursor up one line
        # Limpa a linha inteira
        sys.stdout.write('\033[K')   # Clear to the end of line
    sys.stdout.flush()

def clear_summary():
    clear_last_lines(9)

def print_summary(total_times, total_time, interval):
    WIDTH = 40
    fmt = language.langString.get
    w_title = fmt('summary_title', "summary_title")
    a_lbl = fmt('summary_alerted', "summary_alerted")
    t_lbl = fmt('summary_times', "summary_times")
    tot_lbl = fmt('summary_total_time', "summary_total_time")
    sec_lbl = fmt('summary_seconds', "summary_seconds")
    int_lbl = fmt('summary_youInterval', "summary_youInterval")
    min_lbl = fmt('summary_minutes', "summary_minutes")

    tTime_format = get_fullTimeFormat(total_time)

    # if total_times != 0:
    #     clear_summary()

    print('\n' + '='*WIDTH)
    print(f"{w_title.center(WIDTH)}")
    print('='*WIDTH)
    print(f"{a_lbl:<15}{str(total_times).center(12)}{t_lbl}")
    print(f"{tot_lbl:<15}{str(tTime_format).center(10)}")
    print('='*WIDTH)
    print(f"{int_lbl}: {str(interval).rjust(2)} {min_lbl}")
    print('='*WIDTH)

def print_greetings(version):
    WIDTH = 40
    fmt = language.langString.get
    greetings = fmt('greetings', "greetings")
    format_version = f"v{version}"

    print('\n' + '='*WIDTH)
    print(f"{greetings.center(WIDTH)}")
    print(f"{format_version.center(WIDTH)}")
    print('='*WIDTH)