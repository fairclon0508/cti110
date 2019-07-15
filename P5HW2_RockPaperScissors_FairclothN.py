# Rock, paper, scissors
# 7/14/2019     
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Faircloth, N
#
import random

def main():
        while True:
                main_game()
                
def main_game():
        comp = random.randint(0, 2)
        moves = ['rock', 'paper', 'scissors']
        comp = moves[comp]
        user = str.lower(input('Enter rock, paper, or scissors: '))
        while user != 'rock' and user != 'paper' and user != 'scissors':
                user = str.lower(input('Valid inputs are rock, paper, or scissors: '))
        moves = ['rock', 'paper', 'scissors']
        print('Computer chose', comp)
        if user == comp:
                print('Tie.')
        if user == 'rock' and comp == 'paper':
                print('Computer wins.')
        if user == 'rock' and comp == 'scissors':
                print('You win!.')
        if user == 'paper' and comp == 'rock':
                print('You win!.')
        if user == 'paper' and comp == 'scissors':
                print('Computer wins.')
        if user == 'scissors' and comp == 'paper':
                print('You win!.')
        if user == 'scissors' and comp == 'rock':
                print('Computer wins.')
                
main()
