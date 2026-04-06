#VALIDATIONS ARE APPLIED FOR ID

# Here we make sure ID is not duplicated or not excist in the task data base
def input_unique_id(tasks, find_task):


    start = 1
    while start != 0:
        
            task_id = input("Enter the task ID (4 digits): ")

            if find_task(tasks, task_id):
                print("Task already registered")
            else:
                return task_id

# Some parameters to a valid ID like length of the ID and only numbers allowed            
def task_id_validation(task_id):
    
    if not task_id.isdigit():
        return False
    
    if len(task_id) != 4:
        return False
    
    if not int(task_id) >= 100:
        return False
    
    else:
        return True