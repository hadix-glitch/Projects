import random
def create_number_guesser():
    """interactive number guessing game"""
    print("Guess a number between 1 and 100. I will indicate higher or lower and when you get the correct answer.")
    rand_number=random.randint(1,100)
    guess=None
    while rand_number != guess:
        s = input("Your guess:")
        guess = int(s)
        if guess < rand_number:
            print("Higher!")
        elif guess > rand_number:
            print("Lower!")
        else:
            ("CORRECT!".format(rand_number))

if __name__ == '__main__':
    create_number_guesser()




