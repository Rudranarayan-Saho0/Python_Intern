#Give Bonus Of 5% To Employee If His/Her Year Of Service is More Than 5Year.

salary = float(input("Enter Your Salary: "))
Service_Year = float(input("Enter Your Year Of Service: "))

if Service_Year>5:
    bonus = salary+salary*0.05
else:
    bonus = salary

print(f"Your Net Salary In This Month= {bonus}")