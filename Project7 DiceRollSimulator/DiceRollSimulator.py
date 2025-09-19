import random

def roll_dice(num_dice, num_sides):
# Function to roll dice and return results
    results = []
    for i in range(num_dice):
        roll = random.randint(1, num_sides)  # Random number between 1 and num_sides
        results.append(roll)
    return results

def main():
    print("**Welcome to the Dice Roll Simulator**")
    
    while True:
        try:
            # Take input from the user
            num_dice = int(input("Enter the number of dice to roll: "))
            num_sides = int(input("Enter the number of sides per dice: "))

            # Validate inputs
            if num_dice <= 0 or num_sides <= 1:
                print("Please enter valid values (dice > 0 and sides > 1).")
                continue

            # Roll the dice
            results = roll_dice(num_dice, num_sides)

            # Display results
            print("\nResults of the dice rolls:")
            for i, result in enumerate(results, start=1):
                print(f" Dice {i}: {result}")
            
            print(f"Total Sum: {sum(results)}")

        except ValueError:
            print("⚠️ Invalid input! Please enter integers only.")
            continue

        # Ask if user wants to play again
        choice = input("\nDo you want to roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye")
            break


if __name__ == "__main__":
    main()
