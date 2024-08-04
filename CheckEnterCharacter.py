#A Python Program To Check User Inputed Character is An Alphabet, Digit or Special Character.
char = input("Enter a Character: ")

if char.isalpha():
    print("The Entered Character is an Alphabet.")
elif char.isdigit:
    print("The Entered Charcter Is a Digit.")
else:
    print("The Enteraed Character Is a Special Character.")