import random

number = random.randint(1,100)
counter = 0
guessing = True

print number

def is_number(guess):
    if type(guess) == int:
        return True
    else:
        return False
        

while True:
    guess = raw_input("Please pick a number between 1 and 100!")
    guess = int(guess)
    counter += 1
    if is_number(guess) == True:
        if guess < number:
            print "Too small!"
            if number - guess <= 5:
                print "So close!"
        elif guess > number:
            print "Too big!"
            if guess - number <= 5:
                print "So close!"
        else:
            print "Congratulations, it took you " + str(counter) + " tries!"
            guess = False
    else:
        print "Integer only please!"
