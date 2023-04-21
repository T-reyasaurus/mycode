#!/usr/bin/python3
"""Lab 30: Import Module"""
import html

def main():


    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
    question= trivia["question"]
    D= trivia["correct_answer"]
    A= trivia["incorrect_answers"][0]
    B= trivia["incorrect_answers"][1]
    C= trivia["incorrect_answers"][2]


    print(f"{question}")
    print(f" A: {html.unescape(A)}?")
    print(f" B: {html.unescape(B)}?")
    print(f" C: {html.unescape(C)}?")
    print(f" D: {html.unescape(D)}?")
    choice= input("> ").capitalize()

    if choice == "D":
        print("You are correct!")
    else:
        print("Sorry, that's incorrect")
    print("Thank you for playing")

if __name__ == "__main__":
    main()
