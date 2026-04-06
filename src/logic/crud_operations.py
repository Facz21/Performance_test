
#------------- CRUD OPERATIONS ------------- 


#Create a task

def task_creation(task_id,name,description,priority):
    
    task ={
        "id" : task_id,
        "name" : name,
        "description" :description,
        "priority" : priority,
        "status" : True
    }
    
    return task

#Show all the task stored in memory

def show_tasks_list(tasks):
    if not tasks:
        print("--- TASKS LIST EMPTY ---")
    else:
        
        print("\n--- TASKS LIST ---\n")

        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            
            print(f"Priority: {task['priority']}")
            
            print(f"Status: {'Pending' if task['status'] else 'Done'}")
            print("-" * 40)

 
#Find a task based on its ID
 
def find_task(tasks, task_id):
 
    for task in tasks:
        if task["id"] == task_id:
            return task
        
#Update information of a task

def update_task_information(task, name = None, description = None, priority = None):
    
    if name is not None:
        task["name"] = name
        
    if description is not None:
        task["description"] = description
        
    if priority is not None:
        task["priority"] = priority
    
    return task

# Delete a task
 
def delete_task(tasks, task_id):
    """
    Deletes a product from the inventory using its ID.
    """

    task = find_task(tasks, task_id)

    if task:
        tasks.remove(task)
        print("Task deleted")
    else:
        print("Task not found")
        
# Change tasj status     
        
def change_task_status(task):

    if task:   
        task["status"] = False
        return task
    else:
        task["status"] = True
        return task