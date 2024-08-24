#A Simple Python program to To find The Sum Of Even Numbers From 1To Inputed Number(While Loop)
num = int(input("Enter a Number: "))
sum_even = 0
i = 2
while i<=num:
    sum_even+=i
    i+=2
print(f"The Sum Of All Even Number Between 1 To {num} is  {sum_even}.")