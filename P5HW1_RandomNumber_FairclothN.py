# Random Number Guessing Game
# 7/14/2019
# CTI-110 P5HW1 - Random Number
# Faircloth, N
#
import random

def mainloop():
        print('I\'m thinking of a number between 1 and 100.  Can you guess it?')
        number = random.randint(1, 100)
        count = 0

        #get user input
        while True:
                guess = input('::')
                try:
                        guess = int(guess)
                except:
                        print('Error: must be a whole number')
                        return 1
                count += 1

                #if guess less than number
                if guess < number:
                        print('Too low, try again')
                #if guess higher than number
                if guess > number:
                        print('Too high, try again')
                #if guess = number
                if guess == number:
                        print('Congratulations, you got the correct answer in ', count, ' tries.')
                        return 0

def main():
        while True:
                input('Press enter to start.')
                mainloop()

main()
