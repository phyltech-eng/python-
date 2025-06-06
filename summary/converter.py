#python  weight converter
weight = float(input("Enter your weight : "))
unit = input("kilograms or pounds : ")

if unit == "K":
    weight = weight * 2.20462
    unit = "lbs"
    print(f"Your weight in pounds is: {weight:.2f} {unit}")
elif unit == "L":
    weight = weight / 2.20462
    unit = "kg"
    print(f"Your weight in kilograms is: {weight:.2f} {unit}")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")  


    #temperature converter
    # 
temp = float(input("Enter the temperature: "))
unit = input("Celsius or Fahrenheit (C/F): ")
if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "F"
    print(f"The temperature in Fahrenheit is: {temp:.2f} {unit}")
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "C"
    print(f"The temperature in Celsius is: {temp:.2f} {unit}")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    

