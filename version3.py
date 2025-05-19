
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="ToDo list")

todo_list = []

while True:
    todo_title = input("\nPlease enter ToDo title: ")
    todo_description = input("Please enter ToDo description: ")

    repeat = True
    
    while repeat:
        import re

        pattern = r"\d{4}-\d{2}-\d{2}"                                           # Set format: xxxx-xx-xx
        todo_data = input("Please ad ToDo date (in format: yyyy-mm-dd): ")

        if not re.fullmatch(pattern, todo_data):
            console.print("\nYou entered data in a wrong format.", style="red")
        else:
            repeat = False

    todo = {
        'title' : todo_title,
        'description' : todo_description,
        'data' : todo_data
    }

    todo_list.append(todo)

    console.print("\nToDo list:\n", style="bold cyan")

    for p in todo_list:


        
        console.print(f"ToDo Title: [magenta]{p['title']}[/]")
        console.print(f"ToDo Description: [magenta]{p['description']}[/]")
        console.print(f"ToDo Due Date: [magenta]{p['data']}[/]")