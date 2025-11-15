import random

class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
    #next function takes input as int
    def __str__(self):
        return (f'this is my game and the answer is {self.answer}')

    def guess(self, user_guess):
        # could also apply ternary operator here:
        # print('high' if user_guess > GuessingGame.answer 
        #       else 'low' if user_guess < GuessingGame.answer
        #       else 'correct')
        if user_guess > self.answer:
            print("Too high")
        elif user_guess < self.answer:
            print("Too low")
        else:
            print("WINNER")
    def solved(self, last_guess):
        if last_guess == self.answer:
            return True
        else:
            return False
    

game = GuessingGame(10)
last_guess  = 0
last_result = game.solved(last_guess)
count = 0

print("Hello, and welcome to the secret number Guessing Game")

while game.solved(last_guess) == False:

    #   added counter to skip printing the "oops" line on the first play
    if last_guess != True and count > 0: 
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")

    last_guess  = int(input("Enter your guess: "))
    last_result == game.guess(last_guess)
    count += 1
print(f"You guessed {last_guess}, that's correct!")
  

