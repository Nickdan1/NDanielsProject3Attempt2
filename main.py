#Nicholas Daniels
#project
#28 March 2022
import random

def main():
    user_input = input("what Fortune File would you like to open? ")
    user_input = user_input.lower()
    fortunes_loaded = load_fortunes(user_input)
    return fortunes_loaded


def load_fortunes(filename):
    fortunes = open(filename, "r")
    all_lines = fortunes.read()
    fortunes_into_list = all_lines.replace('\n', ' ').split(".")
    yes = "yes"
    yes = yes.lower()
    no = "no"
    no = no.lower()
    if display_fortune() == yes:
        print(random.choice(fortunes_into_list))
    elif display_fortune() == no:
        print("Thank you come again!")
        exit()
    else:
        exit()




def display_fortune():
    fortune = input("Would you like to see a fortune? ")
    fortune = fortune.lower()



main()
load_fortunes()
display_fortune()
