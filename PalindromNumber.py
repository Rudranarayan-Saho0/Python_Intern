n = int(input("Enter a Number: "))
rev = 0
num = n
while n>0:
    r = n%10
    rev = rev*10+r
    n = n//10
if num==rev:
    print(f"{num} Is a Palindrom Number.: ")
else:
    print(f"{num} Is Not a Palindrom Number.")