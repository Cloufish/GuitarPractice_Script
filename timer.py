import time
import shutil
import sys
from playsound import playsound
from threading import Thread


def countdown_section(time_section, break_length=60, end_message="Time's up! Next section", sound_break_file="resources/yamete.ogg", sound_work_file="resources/motto.mp3"):
    try:
        while time_section >= 0:
            mins, secs = divmod(time_section, 60)
            timer = '\033[91m{:02d}:{:02d}\033[0m'.format(int(mins), int(secs))
            columns = shutil.get_terminal_size().columns
            padding = " " * ((int(columns) - len(timer)) // 2)
            print(padding + timer, end="\r")
            time.sleep(1)
            time_section -= 1
    except KeyboardInterrupt:
        print("\nInterrupted! Moving to the next section...")
    finally:
        playsound(sound_break_file)
        print("\n" + end_message)

    # Start the break countdown
    print("Starting break...")
    try:
        while break_length >= 0:
            mins, secs = divmod(break_length, 60)
            timer = '\033[91m{:02d}:{:02d}\033[0m'.format(int(mins), int(secs))
            columns = shutil.get_terminal_size().columns
            padding = " " * ((int(columns) - len(timer)) // 2)
            print(padding + timer, end="\r")
            time.sleep(1)
            break_length -= 1
    except KeyboardInterrupt:
        print("\nBreak interrupted! Moving to the next section...")
    finally:
        playsound(sound_work_file)
        print("\nBreak's over!")