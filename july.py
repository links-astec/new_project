# To-do list program
"""
1. create a user friendly to-do list
2. users can add, remove, view and update tasks
3. identify potential errors and handle them
4. make the program restartable such that the user can decide when to exit the program
5. achieve using the most efficient code

"""



x =  """
1. chose 1 to add tasks
2. chose 2 to remove tasks
3. chose 3 to view tasks
4. chose 4 to update tasks
"""

# A to-do list application by team glinax

print("Welcome to Robo to-do list application")
print(x)

tasks = []
# the append function adds new members to a list

input_task = input("Kindly type your task below: ")

tasks.append(input_task)

#print(tasks)
for task in tasks:
    print(task)
# pop, remove functions delete members from a list
# pop function removes the last item in the list
# clear function removes all members in the list
# dir function provides a list of functions and methods that apply to a particular data type or structure
#print(dir(tasks))

tasks.remove(input_task)
tasks.clear()
print(tasks)


# indexing

tasks.append("going fising")
tasks.append("go to the market")
tasks.append("go farming")
tasks.append("do my homework")

tasks[0] = input("enter a new task for the first member in your list")

#print(number_2)


print(tasks)