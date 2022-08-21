a = { 1 , 19 , 9 , 10 , 10 , 19 , 1 , 9}
print(a) # we can see that the repititive elements are not shown in the output

# adding elements in python

a.add(35)
print(a)

print(type(a))


# important

print("\n")
b = {}
print(type(b))   # this syntax will return Dictionary type as it is empty set
# this syntax will create an empty Dictionary and not an empty set

c = set()
c.add(3)
c.add(5)
c.add(5)
c.add(5)
c.add(5)
c.add(5)
c.add("CodeWithMustu")

print(type(c))
print((c))


# we cant add list in set
# c.add([2 , 6, 9])
# print(c)  # error : unhashable type

# But we can add tuple
c.add((2,6))
print(c)

# cant add dictionary keys and values in sets
# c.add({"Cool" : "Stylish"})
# print(c)



c.remove("CodeWithMustu")
print(len(c))
print(c)

print(c.pop())

# c.clear()
# print(c)


d = c.union({90 , 19 })
print(d)


e  = d.intersection({90})
print(e)



s1 = {1 , 2}
s2 = {3  , 4 , 1}
s3 = s1.intersection(s2)
print(s3)