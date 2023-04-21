#!/usr/bin/python3
"""Final Project for TLG"""

birthdays = {
        "Mom": "February 12",
        "Dad": "March 2",
        "Sandy" : "October 7"
        }

def main():
    print("Hello Trey! Who's birthday do you want to check on?")
    name = " "
    while name != "q":
        name = input(">")
        if name in birthdays.keys(): 
            print(birthdays[name])
        else:
            print("I didn't find that name.")

if __name__ == "__main__":
    main()
