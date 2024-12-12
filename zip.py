# we sometimes have 2 lists with corresponding values
names = ["Alice", "Bob", "Charlie", "David"]
ages = [30,25,35,20]


################################################################################################ without the ZIP() function
for idx in range(len(names)):  
    name = names[idx]
    age = ages[idx]
    print(f"{name} is {age} years old")


print("------------------------------")
################################################################################################ using the ZIP function
combined = list(zip(names,ages))

for name,age in combined:
    print(f"{name} is {age} years old.")

print(combined)

print("------------------------------")
################################################################################################ even more lists
names = ["Alice", "Bob", "Charlie", "David"]
ages = [30,25,35,20]
gender = ["Female","Male","Male"] # I have less values: zip will solve it for me

combined2 = zip(names,ages,gender)

for name,age,gender in combined2:
    print(f"{name} is {gender} and is {age} years old.")