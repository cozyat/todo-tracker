import tsapp

window = tsapp.GraphicsWindow()
checkboxes = []
lines_map = {}

def display_todos():
    with open("todos.txt") as file:
        todos = []
        for line in file.readlines():
            todos.append(line.replace("\n", "").strip())
            todos.sort()
    for checkbox in checkboxes:
        if checkbox.visible:
            checkbox.visible = False
    for label in lines_map.values():
        label.destroy()
    lines_map.clear()
    for i in range(6):
        if i == len(todos):
            break
        else:
            checkbox = tsapp.Sprite("IconSquareBlackOutline.png", 0, 45 + 67 * i)
            checkbox.scale = 0.2
            checkboxes.append(checkbox)
            window.add_object(checkbox)          
            todos_label = tsapp.TextLabel("OpenSans-Regular.ttf", 30, 100, 125 + 67 * i, 1000, str(todos[i]))
            window.add_object(todos_label)            
            lines_map[checkbox] = todos_label
                
def add_todo():
    new_todo = "\n" + input("Add todo: ")    
    with open("todos.txt", "a") as file:
        file.write(new_todo)
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    cleaned_todos = []
    for todo in todos:
        if todo.strip() != "":
            cleaned_todos.append(todo)
    with open("todos.txt", "w") as file:
        file.writelines(cleaned_todos)
    display_todos()

def delete_todo(checkbox):
    if checkbox in lines_map:
        todo_text = lines_map[checkbox].text
        lines_map[checkbox].destroy()
        checkbox.destroy()
        del lines_map[checkbox]
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        updated_todos = []
        for todo in todos:
            if todo.strip() != todo_text.strip():
                updated_todos.append(todo)    
        with open("todos.txt", "w") as file:
            file.writelines(updated_todos)

background = tsapp.Sprite("AbstractGreenBrightLine.jpg", 0, 0)
window.add_object(background)
header = tsapp.TextLabel("OpenSans-Bold.ttf", 50, 20, 60, 1000, "Todos:")
window.add_object(header)

for i in range(6):
    checkbox = tsapp.Sprite("IconSquareBlackOutline.png", 0, 45 + 67 * i)
    checkbox.scale = 0.2
    checkboxes.append(checkbox)
    window.add_object(checkbox)
todos_label = tsapp.TextLabel("OpenSans-Regular.ttf", 30, 100, 120, 1000, "")
window.add_object(todos_label)
add_button = tsapp.Sprite("IconPlus.png", 0, 445)
add_button.scale = 0.2
window.add_object(add_button)
add_label = tsapp.TextLabel("OpenSans-Bold.ttf", 30, 100, 525, 1000, "Add todo")
window.add_object(add_label)

display_todos()

while window.is_running:
    window.finish_frame()
    mouse_x, mouse_y = tsapp.get_mouse_position()
    for checkbox in checkboxes:
        if tsapp.was_mouse_pressed() and checkbox.is_colliding_point(mouse_x, mouse_y):
            delete_todo(checkbox)
    if tsapp.was_mouse_pressed() and add_button.is_colliding_point(mouse_x, mouse_y):
        add_todo()
