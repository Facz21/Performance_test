#In this python doc we manage the data persistence of the program: functions to load and save data are here

import json
import os

#____________ DATA PERSISTENCE ____________

# Function to save information in JSON raw file
def save_tasks(tasks, path="db/tasks.json"):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

# Function to load the information previosly saved         
def load_tasks(path="db/tasks.json"):
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)