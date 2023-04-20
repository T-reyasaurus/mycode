#!/usr/bin/python3
"""Lab Challenge: Range Practice"""

def main():

    beer = int(input("How many beers on the wall? "))
    for i in range(beer, 0, -1):
        if i > 99:
            print(f"That's too much beer! We have to drive home! Try again")
            break
        if i > 1:
                print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
                print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        elif i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall.")
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")


if __name__ == "__main__":
    main()

