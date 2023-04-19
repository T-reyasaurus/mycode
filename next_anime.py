#!/usr/bin/env python3
"""Mini-Project: Which anime to watch next"""

def main():

# print question
    favor = input("Do you favor --> (Action, Suspense, or Drama) in shows?\n").lower()

# print question 2
    prefer = input("Do you prefer --> (Short, Long, or Very long) shows?\n").lower()

# combination of answers along with if/elif statements and results from input
    if favor=="action" and prefer=="long":
        print("DragonBall Z is a great choice for a long and action packed anime!")
        print("Prepare for a binge worthy journey that'll take you a couple months to get thru!")
    elif favor=="action" and prefer=="short":
        print("One Punch Man is still ongoing, but it's 3 seasons and worth the watch")
        print("Prepare for a lot of one hit knockouts")
    elif favor=="action" and prefer=="very long":
        print("One Piece is loooooooooooooooooong, but a classic and has gotten better with time")
    elif favor=="suspense" and prefer=="long":
        print("Code Geass is a favorite. The suspense keeps you on the edge of your seat") 
    elif favor=="suspense" and prefer=="short":
        print("Death Note is a CLASSIC. Highly recommended for those new anime")
    elif favor=="suspense" and prefer=="very long":
        print("Full Metal Alchemist is another classic. It's long and also has movies that are great as well")
    elif favor=="drama" and prefer=="long":
        print("Naruto is very popular. It has a strong character development")
    elif favor=="drama" and prefer=="short":
        print("HunterxHunter is great go too for a fun anime to watch")
    elif favor=="drama" and prefer=="very long":
        print("Naruto Shippuden is fully extended from 'Naruto' and is that much better")
    else:
        print("You have to type a favor and prefence to recieve details that match your choices")
        print("Be sure to check your spelling. Don't worry about case")

if __name__ == "__main__":
    main()




