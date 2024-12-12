# often times, when we iterate with a for loop, we would like to be able to access both the index and the value

tasks = ["Write report","Attend meeting", "Review code", "Submit timesheet"]


################################################################################################ WAY 1 - without enumerate
for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1}. {task}")

print("------------------------------")
################################################################################################ using enumerate with a for loop
for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

print("------------------------------")
################################################################################################ using enumerate without a for loop
print(list(enumerate(tasks)))