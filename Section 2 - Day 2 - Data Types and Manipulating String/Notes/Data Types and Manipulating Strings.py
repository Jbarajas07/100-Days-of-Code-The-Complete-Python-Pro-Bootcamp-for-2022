#Data Types

#String

print("Hello"[0]) #indexing, Subscript - pulling out a particular element from a string. 
print("Hello"[4])
print("Hello"[-1])

print("123" + "345")

#Integer - whole numbers

print(123 + 345)

123_456_789 # underscores (_) can be used to replace commas (,) in large numbers as 123,456,789. in order to help with visualization.

#Float - decimals

3.14159 

#Boolean
True
False


#Type Error, Type Checking and Type Conversion
num_char = len(input("What is your name?"))
# print("Your name has " num_char + " characters.") - gives an error. Can't concatenate strings and integers. 

print(type(num_char))

#Type casting (Type conversion)
num_char = len(input("What is your name?"))
new_num_char = str(num_char) # str converts integer to string. 
print("Your name has " + new_num_char + " characters.")

#convert a integer into a string. 
a = 123
print(type(a))

a = str(123)
print(type(a))

# float conversion
a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))



