import time
from selenium import webdriver
import sys
import os

driver = webdriver.Chrome('chromedriver')



def main():
    time_total = declaring_time_total()
    time_section = calculate_time_section(time_total)
    time_mini_section = calculate_time_mini_section(time_section)
    time_theory_section = time_total / 2
    metronome()
    TECHNIQUE(time_mini_section)
    TRANSCRIBING(time_section)
    REPERTOIRE(time_section)
    KNOWLEDGE(time_mini_section)
    IMPROVISATION(time_section)




def calculate_time_section(time_total):
    wants_improvisation()
    time_section = time_total
    if wants_improvisation == False:
        time_section = time_total / 4  # Cause there're 4 sections without improvisation
    elif wants_improvisation == True:
        time_section = time_total / 5
    else:
        time_section = time_total / 4
    return time_section


def declaring_time_total():
    time_total = int(input("How much time do you want to plan practicing?(Type in minutes!): "))
    return time_total * 60


def calculate_time_mini_section(time_section):
    time_mini_section = time_section / 3  # mini sections are mostly in Technique section
    return time_mini_section


def countdown_section(time_section):
    while time_section:
        mins, secs = divmod(time_section, 60)
        timer = '{:02f}:{:02f}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_section -= 1
    sys.stderr.write("\x1b[2J\x1b[H")
    print("Times up! next section")


def countdown_mini_section(time_mini_section):
    while time_mini_section:
        mins, secs = divmod(time_mini_section, 60)
        timer = '{:02f}:{:02f}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_mini_section -= 1
        sys.stderr.write("\x1b[2J\x1b[H")
    print("Times up! next section")


def wants_improvisation():
    impro_yes_no = False
    impro_yes_no = input("Do you want to include improvisation in this routine? [true/False]")
    if impro_yes_no.strip().upper().startswith('T'):
        return True
    elif impro_yes_no.strip().upper().startswith('F'):
        return False
    else:
        return False

def theory_level():
    theory_level_int = 1
    theory_level_int = int(input("""What is your level in theory knowledge from 1 to 10?(default - '1'"""))
    if theory_level_int <=5:
        return True
    elif theory_level_int >=5:
        return False
    else:
        return False

def metronome():
    driver.get("https://metronom.us/en/")
    python_button = driver.find_elements_by_xpath("//*[@id='start-stop']")[0]
    python_button.click()
    #create_and_switchTab()

#def create_and_switchTab():
    #driver.switch_to.new_window('tab')

def TECHNIQUE(time_mini_section):
    # Finger Gym
    print("For a beginning, let's do Finger Gym: \n")
    time.sleep(3)
    print("Try to 'flick' the strings with your fret fingers like you should do on hammer ons")
    print("Adnotation: https://www.justinguitar.com/guitar-lessons/finger-gym-te-110 ")
    countdown_mini_section(time_mini_section)

    # Spider exercises
    print("Nothing to say here if you know some of spider patterns on guitar")
    time.sleep(3)
    print("If you don't here's a link - http://www.diegoruizguitar.com/tabs/8-Guitar-Spider-Warm-Up-Exercises-x-Diego-Ruiz.pdf ")

    countdown_mini_section(time_mini_section)
    # Scale Picking
    print("It's time for scale picking!")
    print("You must remember that there are 3 systems of playing Scales: CAGED System, 3 notes per string,  ")
    print("Choose the difficult level: ")
    scale_difficulty = input("Do you want Beginner or Intermediate scales? [B/I]")
    if scale_difficulty.strip().upper().startswith("B"):
        print("BEGINNER:")
        print("https://musiciantuts.com/learning-guitar-scales/#Minor_Pentatonic")
        print("https://musiciantuts.com/learning-guitar-scales/#Major_Pentatonic ")

        countdown_mini_section(time_mini_section)
    if scale_difficulty.strip().upper().startswith("I"):
        print("INTERMEDIATE:")
        print(" https://musiciantuts.com/learning-guitar-scales/#Major_Scale ")
        print("https://musiciantuts.com/learning-guitar-scales/#Natural_Minor_Scale")

        countdown_mini_section(time_mini_section)

def TRANSCRIBING(time_section):
    #python_button = driver.find_elements_by_xpath("//*[@id='start-stop']")[0]
    #python_button.click
    print("TRANSCRIBING section")
    print("Download songs that you want to transcribe and put them into the software called 'transcribe'!")
    os.system('sonic-visualiser &')
    countdown_section(time_section)

def  REPERTOIRE(time_section):
    print("It's time for you to start learning songs in this section")
    print("Choose one that is: \n"
          "-BBQ Song - A simple song that you might play at a party after a few beers \n"
          "- Solo Song - Songs that would sound good without accompaniment \n"
          "- Band Songs - Songs that you should learn intensely and to learn the whole song, not only some bits! \n"
          "- Advanced Songs - When you get to advanced level, you should stop learning BBQ songs and head over into some advanced stuff!")
    countdown_section(time_section)
def KNOWLEDGE(time_section):
    print("It's time to get more knowledge/theory practically : ")
    print("This is supposed to be practical practice of music theory (sounds weird, I know!) \n"
          "So in this section, you should always be having your guitar equipped")
    global theory_level
    theory_level = theory_level()
    if theory_level == True:
        print("""Beginners should focus on Basic Rhythm, Musical time signatures, Localising notes on the neck, Intervals between notes
                It's in some way pointless for me to explain everything, if you don't know what these abilities are, you should google or watch videos about them on youtube! If you know what they mean, then it's still pointless for me to give further explanation REMEMBER TO MAKE IT PRACTICAL AND PLAY ON THE GUITAR""")
        countdown_mini_section(time_section)
    if theory_level == False:
        print("""Intermediate players should focus on: Building Chords, Localising the Chords Notes on the neck, Finding chord grips with more creativity, Modal Harmony
                It's in some way pointless for me to explain everything, if you don't know what these abilities are, you should google or watch videos about them on youtube! If you know what they mean, then it's still pointless for me to give further explanation. REMEMBER TO MAKE IT PRACTICAL AND PLAY ON THE GUITAR!""")

def IMPROVISATION(time_section):
    if wants_improvisation == True:
        print ("It's time for the improvisation")
        countdown_section(time_section)
    else:
         return 0


main()
