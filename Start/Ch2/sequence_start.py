# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# List is the same as an array in Java
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
#print(len(mylist))

# to access a member of a sequence type, use []
# list are 0 index based
# strings are also sequences
# string are immutable
 
# print(mylist[2])
# print(mylist[-1])
# mylist[0] = 10
# print(mylist)

# add a list to another list
# another_list = [6,7,8]
# mylist = mylist + another_list
# print(mylist)

mystr = "This is a string"
# print(mystr[2])


# use slices to get parts of a sequence
# this would grab indexes 1,2,3 but not including 4
# print(mylist[1:4])
#we can add a skip as well and get every other so indexes 1 and 3
# print(mylist[1:4:2])

# print(mylist[::2])


# you can use slices to reverse a sequence (works with strings too)
#print(mylist[::-1])

# Tuples are like lists, but they are immutable
myTuple = (0,1,2,"three")
# print(myTuple[1])

# Sets are also sequences, but they contain unique values
# you cant save multiple of the same value
myset = {1,2,3,2,4, "hey"}
#print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) 
# # this will cause an error

# Test for membership
print(1 in mylist)
print(3 in myTuple)
print(5 in myset)