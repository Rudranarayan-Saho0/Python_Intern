number = int(input('Enter A Three Number'))
if 100<= number <=999:
    last_digit = number%10
    print(f"The Last Digit Of The Number {number} is {last_digit}")
else:
    print(f"Please Enter A Valid Three Digit Number.")
