myDict ={"phone" : "Mobile",
            "bottle" : "water bottle",
            "pankho" : "fan"}

print("Options are " , myDict.keys())

a = input("enter your hindi word here :\n")
# print("The meaning of the hindi word is" , myDict[a])

#  below line will not throw an error if the key is not present in the dictionary
print("The meaning of the hindi word is" , myDict.get(a))

