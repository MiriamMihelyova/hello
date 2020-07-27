import random

def ready_to_guess(word, fails, name):
    repeat = True
    while repeat:
        print()
        word_answer = input("Are you ready to guess the whole word? (yes or no): ")
        if word_answer.lower() == "yes":
            word_guess = input("Guess the word: ")
            print()

            if word_guess == word:
                print(f"Congratulation,You won {name} ")
                turns = 0
                quit()l
            else:
                print("That's not the word.")
                fails += 1

            repeat = False
        elif word_answer.lower() == "no":
            None
            repeat = False
        else:
            print("You can answer just yes or no...!")
            repeat = True
