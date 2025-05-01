''' I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
17
Your guess is too high.
Take a guess.
16
Good job! You guessed my number in 4 guesses!
'''



import random

print("I am thinking of a number between 1 and 20")
machine_guess = random.randint(1,10)


while True:

    print("Take a guess")
    user_guess = int(input())

    if user_guess == machine_guess:
        print("Good job! You guessed my number in {} guesses!".format(user_guess))
        print(user_guess)
        break;

    elif user_guess > machine_guess:
        print("Your guess is too high")
        print(user_guess)

    elif user_guess < machine_guess:
        print("Your guess is too low")
        print(user_guess)
