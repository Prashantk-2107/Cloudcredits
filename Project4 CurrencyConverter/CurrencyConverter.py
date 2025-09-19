import requests

# Function to fetch exchange rates from API
def get_exchange_rates(base_currency="USD"):
    try:
        # Using ExchangeRate-API (Free tier example endpoint)
        url = f"https://open.er-api.com/v6/latest/{base_currency}"
        response = requests.get(url) # Make a GET request to the API
        data = response.json() # Parse JSON response

        if data["result"] == "success":
            # print(data["rates"])
            return data["rates"]
        
        else:
            print("Error fetching exchange rates:", data.get("error-type", "Unknown error"))
            return None
    except Exception as e:
        print("Error:", e)
        return None


# Function to convert currency
def convert_currency(amount, from_currency, to_currency, rates):
    try:
        if from_currency not in rates or to_currency not in rates:
            return None
        # Convert from base to USD, then to target currency
        usd_amount = amount / rates[from_currency] # Convert to USD first
        converted_amount = usd_amount * rates[to_currency] # Convert to target currency
        return converted_amount
    except Exception as e:
        print("Conversion error:", e)
        return None


def main():
    print("===== Currency Converter =====")

    # Fetch rates once at start
    rates = get_exchange_rates("USD")
    if not rates:
        print("Could not fetch exchange rates. Exiting.")
        return

    while True:
        try:
            amount = float(input("\nEnter amount to convert: "))
            from_currency = input("Enter source currency (e.g., USD, INR, EUR): ").upper()
            to_currency = input("Enter target currency (e.g., USD, INR, EUR): ").upper()
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        result = convert_currency(amount, from_currency, to_currency, rates)
        if result is None:
            print("Invalid currency code or conversion error.")
        else:
            # Format output smartly (int if whole, else 2 decimals)
            result = int(result) if result.is_integer() else round(result, 2)
            print(f"{amount} {from_currency} = {result} {to_currency}")

        # Ask to continue or exit
        choice = input("\nDo you want to convert again? (y/n): ").lower()
        if choice != "y":
            print("Exiting Currency Converter. Goodbye!")
            break


if __name__ == "__main__":
    main()
