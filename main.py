import time
from selenium import webdriver
import sys
import os

driver = webdriver.Chrome('chromedriver')



def main():
    time_total = declaring_time_total()
    time_section = calculate_time_section(time_total)
    time_mini_section = calculate_time_mini_section(time_section)
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
        timer = '{:02d}:{:02d}'.format(mins, secs)
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
    if impro_yes_no == "True":
        return True
    elif impro_yes_no == "False":
        return False
    else:
        return False

def metronome():
    driver.get("https://metronom.us/en/")
    python_button = driver.find_elements_by_xpath("//*[@id='start-stop']")[0]
    python_button.click()
    create_and_switchTab() 
      
def create_and_switchTab():
    driver.switch_to.new_window('tab')

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
    print("Choose the difficult level: ")
    scale_difficulty = input("Do you want Beginner or Intermediate scales? [B/I]")
    if scale_difficulty == "B":
        print("BEGINNER:")
        create_and_switchTab()
        driver.get("https://musiciantuts.com/learning-guitar-scales/#Minor_Pentatonic")
        create_and_switchTab()
        driver.get("https://musiciantuts.com/learning-guitar-scales/#Major_Pentatonic ")
        create_and_switchTab()
        driver.get("https://musiciantuts.com/learning-guitar-scales/#Blues_Scale ")
    
        countdown_mini_section(time_mini_section)
    if scale_difficulty =="I":
        print("INTERMEDIATE:")
        create_and_switchTab()
        driver.get(" https://musiciantuts.com/learning-guitar-scales/#Major_Scale ")
        create_and_switchTab()
        driver.get("https://musiciantuts.com/learning-guitar-scales/#Natural_Minor_Scale")
        create_and_switchTab()
        driver.get("https://musiciantuts.com/learning-guitar-scales/#Harmonic_Minor ")
        create_and_switchTab()
        driver.get("https://musiciantuts.com/learning-guitar-scales/#Melodic_Minor ")

        countdown_mini_section(time_mini_section)

def TRANSCRIBING(time_section):
    python_button = driver.find_elements_by_xpath("//*[@id='start-stop']")[0]
    python_button.click
    print("TRANSCRIBING section")
    print("Download songs that you want to transcribe and put them into the software called 'transcribe'!")
    os.system('transcribe')
    countdown_section(time_section)

def  REPERTOIRE(time_section):
    print("It's time for you to start learning songs in this section")
    print("Choose one that is: \n"
          "-BBQ Song - A simple song that you might play at a party after a few beers \n"
          "- Solo Song - Songs that would sound good without accompaniment \n"
          "- Band Songs - Songs that you should learn intensely and to learn the whole song, not only some bits! \n"
          "- Advanced Songs - When you get to advanced level, you should stop learning BBQ songs and head over into some advanced stuff!")

def KNOWLEDGE(time_mini_section):
    print("It's time to get more knowlede :) ")
    print("You should be spending this time on: \n"
          "- 5 minutes - Music Theory - either the recommended one \n"
          "- 5 minutes - Scales or chords depending on what you need to work on. \n"
          "- 5 minutes - < something else of your choice")
    print("While doing this, remenber to take notes")
    time.sleep(5)
    print("Countdown starts!")
    time.sleep(2)
    # Music Theory
    print("Music theory")
    countdown_mini_section(time_mini_section)
    # Scales or chords
    print("Scales or chords")
    countdown_mini_section(time_mini_section)
    # Something else of your choice
    print("Something of your choice")
    countdown_mini_section(time_mini_section)
    
def IMPROVISATION(time_section):
    if wants_improvisation == True:
        print ("It's time for the improvisation")
        countdown_section(time_section)
    else:
         return 0


main()