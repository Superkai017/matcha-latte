import random
word = ("apple", "orange", "banana", "coconut", "pineapple")
hangman_art = {0:("  ",
                  "  ",
                  "  "
                  "  "),
                1:(" o ",
                    "   ",
                    "   "),
                2:(" o ",
                   " | "
                   "   "),
                3:(" o ",
                   "/| ",
                   "   "),
                4:(" o ",
                   "/|\\",
                   "   "),
                5:(" o ",
                   "/|\\",
                   "/  "),
                6:(" o ",
                   "/|\\",
                   "/ \\")}
def display_man(worng_guesses):
    print("*"*11)
    for line in hangman_art[worng_guesses]:
        print(line)
    print("*"*11)
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(word)
    hint = ["_"] * len(answer)

    wrong_guesses = 0          # <-- MUST be here inside main()
    guessed_letters = set()
    is_running = True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess          # FIX (was ==)
        else:
            wrong_guesses += 1               # FIX indentation

        # FIX: checks must be inside the while loop
        if "_" not in hint:
            display_man(wrong_guesses)
            print("Answer:", end=" ")
            display_answer(answer)
            print("you win")
            break

        if wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print("Answer:", end=" ")
            display_answer(answer)
            print("you lose")
            break

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
