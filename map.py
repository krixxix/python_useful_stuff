# map allows to apply a function to every single item in an iterable object
# iterable object is anything that you can loop trough

strings = ["my","world","apple","pear"]

################################################################################################ EXAMPLE 1

lengths = map(len, strings)

print(list(lengths))


print("------------------------------")
################################################################################################ EXAMPLE 2

# we can also use custom function like:
example2 = map(lambda x: x + "s", strings)
print(list(example2))

# it´s going to pass every single one of the strings to the function as the parameter x
# then it´s simply adding "s" to all of the strings


print("------------------------------")
################################################################################################ EXAMPLE 1
def add_s(string):
    return string + "s"

example3 = map(add_s, strings)
print(list(example3))
