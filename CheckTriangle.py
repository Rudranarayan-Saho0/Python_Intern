#Python Program Check Wheather A Triangle is Equilateral, Isoscale or Scalene.
b = float(input("Enter Side B: "))
a = float(input("Enter Side A: "))
c = float(input("Enter side C: "))

if a==b==c:
    print("Triangle Is Equilateral")
elif a==b or b==c or a==c:
    print("Trianglr is Isoscale")
else:
    print("Triangle is Scalene")
