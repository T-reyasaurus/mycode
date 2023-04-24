#!/usr/bin/python3
"""Final Project for TLG"""

birthdays = {
        "Mom": "February 12",
        "Dad": "March 2",
        "Sandy" : "October 7"
        }

def main():
    while True:
        print("\nEnter '1' to look up a birthday")
        print("Enter '2' to add a new birthday")
        print("Enter '3' to delete a birthday")
        print("Enter '4' to show all birthdays")
        print("Enter 'q' to quit")
        choice = input("> ")

        if choice == "1":
            name = input("Enter a name to look up: ").title()
            if name in birthdays:
                print(f"{name}'s birthday is {birthdays[name]}")
            else:
                print(f"Sorry, {name} is not in the database")

        elif choice == "2":
            name = input("Enter a name to add: ").title()
            date = input("Enter their birthday: ")
            birthdays[name] = date
            print(f"{name}'s birthday has been added to the database")

        elif choice == "3":
            name = input("Enter a name to delete: ").title()
            if name in birthdays:
                del birthdays[name]
                print(f"{name}'s birthday has been deleted from the database")
            else:
                print(f"Sorry, {name} is not in the database")

        elif choice == "4":
            print("All birthdays in the database:")
            for name, bday in birthdays.items():
                print(f"{name}: {birthdays[name]}")

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again")
if __name__ == "__main__":
    main()
