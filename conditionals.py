a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))
c = int(input("Enter number 3 :"))



if (a==b==c) :
    print("all numbers are same")
    
elif (a>b) :
    if(a > c) :
        print(a, "is greater from all numbers")
    else :
        print(c, "is greater from all numbers")
else :
    if(b>c) :
        print(b , "is greater from numbers")
    else :
        print(c, "is greater from all numbers")