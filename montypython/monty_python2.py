#!/usr/bin/python3
"""Lab 36: Using while, if, elif, else"""

def main():
    
    round = 0    # use a counter to control the loop

    while True: # simple loop to loop forever or until break
        round = round + 1    # increase the round counter
        print('Finish the movie title, "Monty Python\'s The Life of ______"')

        answer = input("Your guess--> ").title()    # strings answer collected from user

        if answer == 'Brian':               # logic to check if user gave correct answer
            print("Correct! You just won A MILLION.... Yay\'s!!!")
            break                           # break statement escapes the while loop

        elif round == 3:                    # logic to ensure round has not yet reached 3
            print("Sorry, the answer was Brian.")
            break

        else:                               # if answer was wrong, and round is not yet equal to 3
            print("Sorry! Try again!")

if __name__ == "__main__":
    main()
