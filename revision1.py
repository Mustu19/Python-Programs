print("Mustafa kapasi")

# a = int(input("Enter your name:"))
# print(a)

# b =  [1 , 3, 4, 5]

# print(b)
# print(b[1])


# b[0] = 35
# print(b)

# c = (45 , 32, 43, 12)
# print(c)

# c[0] = 24
# print(c)

# calculating orders

print("Welcome to Our Restaurant")
a1 = 0
a2 = 0
b1 = 0
b2 = 0

print("Enter 1 for punjabi menu and 2 for gujarati menu : ")
ch = int(input())

if (ch==1) :
    print("Panner bhurji 100Rs\nPanner toofani 130Rs")
    print("Now enter 1 for panner bhurji and 2 for panner toofani : ")
    a = int(input())
    if(a==1) :
        a1 = a1 + 1
    elif (a==2) :
        a2 = a2 + 1
    else :
        print("enter number 1 or 2")

elif (ch==2) :
    print("Sev tameta 100Rs\nFlower bataka 140Rs")
    print("Now enter 1 for Sev tameta and 2 for flower bateka : ")
    b = int(input())
    if(b==1) :
        b1 = b1 + 1
    elif (b==2) :
        b2 = b2 + 1
    else :
        print("enter number 1 or 2")

else :
    print("enter number 1 or 2")