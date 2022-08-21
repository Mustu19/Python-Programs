a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))
c = int(input("Enter number 3 :"))
d = int(input("Enter number 4 :"))

# if(a > b) : 
#     if(a > c) :
#         if(a > d) :
#             print(a, "is greatest")
#         else :
#             print(d, "is greatest")
#     else :
#         if (c > d):
#             print(c, "is greatest")
#         else :
#             print(d, "is greatest")
# else :
#     if(b>c) :
#         if(b > d) :
#             print(b , "is greatest")
#         else : 
#             print(d , "is greatest")
#     else : 
#          if (c > d):
#             print(c, "is greatest")
#          else :
#             print(d, "is greatest")



# Shortest way to find greatest

if(a > b) :
    num1 = a 
else :
    num1 = b

if(c > d) :
    num2 = c
else :
    num2 = d

if(num1 > num2) :
    print(str(num1) + " is greatest")
else :
    print(str(num2) + " is greatest")