
import random
n = random.randint(1,10)
print("Random number between 1 and 10:")
attempts = 0
chance = 6
while True:
    guess = 0
    attempts += 1
    chance -= 1
    guess = int(input("Enter a guess: "))
    if guess < n:
        
        print(f"your guess low in {attempts} attempt you have {chance} chance left")
    elif guess > n:
        
        print(f"you are guees too high in {attempts} attempts you have {chance} chance left ")
    elif guess == n:
        print(f"you are guess is correct in {attempts} attempts. ")
        break
if  attempts < chance:
    print(f'Sorry! The number was {n}. Better luck next time.')
