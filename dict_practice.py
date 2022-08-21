# l1 = input("Favourite language of friend 1 :")
# l2 = input("Favourite language of friend 2 :")
# l3 = input("Favourite language of friend 3 :")
# l4 = input("Favourite language of friend 4 :")

# myDict = {"Mustu" : l1  , "ALiAsgar" : l2  , "HasanAli" : l3 , "Hamza" : l4}

# # if the name of 2 friends , it will show the  latest updated value entered by the user that is l2

# # if the name of 2 values(languages) are same , it will show the output whole without any changes

# print(myDict)

def task(rows) :    
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print('')


from time import time

start = time()

# Python program to create acronyms
rows = 5
word = "Artificial Intelligence Machine Learning"
text = word.split()
print(text)
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
task(rows)
end = time()
execution_time = end - start
print("Execution Time : ", execution_time)