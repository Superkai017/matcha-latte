#module
import random
#category of words for guess 
animals = ['elehant', 'lion', 'tiger', 'giraffe', 'zebra', 'monkey', 'panda', 'kangaroo', 'bear', 'wolf']
fruits = ['apple', 'banana', 'orange', 'grape', 'mango', 'peach', 'pear', 'plum', 'kiwi', 'melon']
stationary = ['pen', 'pencil', 'notebook', 'eraser', 'ruler', 'sharpener', 'marker', 'highlighter', 'stapler', 'tape']
words = animals + fruits + stationary
#random is picked from words list
random_word = random.choice(words)
#give a hint if random_word in one of three lists
print('word guessing game')
if random_word in animals:
    print('Hint:it is animal')
elif random_word in fruits:
    print('Hint:it is fruit')
else: 
    print('Hint:it is stationary')
#initiallize condition
ug = ''
ch= 5
#condition using while loop
while ch > 0:
    worng_guess = 0
    for c in random_word:
        if c in ug:
            print(c, end = ' ')
        else:
            worng_guess += 1
            print('_', end = ' ')
    if worng_guess == 0:
        print('\ncongrats.You won. the word is', random_word)
        break
    #user input
    guess = input('\nmake a guess:')
    if guess in ug:
      print("You already guessed that letter! Try again.")
    
    ug += guess
    #condition if guess is worng
    if guess not in random_word:
        ch-= 1
        print(f'worng you have {ch} more chance')
        if ch == 0:
            print('game is over the word is', random_word)
   

    

