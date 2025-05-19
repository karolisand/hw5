
from rich.console import Console
from rich.table import Table
import re

console = Console()
todo_list = []

while True:
    todo_title = input("\nPlease enter ToDo title: ")
    todo_description = input("Please enter ToDo description: ")
    
    while True:
        todo_data = input("Please ad ToDo date (in format: yyyy-mm-dd): ")
        pattern = r"\d{4}-\d{2}-\d{2}"                                           # Set format: xxxx-xx-xx
    
        if not re.fullmatch(pattern, todo_data):
            console.print("\nYou entered data in a wrong format.", style="red")
        else:
            break
            # repeat = False

    todo = {
        'title' : todo_title,
        'description' : todo_description,
        'date' : todo_data
    }

    todo_list.append(todo)

    table = Table(title="ToDo list")
    table.add_column("ToDo Title", style="bold")
    table.add_column("ToDo Description")
    table.add_column("ToDo Due Date", style="green")

    for item in todo_list:
        table.add_row(item['title'], item['description'], item['date'])

    console.print(table)
    