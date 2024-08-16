#A Python Program To Count The Factors Of a Number
num = int(input("Enter a Number For Count The Factors: "))
count=0
i =1 
while i<=num:
    if num%i == 0:
        count+=1
    i+=1

print(f"Numbers of factors of {num} is: {count}")