#Program For Add The Digit Of a Number.
number = int(input("Enter a Three Digit Number"))
if 100<=number<=999:
    digit = (number//100)+((number//10)%10)+number%10
    print(f"The Sum Of Digit Of {number} is {digit}")
else:
    print("Invalid Input")