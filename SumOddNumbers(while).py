#a Simple Python Program To Calculater The Sum Of Odd Numbers.(While Loop)
num = int(input("Enter a Number: "))
sum_odd = 0
i=1
while i<=num:
    if i%2!=0:
        sum_odd+=i
    i+=1
print(f"The Sum Of Odd Numbers from 1 to {num} is {sum_odd}")
