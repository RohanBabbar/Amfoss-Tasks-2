import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    # new = guess.islower()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
# print(toss)
if toss == 0:
    if guess.islower() == "tails":
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if toss == 0:
            if guess.islower() == "tails":
                print('You got it!')
            else:
                print('Nope. You are really bad at this game.')
else:
    if guess.islower() == "heads":
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if toss == 1:
            if guess.islower() == "heads":
                print('You got it!')
            else:
                print('Nope. You are really bad at this game.')