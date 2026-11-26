# Printing the length of a string

str1 = "Hello"
str2 = "World"

length1 = len(str1)
length2 = len(str2)
print("Length of str1 =", length1)
print("Length of str2 =", length2)

final_string = str1 + " " + str2
print(final_string)
print("Length =", len(final_string))


# Indexing the string
string1 = "Junaid Ahmad"  # We use indexing to print the specific element in the string.
print(string1[0])


# Slicing the string
string = "Junaid Ahmad"
print(string[0:len(string)])  # We use slicing to print the range of elements in the string.
print(string[0:])
print(string[:4])
