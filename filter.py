# it will take every single item in our iterable object
# it will pass it to some function
# if that function returns true, it will kepp that item, otherwise it will remove it from the result

strings = ["my","world","apple","pear"]


################################################################################################ EXAMPLE 1

def longer_than_4(string):
    return len(string) > 4

filtered = filter(longer_than_4, strings)

print(list(filtered))