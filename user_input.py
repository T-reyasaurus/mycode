#!/usr/bin/python3
"""Trey's example of user input"""

def print_hello(user_name):
    print(f"Hello, {user_name}!")

def main():
    """run-time"""
    name = input("What is your name?")
    print_hello(name)
if __name__== "__main__":
    main()
