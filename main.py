import random

#choose a randome number
n = random.randint(1,1000)


# maximum number of guesses
guess = 10

found = False
while guess > 0:
    check = int(input())
    if check == n:
        print("You Found the Number, You Won!")
        found = True
        break
    elif check > n:
        print("You guessed a larger number")
    else:
        print("You guessed a smaller number")
    
    guess -= 1

if found == False:
    print("Number of guesses are over, You lose!")


     
