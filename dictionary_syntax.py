myDict = { "Beautiful" : "Amazing and Sweet" , 
            "Football" : "A game which whole world loves" , 
            "Programmer" : "A language to talk with Computer" , 
            "Colleges" : ["IIT" , "NIT" , "IIIT" , "BVM"] , 
            "anotherDict" : {"Mustu" : "Programmer"} 
        }


print(myDict["Football"])
print(myDict["Colleges"])
print(myDict["anotherDict"]["Mustu"])

# We can change the myDict bcoz it mutable

myDict["Football"] = '''Cricket'''
print(myDict["Football"])


