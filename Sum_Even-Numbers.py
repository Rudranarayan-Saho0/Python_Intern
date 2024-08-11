#The Sum of Even  Numbers Using For Loop.
num = int(input("Enter A Number: "))
sum_even = 0
for i in range(2,num+1,2):
    sum_even+=i
print(f"The Sum Of Even Numbers from 1 to {num} is {sum_even}")
