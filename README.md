# Task Manager

This project implements a simple task management system in Python. It allows users to create, manage, and track tasks with different priorities.

## Project Structure

The project consists of two main classes:

1. `Tarea` (Task): Represents a single task with attributes such as ID, title, description, completion status, and priority.
2. `GestorTareas` (TaskManager): Manages a collection of tasks, providing methods to add, delete, search, and filter tasks.

## Features

- Create new tasks with title, description, and priority levels
- Delete existing tasks by ID
- Search for tasks by ID
- Mark tasks as completed
- List all tasks or only pending tasks
- Filter tasks by priority (low, normal, high)
- Task priority validation

## Class: Tarea (Task)

The `Tarea` class represents an individual task with the following attributes:

- `id`: Unique identifier for the task
- `titulo` (title): The title of the task
- `descripcion` (description): A detailed description of the task (optional)
- `completada` (completed): Boolean status indicating if the task is completed
- `prioridad` (priority): Priority level of the task (low, normal, high)

The class implements custom equality comparison (`__eq__`) based on task ID.

## Class: GestorTareas (TaskManager)

The `GestorTareas` class manages a collection of tasks with the following methods:

- `agregar_tarea` (add_task): Creates a new task and adds it to the collection
- `borrar_tarea` (delete_task): Removes a task by ID
- `buscar_tarea_porID` (search_task_by_ID): Finds a task by its ID
- `marcar_tarea_completada` (mark_task_completed): Updates a task's completion status
- `listar_tareas` (list_tasks): Returns all tasks or only pending tasks
- `filtrar_tarea_prioridad` (filter_task_by_priority): Filters tasks by priority level

## Testing

The project includes a comprehensive set of unit tests covering all the functionality:

- Adding tasks
- Deleting tasks
- Searching for tasks
- Marking tasks as completed
- Listing tasks
- Filtering tasks by priority
- Priority validation
- Task comparison

Run the tests using:

```python
python -m unittest test_gestor_tareas.py
```

## Priority Levels

The system supports three priority levels:
- `baja` (low)
- `normal` (normal)
- `alta` (high)

Attempting to use any other priority will raise a `ValueError`.