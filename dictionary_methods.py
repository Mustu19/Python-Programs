myDict = { "Beautiful" : "Amazing and Sweet" , 
            "Football" : "A game which whole world loves" , 
            "Programmer" : "A language to talk with Computer" , 
            "Colleges" : ["IIT" , "NIT" , "IIIT" , "BVM"] , 
            "anotherDict" : {"Mustu" : "Programmer"} , 
            19 : 5252
        }

# prints the keys of the dictionaries
print(list(myDict.keys()))

# prints the values of the dictionaries
print(myDict.values())

print("\n\n")

# prints the (key , value) for all contents of dictionary
print(list(myDict.items()))

# add contents in the dictionary or update the dictionary
print(myDict)

update_dict = {"Stay Foolish" : "Stay Hungry" , 
                "Beautiful" : "Dull and Dark" , 
                }
myDict.update(update_dict)

print(myDict)

print("\n\n\n")


# Important
print(myDict.get("Colleges")) # Prints the value of written key Colleges
print(myDict["Colleges"])  # Prints the value of written key Colleges

# The difference between .get and [ ] in Dictionaries ?
print(myDict.get("Colleges2")) # This key which is not present in myDict will give none in output 
print(myDict["Colleges2"])  # this will throw a error
