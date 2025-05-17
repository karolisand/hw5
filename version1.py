
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
            print("\nYou entered data in a wrong format.")
        else:
            repeat = False

    todo = {
        'title' : todo_title,
        'description' : todo_description,
        'data' : todo_data
    }

    todo_list.append(todo)

    print("\nToDo list:\n")

    for p in todo_list:
        print(f"ToDo Title: {p['title']}\n ToDo Description: {p['description']}\n ToDo Due Date: {p['data']}")