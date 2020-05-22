import random

def win():
    while True:
        answer = input('Do you want to play again. \n Press Y/y to play again, Press N/n to quit')
        if answer.upper() == 'Y':
            return answer.upper()
        elif answer.upper() == 'N':
            return answer.upper()
        else:
            print('Please provide a proper response!')
            continue

def proper_input():
    while True:
        try:
            guesses.append(int(input('Keep guessing the number:')))
        except:
            print('Provide a proper integer')
            continue
        else:
            return guesses
def end():
    while True:
        guesses = proper_input()
        if abs(guesses[-1]) == random_integer:
            print('Congratulations, you have guessed the number!')
            ans = win()
            return ans  
        elif abs(guesses[-1] - random_integer) > abs(guesses[-2] - random_integer):
            print('Colder')
        elif abs(guesses[-1] - random_integer) < abs(guesses[-2] - random_integer):
            print('Warmer')
        elif abs(guesses[-1] - random_integer) == abs(guesses[-2] - random_integer):
            print('You are a equal distance from the number as you were before this guess')
        elif abs(guesses[-1] - guesses[-2]) == 0:
            print('You have typed the same integer again, please provide a new integer')
            continue


print("welcome to the game\n i will pick any random integer between 1 and 100, including 1, 100 and u have to try to guess it.\n On the first guess if your guess is within 10 bounds of the number, i will say 'WARM' and if it isnt i will say 'COOl'\n Then keep on guessing and i will say warmer and cooler if u come close to the number or go away from the number")

random_integer = random.randint(1,100)

while True:
    try:
        guess = int(input("Pick a integer:"))
    except:
        print("Please enter a proper integer")
        continue
    else:
        if guess<1 or guess>100:
            print('OUT OF BOUNDS')
            continue
        else:
            if abs(guess - random_integer) <= 10 and guess != random_integer:
                print('WARM')
                guesses = [guess]
                ans = end()
                if ans == 'Y':
                    continue
                elif ans == 'N':
                    break
                
            elif guess == random_integer:
                print('congratulations, you have guessed the number!')
                ans = win()
                if ans == 'Y':
                    continue
                elif ans == 'N':
                    break  
            else:
                print('COOL')
                guesses = [guess]
                ans = end()
                if ans == 'Y':
                    continue
                elif ans == 'N':
                    break
