import random
from enum import Enum
import timer
import time

class Activity:
    ACTIVE_IMMERSION = "Active Immersion"
    OUTPUT_ANKI = "Output Anki"
    GRAMMAR_ANKI = "Grammar Anki"

class Section(Enum):
    ACTIVE_IMMERSION = 1
    OUTPUT_ANKI = 2
    GRAMMAR_ANKI = 3

def main():
    try: 
        ACTIVE_IMMERSION(30*60)
        OUTPUT_ANKI(15*60)
        GRAMMAR_ANKI(10*60)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")

def print_and_sleep(message, sleep_time=3):
    print(message)
    time.sleep(sleep_time)

def bold_text(text):
    return "\033[1m" + text + "\033[0m"

def ACTIVE_IMMERSION(time_section):
    print_and_sleep(bold_text(Activity.ACTIVE_IMMERSION + " for 30 minutes"))
    timer.countdown_section(time_section)

def OUTPUT_ANKI(time_section):
    print_and_sleep(bold_text(Activity.OUTPUT_ANKI + " for 15 minutes"))
    timer.countdown_section(time_section)

def GRAMMAR_ANKI(time_section):
    print_and_sleep(bold_text(Activity.GRAMMAR_ANKI + " for 10 minutes"))
    timer.countdown_section(time_section)

if __name__ == "__main__":
    main()