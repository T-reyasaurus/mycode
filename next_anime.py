#!/usr/bin/env python3
"""Mini-Project: Which anime to watch next"""

def main():

# print question
    print("Do you favor Action, Suspense,or Drama?")
    favor = input().lower()

# print question 2
    print("Do you prefer Short, Long, or Very long shows?")
    prefer = input().lower()

# combination of answers along with if/elif statements and results from input
    if favor=="action" and prefer=="long":
        print("DragonBall Z")
    elif favor=="action" and prefer=="short":
        print("One Punch Man")
    elif favor=="action" and prefer=="very long":
        print("One Piece")
    elif favor=="suspense" and prefer=="long":
        print("Code Geass") 
    elif favor=="suspense" and prefer=="short":
        print("Death Note")
    elif favor=="suspense" and prefer=="very long":
        print("Full Metal Alchemist")
    elif favor=="drama" and prefer=="long":
        print("Naruto")
    elif favor=="drama" and prefer=="short":
        print("HunterxHunter")
    elif favor=="drama" and prefer=="very long":
        print("Naruto Shippuden")

if __name__ == "__main__":
    main()




