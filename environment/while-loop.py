import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


isGuessRight = False
correct_number = 5  # You can set this to any number between 1 and 10

# Start the guessing loop
while not isGuessRight:
    # Prompt the user for a guess
    guess = input("Guess a number between 1 and 10: ")
    
    # Convert guess to an integer
    guess = int(guess)
    
    # Check if the guess is correct
    if guess == correct_number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True  # Exit the loop
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
    


