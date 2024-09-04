#Print The First digit Of The Three Digit Number
number = int(input('Enter a Three Digit Number '))
if 100<= number<=999:
    digit = number //100
    print(f'the first digit of number is {digit} ')
else:
    print('Invalid Input')