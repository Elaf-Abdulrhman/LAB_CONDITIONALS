def calculate_bmi(weight: float, height: float) -> float:
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

# Ask user for input
try:
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

    # Provide feedback based on BMI
    if bmi < 18.5:
        print("You are underweight. Watch your health.")
    elif 18.5 <= bmi < 24.9:
        print("You are fit & healthy.")
    else:
        print("You are overweight. You need to work out more and watch your diet.")

except ValueError:
    print("Please enter valid numerical values for weight and height.")