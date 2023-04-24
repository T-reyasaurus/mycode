#!/usr/bin/python3
"""Final Project for TLG"""

birthdays = {
        "Mom": "February 12",
        "Dad": "March 2",
        "Sandy" : "October 7"
        }

def add_birthday():
    name = input("Enter name: ").title()
    date = input("Enter birthday (MM/DD): ")
    birthdays[name] = date
    print(name, "'s birthday has been added to the database.")

def delete_birthday():
    name = input("Enter name to delete: ").title()
    if name in birthdays.keys():
        del birthdays[name]
        print(name, "'s birthday has been deleted from the database.")
    else:
        print("I didn't find that name.")

def main():
    print("Hello Trey! Who's birthday do you want to check on?")
    while True:
        name = input(">").title()
        if name in birthdays.keys():
            print(birthdays[name])
        elif name == "Q":
            print("Come back if you have a birthday to check on")
            break
        elif name == "Add":
            add_birthday()
        elif name == "Delete":
            delete_birthday()
        else:
            print("I didn't find that name.")

if __name__ == "__main__":
    main()
