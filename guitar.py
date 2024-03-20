import random
from enum import Enum
import timer
import time
import os

class TheoryLevel(Enum):
    BASIC = 1
    INTERMEDIATE = 2
    ADVANCED = 3

class Section(Enum):
    TECHNIQUE = 1
    TRANSCRIBING = 2
    REPERTOIRE = 3
    KNOWLEDGE = 4
    IMPROVISATION = 5


def main():
    try: 
        include_improvisation = wants_improvisation()
        time_total = declaring_time_total()
        time_technique, time_repertoire, time_section = calculate_time_section(time_total, include_improvisation)
        TECHNIQUE(time_technique)
        REPERTOIRE(time_repertoire)
        TRANSCRIBING(time_section)
        KNOWLEDGE(time_section)
        IMPROVISATION(time_section)
        SINGING(30*60)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")

def print_and_sleep(message, sleep_time=3):
    print(message)
    time.sleep(sleep_time)

def calculate_time_section(time_total, include_improvisation):
    """Calculates the time for each section based on total time and whether improvisation is included."""
    time_technique = time_total * 0.33
    time_repertoire = time_total * 0.33
    num_sections = len(Section) - 1 if not include_improvisation else len(Section)
    time_section = (time_total - time_technique - time_repertoire) / num_sections
    return time_technique, time_repertoire, time_section


def declaring_time_total():
    while True:
        try:
            time_total = int(input("How much time do you want to plan practicing? (Type in minutes!): "))
            return time_total * 60
        except ValueError:
            print("Invalid input. Please enter an integer.")

def wants_improvisation():
    """Asks the user if they want to include improvisation in their routine."""
    while True:
        try:
            impro_yes_no = input("Do you want to include improvisation in this routine? [True/False]: ")
            return impro_yes_no.strip().upper().startswith('T')
        except ValueError:
            print("Invalid input. Please enter T/F or True/False")


def theory_level():
    theory_level_int = 1
    theory_level_int = int(
        input("""What is your level in theory knowledge from 1 to 10?(default - '1'): """))
    if theory_level_int <= 5:
        return True
    elif theory_level_int >= 5:
        return False
    else:
        return False

def bold_text(text):
    return "\033[1m" + text + "\033[0m"

def TECHNIQUE(time_technique):
    time_mini_section = time_technique / 4
    # Spider exercises
    print_and_sleep("Let's do " + bold_text("Spider Patterns") + " \n")
    print("If you don't here's a link - http://www.diegoruizguitar.com/tabs/8-Guitar-Spider-Warm-Up-Exercises-x-Diego-Ruiz.pdf ")

    timer.countdown_section(time_mini_section)
    # Scale Picking
    print("It's time for  " + bold_text("Scale Picking") + "\n")
    print("You must remember that there are 3 systems of playing Scales: CAGED System, 3 notes per string,  ")
    print("Choose the difficult level: ")
    scale_difficulty = input(
        "Do you want Beginner or Intermediate scales? [B/I]: ")
    if scale_difficulty.strip().upper().startswith("B"):
        print("BEGINNER:")
        # Define the scales
        scales = {
            'Major': ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
            'Minor': ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        }

        # Randomly choose between Major and Minor
        scale_type = random.choice(['Major', 'Minor'])

        # Randomly pick two scales of the chosen type
        chosen_scales = random.sample(scales[scale_type], 2)

        print(f"Chosen scale type: {scale_type}")
        print(f"Chosen scales: {chosen_scales}")
        
        timer.countdown_section(time_mini_section)
    elif scale_difficulty.strip().upper().startswith("I"):
        
        print("INTERMEDIATE:")
        
    else:
        print("Invalid input. Please enter either 'B' for Beginner or 'I' for Intermediate.")
    # Random Technique
    other_techniques = {
        "Hybrid Picking": "\nThis technique involves using both the pick and the fingers to pluck the strings. Practice it by playing a simple melody or chord progression.",
        "Chord Changes": "\nThis involves changing from one chord to another. Practice it by picking two chords and switching between them.",
        "Finger Tapping": "\nThis technique involves tapping the strings with the fingers of the picking hand. Practice it by tapping out a simple melody on one string.",
        "Arpeggios": "\nThis is a technique where you play the notes of a chord one by one. Practice it by choosing a chord and playing its notes in order.",
        "Bending": "\nThis technique involves bending the string to raise the pitch. Practice it by playing a note and then bending the string to reach the next note.",
        "Sliding": "\nThis involves sliding from one note to another. Practice it by playing a note and then sliding your finger to the next note without lifting it.",
        "Hammer Ons": "\nThis technique involves tapping a string hard enough to create a note. Practice it by picking a note and then hammering on to a higher note.",
        "Pull Offs": "\nThis is the opposite of a hammer on, where you pluck a string by pulling your finger off. Practice it by picking a note and then pulling off to a lower note.",
        "Vibrato": "\nThis involves rapidly bending a string back and forth to create a vibrating effect. Practice it by playing a note and then applying the vibrato.",
        "Palm Muting": "\nThis technique involves resting the palm of the picking hand on the strings to mute them. Practice it by playing a riff or chord progression with palm muting.",
        "Sweep Picking": "\nThis technique involves playing a series of notes on consecutive strings with a 'sweeping' motion of the pick. Practice it by playing an arpeggio with a sweeping motion.",
        "Alternate Picking": "\nThis involves alternating downstrokes and upstrokes. Practice it by playing a scale or melody using alternate picking.",
        "String Skipping": "\nThis technique involves skipping over strings when playing. Practice it by playing a scale or melody that requires you to skip strings.",
        "Natural Harmonics": "\nThese are the bell-like sounds that occur at certain points on the strings. Practice it by lightly touching a string at a harmonic point and plucking it.",
        "Tremolo Picking": "\nThis involves picking a string rapidly. Practice it by choosing a note and picking it as fast as you can.",
        "Double Stops": "\nThis involves playing two notes simultaneously. Practice it by playing a melody that includes double stops.",
        "Artificial Harmonics": "\nThis involves creating harmonics at points where they don't naturally occur. Practice it by lightly touching a string at a non-natural harmonic point and plucking it."
    }

    random_other_technique, technique_explanation = random.choice(list(other_techniques.items()))
    print_and_sleep("Let's do " + bold_text(random_other_technique) + ".\n " + technique_explanation + "\n")

    timer.countdown_section(time_mini_section) 

    random_other_technique, technique_explanation = random.choice(list(other_techniques.items()))
    print_and_sleep("Let's do " + bold_text(random_other_technique) + ".\n " + technique_explanation + "\n")
    
    timer.countdown_section(time_mini_section) 

def TRANSCRIBING(time_section):
    print(" " + bold_text("TRANSCRIBING") + " section\n")
    print("Download songs that you want to transcribe and put them into the software called 'transcribe'!")
    os.system('sonic-visualiser &')
    os.system('musescore &')
    timer.countdown_section(time_section)


def REPERTOIRE(time_section):
    print("It's time for  " + bold_text("REPERTOIRE") + " section\n")
    print("Choose one that is: \n")
    print("- BBQ Song - A simple song that you might play at a party after a few beers \n")
    print("- Solo Song - Songs that would sound good without accompaniment \n")
    print("- Band Songs - Songs that you should learn intensely and to learn the whole song, not only some bits! \n")
    print("- Advanced Songs - When you get to advanced level, you should stop learning BBQ songs and head over into some advanced stuff!")
    timer.countdown_section(time_section)


def KNOWLEDGE(time_section):
    print("It's time for  " + bold_text("KNOWLEDGE") + " section : \n")
    print("This is supposed to be practical practice of music theory (sounds weird, I know!) \n")
    print("So in this section, you should always be having your guitar equipped \n")
    global theory_level
    theory_level = theory_level()
    if theory_level == True:
        print("[0] Basic Rhythm")
        print("[1] Musical time signatures")
        print("[2] Localising notes on the neck")
        print("[3] Intervals between notes")

        time_mini_theory_section = time_section/2
        
        chosen_theory_segment = int(
            input("Choose the first theory practice segment by inputting 0-3: "))
        second_chosen_theory_segment = int(
            input("Choose the second theory practice segment by inputting 0-3: "))

        for i in range (2):
            if chosen_theory_segment == 0:
                print("You've chosen Basic Rhythm practice")
                strumming_patters = [1, 2, 3, 4, 5]
                print("We'll begin with the most basic pattern: \n")
                print("""1 & 2 & 3 & 4 &""")
                print("""D   D   D   D""")
                print("""This might sound easy, however, you need to keep the tempo even! 
                    I suggest you lowering the tempo, this would make this exercise more challenging and productive! Doing it slowly and accurate!
                    And another tip: YOU NEED to keep the up and down hand motion going non-stop!""")
                timer.countdown_section(time_mini_theory_section/3)
                for i in range(0,2):
                    random_strumming_patterns = random.choice(strumming_patters) 
                    strumming_patters = [2, 3, 4, 5]
                    if random_strumming_patterns == 2:
                        print("Time for Upstrokes strumming on 'AND', so we're strumming up additionaly! ")
                        print("""1 & 2 & 3 & 4 &""")
                        print("""D U D U D U D U""")
                        timer.countdown_section(time_mini_theory_section/3)
                        continue
                    elif random_strumming_patterns == 3:
                        print("Time for Muted strumming on second, fourth beat or whichever you like")
                        print("""1 & 2 & 3 & 4 &""")
                        print("""D U M U D U M U""")
                        timer.countdown_section(time_mini_theory_section/3)
                        continue
                    elif random_strumming_patterns == 4:
                        print("Resting some of the counts (not strumming them)")
                        print("""1 & 2 & 3 & 4 &""")
                        print("""D U   U D U   U""")
                        timer.countdown_section(time_mini_theory_section/3)
                        continue
                    elif random_strumming_patterns == 5:
                        print("Resting the Downstrokes!")
                        print("""1 & 2 & 3 & 4 &""")
                        print("""D U D U   U D U""")
                        timer.countdown_section(time_mini_theory_section/3)
                        continue

                        
            elif chosen_theory_segment == 1:
                print("You've chosen Musical time signatures")
                
                print("If you don't know what musical time signatures are, google this out and get familiar https://duckduckgo.com/?q=Musical+time+signatures+guitar+how+to+exercise&ia=web")
                print("Essentially, different style use different time signatures, for example most western/pop music uses 4/4 signatures\n")            
                print("[0] Simple Time")
                print("[1] Compound Time")
                print("[2] Irregular Time")

        
                chosen_time_signature_type = int(input("Choose the time signature type you want to practice by inputting 0-3: ")) 
                if chosen_time_signature_type == 0:
                    for i in range(0,3):
                        time_signatures=["4/4","3/4","2/4","2/2","2/1"]
                        random_time_signature = random.choice(time_signatures)
                        print(f"Time for -->{random_time_signature}<-- time signature")
                    
                        timer.countdown_section(time_mini_theory_section/3) 
                
                if chosen_theory_segment == 1:
                    for i in range(0,3):
                        time_signatures=["6/8","9/8","12/8"]
                        random_time_signature = random.choice(time_signatures)
                        print(f"Time for -->{random_time_signature}<-- time signature")
                    
                        timer.countdown_section(time_mini_theory_section/3)
                
                if chosen_theory_segment == 2:
                    for i in range(0,3):
                        time_signatures=["5/8","7/8"]
                        random_time_signature = random.choice(time_signatures)
                        print(f"Time for -->{random_time_signature}<-- time signature")
                        
                        timer.countdown_section(time_mini_theory_section/3)
            elif chosen_theory_segment == 2:
                print("You've chosen Localising notes on the neck")
                all_notes=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
                time_localising_notes=25
                total_lvs= float(time_mini_theory_section/25)
                lv = 0
                while True:
                    if lv >= total_lvs:
                        break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        random_note = random.choice(all_notes)
                        print(random_note)
                        timer.countdown_section(time_localising_notes)
                        lv+=1
                
            elif chosen_theory_segment == 3:
                print("You've chosen Intervals between notes")
                all_notes=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
                intervals_possible=["minor 2nd","Major 2nd","minor 3rd","Major 3rd","Perfect 4th","tritone","Perfect 5th","minor 6th","Major 6th","minor 7th / dominant 7th","major 7th","octave"]
                time_intervals = 25
                total_lvs= float(time_mini_theory_section/25)
                lv = 0
                while True:
                    if lv >= total_lvs:
                        break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        random_interval = random.choice(intervals_possible)
                        random_note = random.choice(all_notes)
                        print(random_note + ": " + random_interval)
                        timer.countdown_section(time_intervals)
                        lv+=1
            chosen_theory_segment=second_chosen_theory_segment
        else:
            "You didn't supplied valid number/value"
        
        
    if theory_level == False:
        print("[0] Building Chords")
        print("[1] Localising the Chords on the neck")
        print("[2] Finding chord grips with more creativity")
        print("[3] Modal Harmony")

        # print("""Intermediate players should focus on: Building Chords, Localising the Chords Notes on the neck, Finding chord grips with more creativity, Modal Harmony
        #        It's in some way pointless for me to explain everything, if you don't know what these abilities are, you should google or watch videos about them on youtube! If you know what they mean, then it's still pointless for me to give further explanation. REMEMBER TO MAKE IT PRACTICAL AND PLAY ON THE GUITAR!""")
        timer.countdown_section(time_section)


def IMPROVISATION(time_section):
    if wants_improvisation == True:
        print("It's time for the  " + bold_text("IMPROVISATION") + "\n")
        timer.countdown_section(time_section)
    else:
        return 0

def SINGING(time_section):
    if wants_improvisation == True:
        print("It's time for " + bold_text("SINGING") + "\n")
        timer.countdown_section(time_section)
    else:
        return 0

if __name__ == "__main__":
    main()