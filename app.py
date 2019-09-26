course = 'Python Programming'
print(len(course))
print(course[2])
# to print the last character of the string
print(course[-1])
# to slice, this will return the first three characters in the string
print(course[0:3])
# this will return the same as above
print(course[:3])
# will return the entire string
print(course[0:])
# will also return the entire string
print(course[:])

# strings are immutable in Python, hence this results in different memory locations when run
print(id(course))
print(id(course[0]))
