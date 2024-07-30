#Find The Unique Value From The Given Two List
m = [12, 56,89, 34, 67]
n = [12, 45, 56, 55, 21]

Unique_Number = list(set(m) & set(n))
print(f'Unique Value = {Unique_Number}')