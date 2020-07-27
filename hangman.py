print("What's your name?")
name = input(">")
print(f"Let's start {name}.")

words = open("words.txt").read()
list = words.split()
word = random.choice(list)
word = word.lower()

minus_word = word
turns = 6
fails = 0
characters = len(word)
list_r_guesses = []
list_w_guesses = []
answer = "_" * characters



while turns > 0 and fails != 2:
    print()
    print(answer)

    print("Guess a letter: ")
    guess = input(">")

    if len(guess) > 1:
        print("Don't cheat! you can guess just one letter at the time")

    elif guess == "" or guess.isalpha() == False:
        print("You need to write a letter...")

    else:
        guess = guess.lower()
        print()

        turns -= 1

        if guess.lower() in word and guess.lower() not in list_r_guesses:
            print(f"Yes, that letter is in the word, you have {turns} turns left")

            list_r_guesses.append(guess)
            if word.count(guess) > 1:
                for i in range(word.count(guess)):
                    ind = minus_word.find(guess)
                    minus_word = minus_word[:ind] + "*" + minus_word[ind + 1:]

                    ind2 = minus_word.find("*")
                    answer = answer[:ind2] + guess + answer[ind2 + 1:]

                    minus_word = minus_word.replace("*", "-")



            else:
                ind = word.find(guess)
                answer = answer[:ind] + guess + answer[ind + 1:]
                minus_word = minus_word[:ind] + "-" + minus_word[ind + 1:]

            print(answer)
            D_hangman.ready_to_guess(word, fails, name)

        elif guess.lower() not in word and guess.lower() not in list_w_guesses :
            print("That letter is not in the word")
            print(f"You have {turns} turns left")
            list_w_guesses.append(guess)


        elif len(guess) > 1:
            print("Don't cheat! you can guess just one letter at the time")

        else:
            print("You already tried that letter")
        print()


print("You lose")
print(f"The right answer was: {word}")








