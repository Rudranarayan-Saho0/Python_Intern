#Print The sum of Squares Of all Integers from 1 to n.
num = int (input("Enter A Number "))
sumOfSquare= 0
for i in range (1,num+1):
    sumOfSquare+=i**2
print(f"the sum of the squares of all integers from 1 to {num} is {sumOfSquare}.")