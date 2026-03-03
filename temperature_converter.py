print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice (1-6): "))
temp = float(input("Enter temperature value: "))

if choice == 1:
    print("Result:", (temp * 9/5) + 32, "F")
elif choice == 2:
    print("Result:", temp + 273.15, "K")
elif choice == 3:
    print("Result:", (temp - 32) * 5/9, "C")
elif choice == 4:
    print("Result:", (temp - 32) * 5/9 + 273.15, "K")
elif choice == 5:
    print("Result:", temp - 273.15, "C")
elif choice == 6:
    print("Result:", (temp - 273.15) * 9/5 + 32, "F")
else:
    print("Invalid choice")  