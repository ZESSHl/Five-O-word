import word_list

def main():
    while True:
        print("Welcome to Five O'word!")
        print("A game of 1 word, 5 letters, limited tries")
        print("A letter encased in [] means it's in the right place") #example: [A]
        print("A letter encased in () means it's in the wrong spot") #example (A)
        print("A word not encased means the letter is not in the word") #example A
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Exit Game")

        choice = input("Enter number: ")

        # difficulty choice
        if choice == "1":
            import game_easy as game
            words = word_list
            game.start(words)
        elif choice == "2":
            import game_medium as game
            words = word_list
            game.start(words)
        elif choice == "3":
            import game_hard as game
            words = word_list
            game.start(words)
        elif choice == "4":
            print("Game Exited")
            exit()
        else:
            print("Invalid Input")


    # main.py will onlyactivate when player is in this file
if __name__ == "__main__":
    main()
