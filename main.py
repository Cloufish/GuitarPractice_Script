import time
from selenium import webdriver
import sys
import os
import random

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
    KNOWLEDGE(time_section)
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
    time_total = int(
        input("How much time do you want to plan practicing?(Type in minutes!): "))
    return time_total * 60


def calculate_time_mini_section(time_section):
    # mini sections are mostly in Technique section
    time_mini_section = time_section / 3
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
    impro_yes_no = input(
        "Do you want to include improvisation in this routine? [true/False]")
    if impro_yes_no.strip().upper().startswith('T'):
        return True
    elif impro_yes_no.strip().upper().startswith('F'):
        return False
    else:
        return False


def theory_level():
    theory_level_int = 1
    theory_level_int = int(
        input("""What is your level in theory knowledge from 1 to 10?(default - '1'"""))
    if theory_level_int <= 5:
        return True
    elif theory_level_int >= 5:
        return False
    else:
        return False


def metronome():
    driver.get("https://metronom.us/en/")
    python_button = driver.find_elements_by_xpath("//*[@id='start-stop']")[0]
    # python_button.click()
    # create_and_switchTab()

# def create_and_switchTab():
    # driver.switch_to.new_window('tab')


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
    scale_difficulty = input(
        "Do you want Beginner or Intermediate scales? [B/I]")
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
    # python_button.click
    print("TRANSCRIBING section")
    print("Download songs that you want to transcribe and put them into the software called 'transcribe'!")
    os.system('sonic-visualiser &')
    os.system('musescore &')
    countdown_section(time_section)


def REPERTOIRE(time_section):
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
        print("[0] Basic Rhythm")
        print("[1] Musical time signatures")
        print("[2] Localising notes on the neck")
        print("[3] Intervals between notes")

        time_mini_theory_section = time_section/2
        
        chosen_theory_segment = int(
            input("Choose the first theory practice segment by inputting 0-3"))
        second_chosen_theory_segment = int(
            input("Choose the second theory practice segment by inputting 0-3"))

        if chosen_theory_segment == 0:
            print("You've chosen Basic Rhythm practice")
            strumming_patters = [1, 2, 3, 4, 5]
            print("We'll begin with the most basic pattern: \n")
            print("""1 & 2 & 3 & 4 &
                     D   D   D   D""")
            print("""This might sound easy, however, you need to keep the tempo even! 
                  I suggest you lowering the tempo, this would make this exercise more challenging and productive! Doing it slowly and accurate!
                  And another tip: YOU NEED to keep the up and down hand motion going non-stop!""")
            countdown_section(time_mini_theory_section/3)
            for i in range(0,2):
                random_strumming_patterns = random.choice(strumming_patters) 
                strumming_patters = [2, 3, 4, 5]
                if random_strumming_patterns == 2:
                    print("Time for Upstrokes strumming on 'AND', so we're strumming up additionaly! ")
                    print("""1 & 2 & 3 & 4 &
                             D U D U D U D U""")
                    countdown_section(time_mini_theory_section/3)
                    continue
                elif random_strumming_patterns == 3:
                    print("Time for Muted strumming on second, fourth beat or whichever you like")
                    print("""1 & 2 & 3 & 4 &
                             D U M U D U M U""")
                    countdown_section(time_mini_theory_section/3)
                    continue
                elif random_strumming_patterns == 4:
                    print("Resting some of the counts (not strumming them)")
                    print("""1 & 2 & 3 & 4 &
                             D U   U D U   U""")
                    countdown_section(time_mini_theory_section/3)
                    continue
                elif random_strumming_patterns == 5:
                    print("Resting the Downstrokes!")
                    print("""1 & 2 & 3 & 4 &
                             D U D U   U D U""")
                    countdown_section(time_mini_theory_section/3)
                    continue

                    
        elif chosen_theory_segment == 1:
                print ("You've chosen Musical time signatures")
                
                print ("If you don't know what musical time signatures are, google this out and get familiar https://duckduckgo.com/?q=Musical+time+signatures+guitar+how+to+exercise&ia=web")
                print ("Essentially, different style use different time signatures, for example most western/pop music uses 4/4 signatures\n")            
                print("[0] Simple Time")
                print("[1] Compound Time")
                print("[2] Irregular Time")

        
                chosen_time_signature_type = int(input("Choose the time signature type you want to practice by inputting 0-3")) 
                if chosen_time_signature_type == 0:
                    for i in range(0,3):
                        time_signatures=["4/4","3/4","2/4","2/2","2/1"]
                        random_time_signature = random.choice(time_signatures)
                        print("Time for -->" + random_time_signature + "<-- time signature")
                     
                        countdown_section(time_mini_theory_section/3) 
                
                if chosen_theory_segment == 2:
                    for i in range(0,3):
                        time_signatures=["6/8","9/8","12/8"]
                        random_time_signature = random.choice(time_signatures)
                        print("Time for -->" + random_time_signature + "<-- time signature")
                    
                        countdown_section(time_mini_theory_section/3)
                
                if chosen_theory_segment == 2:
                    for i in range(0,3):
                        time_signatures=["5/8","7/8"]
                        random_time_signature = random.choice(time_signatures)
                        print("Time for -->" + random_time_signature + "<-- time signature")
                         
                        countdown_section(time_mini_theory_section/3)
        elif chosen_theory_segment == 2:
            print("You've chosen Localising notes on the neck")
            all_notes=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
            time_localising_notes=25
            start_time = time.time()
            lv = 0
            while True:
                if lv == 5:
                    if time.time() >= time_mini_theory_section:
                        break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        random_note = random.choice(all_notes)
                        print(random_note)
                        countdown_section(time_localising_notes)
                        lv = 0
                        lv+=1
            
        elif chosen_theory_segment == 3:
            print("You've chosen Intervals between notes")
            all_notes=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
            intervals_possible=["minor 2nd","Major 2nd","minor 3rd","Major 3rd","Perfect 4th","tritone","Perfect 5th","minor 6th","Major 6th","minor 7th / dominant 7th","major 7th","octave"]
            time_intervals = 25
            lv = 0
            while True:
                if lv == 5:
                    if time.time() >= time_mini_theory_section:
                        break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        random_interval = random.choice(intervals_possible)
                        random_note = random.choice(all_notes)
                        print(random_note + ": " + random_interval)
                        countdown_section(time_intervals)
                        lv = 0
                        lv+=1
            
        else:
            "You didn't supplied valid number/value"
        

        # print("""Beginners should focus on Basic Rhythm, Musical time signatures, Localising notes on the neck, Intervals between notes
        #        It's in some way pointless for me to explain everything, if you don't know what these abilities are, you should google or watch videos about them on youtube! If you know what they mean, then it's still pointless for me to give further explanation REMEMBER TO MAKE IT PRACTICAL AND PLAY ON THE GUITAR""")
            countdown_section(time_section)
    if theory_level == False:
        print("[0] Building Chords")
        print("[1] Localising the Chords on the neck")
        print("[2] Finding chord grips with more creativity")
        print("[3] Modal Harmony")

        # print("""Intermediate players should focus on: Building Chords, Localising the Chords Notes on the neck, Finding chord grips with more creativity, Modal Harmony
        #        It's in some way pointless for me to explain everything, if you don't know what these abilities are, you should google or watch videos about them on youtube! If you know what they mean, then it's still pointless for me to give further explanation. REMEMBER TO MAKE IT PRACTICAL AND PLAY ON THE GUITAR!""")
        countdown_section(time_section)


def IMPROVISATION(time_section):
    if wants_improvisation == True:
        print("It's time for the improvisation")
        countdown_section(time_section)
    else:
        return 0


main()
