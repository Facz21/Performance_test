#IMPORTS TO HANDLER BUSINESS LOGIC AND UI MENUS INTERFACE

from ui.menus import main_menu
from src.logic.crud_operations import show_tasks_list
from src.handler.task_handler import (
    tasks_registration_handler, search_task_by_id, update_task_handler, handle_delete, change_status_handler
)

# here we import the functions for data persistance
from db.json_manager import(
    save_tasks, load_tasks
)


def main():
    
    # Control variable for the main loop (0 = exit program)
    start = 1
    tasks = load_tasks() # Load existing tasks from JSON file into memory
    
    # Main program loop
    while start != 0:
        
        main_menu() # Display main menu options
        
        
        # Capture user option
        option = input("Select a option: ")
        
        # CRUD OPERATIONS

        # CREATE → Add a new taskt
        if option == "1":
            
            tasks_registration_handler(tasks)
            save_tasks(tasks)
        
        # READ → Show all tasks
        elif option == "2":
            
            show_tasks_list(tasks)
        
        # SEARCH → Search task by ID         
        elif option == "3":
            
            search_task_by_id(tasks)
        
        # UPDATE → Modify an existing task
        elif option == "4":
            
            update_task_handler(tasks)
            save_tasks(tasks)
            
        # UPDATE → Modify status of a task
        elif option == "5":
            
            change_status_handler(tasks)
            save_tasks(tasks)
            
        # DELETE → Remove a task from task "data base"
        elif option == "6":
            
            handle_delete(tasks)
            save_tasks(tasks)
       
        # EXIT → End program
        elif option == "0":
            
            print("Good bye user")
            start = 0
            
        # INVALID OPTION → Handle incorrect input
        else:
            print(f"""
Option {option} is not valid.
Please try again (Valid option 1-5 | enter 0 to exit)
                  """)

# Entry point of the program
# Ensures main() runs only when this file is executed directly            
if __name__ == "__main__":
    main()           