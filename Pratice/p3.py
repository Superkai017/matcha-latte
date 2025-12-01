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
                   "/|\\"
                   "/ \\")}
def display_man(worng_guesses):
    print("*"*11)
def display_hint(hint):
    pass
def display_answer(answer):
    pass
def main():
    answer = random.choice(word)
    hint = ["_"] * len(answer)
    worng_guesses = 0
    guessed_letters = set()
    is_running = True
    while is_running:
        display_man(worng_guesses)
        display_hint(hint)
        guess = input("enter a letter: ").lower()
if __name__ == "__main__":
    main()