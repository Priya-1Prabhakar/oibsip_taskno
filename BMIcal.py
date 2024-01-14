def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Prompt the user for weight and height, and handle input validation


while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        if weight <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid weight.")
while True:
    try:
        height = float(input("Enter your height in meters: "))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid height.")

# Calculate the BMI
bmi = calculate_bmi(weight, height)

# Classify the BMI
category = classify_bmi(bmi)

# Display the result to the user
print("Your BMI is:", bmi)
print("Category:", category)
