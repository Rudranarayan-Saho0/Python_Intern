#A Python Program To Convert The Tempreture celcius To Fahrenheit & Fahrenheit to Celcius.
print("1. Convert Celcius To Fahrenheit.\n2. Convert Fahrenheit To celcius.")
choice = input("Enter Your Choice(1/2): ")

if choice == "1":
    Celcius = float(input("Enter Tempreture in Celcius: "))
    Fahrenheit = (Celcius*9/5)+32
    print(f"{Celcius}C = {Fahrenheit}F")
elif choice == "2":
    Fahrenheit = float(input("Enter Tempreture in Fahrenheit: "))
    Celcius = (Fahrenheit-32)*5/9
    print(f"{Fahrenheit}F = {Celcius}C")
else:
    print("Invalid Choice.")