# Task Management System (Python CLI)

A structured Task Management System built with Python.
Implements CRUD operations, input validation,  and JSON-based data persistence.

---

## Features

* Add new task
* View all task
* Search by ID
* Update task information
* Change task status
* Delete tasks
* Save and load data from CSV
* Input validation and error handling

---

## Project Structure

```id=
Prueba_desempeño/
|
├── main.py
├── README.md
|
├── db
│   ├── json_manager.py   
│   └── tasks.json
|
├── docs
│   └── Enunciado Prueba de Desempeño - M1 Python V2_2.pdf
|
├── src
│   ├── handler
│   │   └── task_handler.py
│   ├── logic
│   │   ├── crud_operations.py
│   │   └── priorities.py   
│   │   
│   └── validations
│       └── input_validations.py
│   
└── ui 
    └── menus.py
  
```

---

## How It Works

1. The program loads product data from a JSON file
2. Displays a menu to the user
3. Executes actions based on user input
4. Updates the in-memory tasks list
5. Saves changes back to the JSON file

---

## CRUD Operations

| Operation | Description             |
| --------- | ----------------------- |
| Create    | Add a new task          |
| Read      | Display all task        |
| Update    | Modify an existing task |
| Delete    | Remove a task           |

---

## Technologies Used

* Python 3
* CSV module (standard library)
* Command Line Interface (CLI)

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Facz21/Performance_test.git
cd ProjectInventory
```

2. Run the program:

```bash
python main.py
```

---

## Documentation

The `docs/` folder contains additional documentation:

* `docs/Enunciado Prueba de Desempeño - M1 Python V2_2.pdf`: Program requirements

---

## Design Principles

* Separation of concerns
* Modular architecture
* Clean and readable code
* Input validation
* Error handling

---

## Future Improvements

* Graphical user interface (Tkinter or PyQt)
* Database integration (SQLite or PostgreSQL)
* Logging system
* Advanced search and filtering

---

## Author

Andrés Felipe Cortés Zambrano | Python Developer

Github: Facz21
