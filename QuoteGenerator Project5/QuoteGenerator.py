import random

# Predefined list of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "Do what you can with all you have, wherever you are. – Theodore Roosevelt",
    "Believe you can and you’re halfway there. – Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson"
]

def display_random_quote():
    # Select and display a random quote from the list
    return random.choice(quotes) 

def main():
    print("**Random Quote Generator**")
    
    while True:
        # Display a random quote
        print("\n💡 Quote of the Moment:")
        print(f"\"{display_random_quote()}\"")
        
        # Ask if user wants another quote
        choice = input("\nDo you want another quote? (y/n): ").lower()
        if choice != "y":
            print("Thanks for using Random Quote Generator. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
