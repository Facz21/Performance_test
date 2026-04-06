#IMPORTS

#Business logic functions (CRUD )
from src.logic.crud_operations import *

#Options for priorities selection
from src.logic.priorities import get_priorities

# UI menus
from ui.menus import priorities_options

# Input validations for unique ID and valid parameters for it
from src.validations.input_validations import(
    input_unique_id, task_id_validation
)

# This function handle the priority selection to add it to the main dictionary list
def priority_selection_handler():
    priorities = get_priorities()
    

    start = 1
    
    while start != 0:
         
        priorities_options()
        option = input("Select a priority: ")
         
      
        if option in priorities:
            priority = priorities[option]
            start = 0
        else:
            print(f"""
Option {option} not avalible.
Try again.
                  """)
    return priority

# Here we create a task with parameters (ID, name, description, priority and status)
def tasks_registration_handler(tasks):
    
    start = 1
    
    while start != 0:
        task_id = input_unique_id(tasks, find_task)
        if task_id_validation(task_id):
            start = 0
        else:
            print("Invalid ID. Must be 4 digits and numeric ")
    start = 1
    
    
    
    task_name = input("Enter task name: ")        
    task_description = input("Enter task description: ")
    priority = priority_selection_handler()
    new_task = task_creation(task_id, task_name, task_description, priority)
    
    if new_task:
        tasks.append(new_task)
        print(f"Taks {new_task["name"]} registered successfully")

#Here the function look for a match with ID and tasks data base        
def search_task_by_id(tasks):
    task_id = input("Enter task ID: ")
    
    task = find_task(tasks, task_id)
    
    if task is None:
        print("Task not found")
        return
    
    show_tasks_list([task])
 
#With this function we update info of a especific task 
def update_task_handler(tasks):
    print("\n--- UPDATE TASK ---")

    task_id = input("Enter task ID: ")

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    
    show_tasks_list([task])

    print("Leave blank to keep current value")

    
    
    name = str(input("Enter task new name: "))
               
    description = str(input("Enter task new description: "))

    change_priority = input("Update priority? (y/n): ").lower()

    if change_priority == "y":
        priority = priority_selection_handler() #Recall priority selection to choose a new priority for a task
    else:
        priority = None
    
    update_task_information(task, name, description, priority)

    print("Task updated successfully.")   

# Also here we can change the status of a task to done or pending with this function    
def change_status_handler(tasks):
    print("\n--- CHANGE TASK STATUS ---")

    task_id = input("Enter task ID: ")

    task = find_task(tasks, task_id)

    if task is None:
        print("task not found.\n")
        return

    change_task_status(task)

    print("task status successfully changed.")

# Finally, the delete function to remove task from the tasks "data base"     
def handle_delete(tasks):


    try:
        task_id = input("Enter ID: ")
        delete_task(tasks, task_id)
        

    except ValueError:
        print("Invalid input")


#And this it the handler of the program: we use the CRUD functions to have a better experience in the development of those functions