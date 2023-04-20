#!/usr/bin/python3
"""Lab45 Challenge: Farm Loops"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
NE_animals = farms[0]["agriculture"]
#choice = input("Choose a farm (NE Farm, W Farm, or SE Farm)--> ")

def main():

#for i in NE_animals:
#    print(i)
    for farm in farms:
        print("-", farm["name"])
    choice= input("Pick a farm!\n")
      continue
    
    for farm in farms:
        if farm["name"].lower() == choice.lower:
             print(choice)
if __name__ == "__main__":
    main()
    # you do the rest!

