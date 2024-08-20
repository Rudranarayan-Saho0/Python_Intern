#Basic Traffic Light Program.

signal = input("Enter The Traffic Light Color(Red/Yellow/Green/Other): ").lower()

if signal=="red":
    print("Car Has To Stop.")
elif signal=="green":
    print("Car Is Allowed To Go.")
elif signal=="yellow":
    print("Car Has To Wait.")
else:
    print("Unrecognised Color.")
