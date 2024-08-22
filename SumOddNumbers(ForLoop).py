#a Simple Python Program To Calculater The Sum Of Odd Numbers.(While Loop)
num = int(input("Enter a Number: "))
sum_odd = 0
i=1
for i in range (1,num+1,2):
        sum_odd+=i

print(f"The Sum Of Odd Numbers from 1 to {num} is {sum_odd}")