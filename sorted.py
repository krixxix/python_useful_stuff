# this functino will sord an iterable object in ascending or descending order 
# depends on our demands

numbers = [4,5,2,3,-1,0,9]

################################################################################################ EXAMPLE 1
sorted_nums = sorted(numbers)
print(sorted_nums)

print("------------------------------")
################################################################################################ EXAMPLE 2
sorted_nums2 = sorted(numbers, reverse=True)
print(sorted_nums2)

print("------------------------------")
################################################################################################ EXAMPLE 3
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age":35},
    {"name": "David", "age": 20},
]

sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)
