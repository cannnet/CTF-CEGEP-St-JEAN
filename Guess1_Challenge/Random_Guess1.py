random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            print("Number of attempts:", attempts)
		 print("You have almost found the answer!")
            print("Think of a common IP address range BASE in private networks:")
            print("MDEyNTNDVEZ7aDFkM2QtRmw0Z30=")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guess_number()
