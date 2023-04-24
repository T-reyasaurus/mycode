#!/usr/bin/python3
"""Lab45 Challenge: Farm Loops"""
farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]
yuck= ["carrots", "celery"]

for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
         for ag_item in farm["agriculture"]:
                 print(ag_item)
