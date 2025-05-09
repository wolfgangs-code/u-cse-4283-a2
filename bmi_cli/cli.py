from bmi import imperial_to_bmi, categorize_bmi


def main():
    print("Welcome to the BMI Calculator!")
    print("Please enter your weight and height (feet then inches) to calculate your BMI.")

    try:
        # Get user input for weight and height
        weight = float(input("Enter your weight in pounds: "))
        h_feet = float(input("Enter your height in feet: "))
        h_inch = float(input("Enter your height in inches: "))

        # Calculate BMI
        bmi = imperial_to_bmi(h_feet, h_inch, weight)
        category = categorize_bmi(bmi).lower()

        # Display results
        print(f"Your BMI is {bmi:.2f}.")
        print(f"You are considered to be {category}.")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
    except ZeroDivisionError:
        print("Height cannot be zero. Please enter a valid height.")

if __name__ == "__main__":
    main()