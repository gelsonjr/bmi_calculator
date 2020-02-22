# bmi_caulculator.py
# Gelson Cardoso
# This is my Python BMI Calculator. It can calculate using both Metric and Imperial units

def main():

    # Introduction
    print("Welcome to my BMI calculator!")

    # Get input from the user to check if we need to use Imperial or Metric units
    unit_input = str(
        input("Are we using Imperial units for your calculation today? (yes / no) "))

    if unit_input == "yes":
        weight_lb = float(input("Great! What is your weight in pounds? "))
        height_in = float(input("And what is your height in inches? "))
        imp_calc(weight_lb, height_in)

    elif unit_input == "no":
        weight_kg = float(input("No problem! What is your weight in kg? "))
        height_m = float(
            input("And what is your height in meters? (x.xx format) "))
        metric_calc(weight_kg, height_m)

    else:
        print('Invalid input. Please enter "yes" or "no"\n')
        return main()

    # Checking if user would like to try another calculation
    try_again = str(
        input("\nWould you like to try another BMI calculation? (yes/no) "))

    if try_again == "yes":
        print("Excellent! Let's try another one.\n")
        return main()

    else:
        print("Very well. Good bye!")
        exit()

# Methods        

# BMI Formula (Imperial)
def imp_calc(weight_lb, height_in):
    bmi = round(((weight_lb / (height_in ** 2)) * 703), 2)
    bmi_standards(bmi)

# BMI Formula (Metric)
def metric_calc(weight_kg, height_m):
    bmi = round(weight_kg / (height_m ** 2), 2)
    bmi_standards(bmi)

# BMI Standards
def bmi_standards(bmi):
    if 18.5 > bmi:
        print("Your BMI is", bmi, "- You are underweight, eat some cake.")
    elif 18.5 <= bmi <= 24:
        print("Your BMI is", bmi, "- That's a healthy weight. Looking Good!")
    elif 25 <= bmi <= 29:
        print("Your BMI is", bmi, "- You are overweight, you need to hit the gym.")
    elif 30 <= bmi <= 39:
        print("Your BMI is", bmi, "- You are obese, get off the couch you lazy head.")
    elif 39 < bmi:
        print("Your BMI is", bmi, "- You are extremely obese! Go get some help.")


main()
