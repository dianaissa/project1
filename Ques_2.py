number=int(input("enter decimal number"))
b=[]
while number > 0:

    rem=number%2
    number = number // 2
    b.append (rem)
b.reverse()
print(b)