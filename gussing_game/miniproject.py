# we are going to guess the number 
import random

def guess(x):
    random_number = random.randint()
    guess = 0

    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}:"))
        if guess < random_number:
            print("sorry , guess again ; too low ")
        elif guess > random_number:
            print("sorry, guess again ; too high")
    
    print(f"yah! you have guessed the {random_number} correct .")

    # computer will guess the number 

def computer_guess(X):
    low = 1
    high = X
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess =low # or it could be high
        feedback = input(f"is guess {guess} too high or too low or its correct (c)?")

        if feedback =='h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

    print(f"yeah the computer guess your number {guess} correctly")

# rock paper seasor 

def play():
    user = input("whats your choice ? 'r' for rock 'p' for paper and 's' for seasor \")
    computer  = random.choice(['r', 'p', 's'])


    if user == computer:
        return 'tie'

    if is_win(user , computer ):
        return 'You Won!'
    
    return 'You Lost '
    

    def is_win(player, opponent ):

        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
          or (player == 'p' and opponent == 'r'):
          return True 






