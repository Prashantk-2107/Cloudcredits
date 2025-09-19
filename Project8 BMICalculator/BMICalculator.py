# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi
# def bmi_category(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         return "Normal weight"
#     elif 25 <= bmi < 29.9:
#         return "Overweight"
#     else:
#         return "Obesity"
# def main():
#     while True:
#         print("Choose the unit system For Weight:")
#         print("1. Kilograms")
#         print("2. LBS")
#         weight_unit = input("Enter 1 or 2: ")
#         if weight_unit == '1':
#             weight = float(input("Enter your weight in kilograms: "))
#         elif weight_unit == '2':
#             weight = float(input("Enter your weight in pounds: "))
#             weight = weight * 0.453592  # Convert pounds to kilograms
#         else:
#             print("Invalid choice. Please try again.")
#             continue
#         print("Choose the unit system For Height:")
#         print("1. Meters")
#         print("2. Feet And Inches")
#         height_unit = input("Enter 1 or 2: ")
#         if height_unit == '1':
#             height = float(input("Enter your height in meters: "))
#         elif height_unit == '2':
#             feet = float(input("Enter your height in feet: "))
#             inches = float(input("Enter your height in inches: "))
#             height = (feet * 0.3048) + (inches * 0.0254)  # Convert feet and inches to meters
#         else:
#             print("Invalid choice. Please try again.")
#             continue
#         if height <= 0 or weight <= 0:
#             print("Height and weight must be positive values. Please try again.")
#             continue
#         else:
#             bmi = calculate_bmi(weight, height)
#             category = bmi_category(bmi)
#             print(f"Your BMI is: {bmi:.2f}")
#             print(f"You are categorized as: {category}")
#             print("Would you like to calculate again? (yes/no)")
#             again = input().strip().lower()
#             if again != 'yes' and again != 'y':
#                 break
# if __name__ == "__main__":
#     main()

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
def main():
    while True:
        while True:
            print("Choose the unit system For Weight:")
            print("1. Kilograms")
            print("2. LBS")
            weight_unit = input("Enter 1 or 2: ")
            if weight_unit == '1':
                weight = float(input("Enter your weight in kilograms: "))
                break
            elif weight_unit == '2':
                weight = float(input("Enter your weight in pounds: "))
                weight = weight * 0.453592  # Convert pounds to kilograms
                break
            else:
                print("Invalid choice. Please try again.")
        while True:
            print("Choose the unit system For Height:")
            print("1. Meters")
            print("2. Feet And Inches")
            height_unit = input("Enter 1 or 2: ")
            if height_unit == '1':
                height = float(input("Enter your height in meters: "))
                break
            elif height_unit == '2':
                feet = float(input("Enter your height in feet: "))
                inches = float(input("Enter your height in inches: "))
                height = (feet * 0.3048) + (inches * 0.0254)  # Convert feet and inches to meters
                break
            else:
                print("Invalid choice. Please try again.")
        if height <= 0 or weight <= 0:
            print("Height and weight must be positive values. Please try again.")
            continue
        else:
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            print(f"Your BMI is: {bmi:.2f}")
            print(f"You are categorized as: {category}")
            print("Would you like to calculate again? (yes/no)")
            again = input().strip().lower()
            if again != 'yes' and again != 'y':
                break
if __name__ == "__main__":
    main()