#!/usr/bin/python3
"""Simpson's Challenge"""

def main():

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

    print(f"My {list(trial[2].keys())[0]}! The {list(trial[2].keys())[1]} do {trial[3]}!")



if __name__ == "__main__":
    main()

