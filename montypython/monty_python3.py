#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

def main():
    
    round = 0
    answer = " "

    while round < 3 and answer != "Trey":
        round += 1     # increase the round counter by 1
        answer = input('Who is Candy\'s favorite child? ______:\n')
        answer = answer.capitalize() # this line inserted to line 8 will make all 
                                     # user input start with an uppercase
        if answer == "Trey": # logic to check if user gave correct answer
            print("Correct!")
        elif answer == "None":
            print("You found the super secret answer! But we know the truth :)")
        elif round == 3:    # logic to ensure round has not yet reached 3
            print("Sorry, the answer was Trey.")
        else:                 # if answer was wrong
            print("Sorry. Try again!")

if __name__ == "__main__":
    main()

