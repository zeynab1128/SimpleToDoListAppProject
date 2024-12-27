def add_task(task) :
    if task not in todoList :
        todoList.append(task)
        return "Done"
    else :
        return "The activity has already been added to the list."

def view_tasks() :
    if not todoList:
        return "Your to-do list is currently empty."
    else :
        return("\n".join(todoList))

def mark_completed(task) :
    if task in todoList :
        todoList.remove(task)
        completedList.append(task)
        return f"Task '{task}' marked as completed."
    else :
        return f"Task '{task}' not found in the list."

def remove_completed_tasks(task) :
    if task in todoList :
        list_index = todoList.index(task)
        todoList.pop(list_index)
        uncompletedList.append(task)
        return f"Task '{task}' deleted."
    else :
        return f"Task '{task}' not found in the list."

todoList = []
completedList = []
uncompletedList = []

while True:
    print("Please enter the task number you want to do with the ToDo list:\n1)Add new task.\n2)View existing task.\n3)Mark task as completed.\n4)Remove uncompleted task.")
    num_task = input()
    
    if num_task == "1" :
        print("Please Enter the name of the task you want to add:")
        task = input()
        print(add_task(task))
    
    elif num_task == "2" :
        print(view_tasks())
    
    elif num_task == "3" :
        print("Please Enter the name of the task you want to Marked:")
        task = input()
        print(mark_completed(task))
    
    elif num_task == "4" :
        print("Please Enter the name of the task you want to delete:")
        task = input()
        print(remove_completed_tasks(task))
    
    print("*_**_**_**_**_**_**_**_**_**_*")