from string import printable


name = "Mustu"
greeting = "Good Morning "
# print(type(name))

# Concatenating strings
print(greeting + name)

print(name[0] + name[1] + name[2])

# name[3] = "d" --> does not work


# String Slicing
print(name[0:2])  # it will print index 0 ,1, 2, and 3
print(name[2:4])
print(name[:4])   # this is same as name[0:4]
print(name[0:])   # this is same as name[0:5]


# Negative indices

print(name[-3:-1])  # this is same as name[2:4]

name = "CodeWithMustu"
d = name[0::3]  # --> pella 2 ma kya thi kya sudhi javu hoi enu and last number eni mate ke ee index numer skip thato rehse
print(d)

word = "beautiful"
print(word[0::2])