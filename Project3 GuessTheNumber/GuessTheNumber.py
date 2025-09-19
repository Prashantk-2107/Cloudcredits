import random # Importing random module to generate random numbers

def guess_the_number(): # Main function for the game
    print("Guess The Number Game")
    
    # Let user choose difficulty level
    print("Choose difficulty level:")
    print("1. Easy (Range: 1-10, 5 attempts)")
    print("2. Medium (Range: 1-50, 7 attempts)")
    print("3. Hard (Range: 1-100, 10 attempts)")
    # Only allow valid inputs for difficulty level
    while True:
        difficulty = input("Enter choice (1/2/3): ")
        if difficulty == "1":
            number = random.randint(1, 10)
            attempts = 5
            break
        elif difficulty == "2":
            number = random.randint(1, 50)
            attempts = 7
            break
        elif difficulty == "3":
            number = random.randint(1, 100)
            attempts = 10
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
    
    print(f"\nI have selected a number. Try to guess it! You have {attempts} attempts.")
    
    # Start guessing loop
    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if guess == number:
            print(f"Congratulations! You guessed it right. The number was {number}.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        attempts -= 1
        print(f"Attempts left: {attempts}")
    
    else:  # This else runs if while loop ends without 'break'
        print(f"Game Over! You’ve used all your attempts. The number was {number}.")

if __name__ == "__main__": # Entry point of the program
    guess_the_number()
