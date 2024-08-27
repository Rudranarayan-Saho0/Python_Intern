#Accept Words from User & Reverse The Word.
word = input("Enter A Word: ")
reverse = " "
i = len(word)-1
while i>=0:
    reverse+=word[i]
    i-=1
print(f"Reverse Word= {reverse}")
