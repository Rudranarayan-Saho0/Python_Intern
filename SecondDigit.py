#Print The Second Digit Of a Three Digit Number
number = int(input('Enter a Three Digit Number '))
if 100<=number<=999:
    digit = (number//10)%10
    print(f'The Second Digit Of The {number} is {digit}')
else:
    print("Invalid Input")