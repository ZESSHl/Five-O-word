import time
import sys
from word_check import check_words

# This block code is made using AI ChatGPT 5.1 (# End will mark how far the code is AI)
def definer(secret, guess):
    result = ["absent"] * len(secret) # makes the guessed word into separate characters like ["absent", "absent"] depending on how long the word is
    secret_list = list(secret)

    # checks for characters that are correct place
    for i, ch in enumerate(guess):
        if ch == secret[i]:
            result[i] = "correct"
            secret_list[i] = None

    # checks for character in word but not in place
    for i, ch in enumerate(guess):
        if result[i] == "correct":
            continue
        if ch in secret_list:
            result[i] = "present"
            secret_list[secret_list.index(ch)] = None

    return result

def arranger(guess, feedback):
    out = []
    for ch, status in zip(guess, feedback):
        if status == "correct":
            out.append(f"[{ch}]")   # for word sin correct spot in word
        elif status == "present":
            out.append(f"({ch})")   # for characters in word but in the wrong spot
        else:
            out.append(f" {ch} ")   # for characters not in word
    print(" ".join(out))
# End of the use of AI

# utilities? 

def start(words):
    secret = words.random_word()
    max_try = 0 
    start_time = time.time()
    print("Medium difficulty started!")
    print("You get 5 tries.")


    while max_try < 5:
        player_guess = input("Input your word: ")
        guess = player_guess.upper()

        # require 5 letter words no more no less, does not include into tries
        if len(guess) != len(secret):
            print(f"Please enter a {len(secret)}-letter word.")
            continue

        # make sure the player can't put in random words
        if guess not in check_words:
            print("Sorry, word is not in our dictionary")
            print("Try again")
            continue

        # win condition
        if guess == secret:
            end_time = time.time()
            time_taken = end_time - start_time
            total_seconds = int(time_taken)

            minutes = total_seconds // 60
            seconds = total_seconds % 60

            print(f"Correct! time taken is {minutes} minutes and {seconds} seconds")
            while True:
                print(" ")
                print("Play again? ")
                print("1. Yes")
                print("2. No")
                print("3. Return to main menu")
                decide = input()

                if decide in ("1", "Yes", "yes"):
                    return start(words)
                elif decide in ("No", "no", "2"):
                    sys.exit()
                elif decide in ("Return", "Return to main", "Return to main menu", "3"):
                    return
                else:
                    print("Invalid Input")

        else:
            # passes a wrong guess to the top def definer and arranger
            feedback = definer(secret, guess)
            arranger(guess, feedback)

            max_try += 1
            tries_left = 5 - max_try

            if max_try < 5:
                print(f"Incorrect, you have {tries_left} tries left")

        # losing condition
        if max_try == 5 and guess != secret:
            end_time = time.time()
            time_taken = end_time - start_time
            total_seconds = int(time_taken)

            minutes = total_seconds // 60
            seconds = total_seconds % 60
            print(f"Nice try. Time taken is {minutes} minutes and {seconds} seconds.")
            print(f"The word is: {secret}")

            while True:
                print(" ")
                print("Play again? ")
                print("1. Yes")
                print("2. No")
                print("3. Return to main menu")
                decide = input()

                if decide in ("1", "Yes", "yes"):
                    return start(words)
                elif decide in ("No", "no", "2"):
                    sys.exit()
                elif decide in ("Return", "Return to main", "Return to main menu", "3"):
                    return
                else:
                    print("Invalid Input")
