import flet as ft

def main(page: ft.Page):
    page.title = "Todo List Manager"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tasks = []

    task_input = ft.TextField(
        label="Enter a new task",
        width=300
    )

    tasks_listview = ft.ListView(
        expand=True,
        spacing=10,
        padding=10
    )

    def on_delete_task(task_row):
        def delete(e):
            tasks_listview.controls.remove(task_row)
            page.update()
        return delete

    def on_add_task(e):
        if task_input.value:
            task_text = ft.Text(task_input.value)
            task_checkbox = ft.Checkbox()
            delete_button = ft.IconButton(
                icon=ft.Icons.DELETE,
                on_click=on_delete_task(None)  # Will be set properly below
            )

            task_row = ft.Row(
                controls=[task_checkbox, task_text, delete_button],
                spacing=10
            )

            # Update the delete button's event function with the task_row
            delete_button.on_click = on_delete_task(task_row)

            tasks_listview.controls.append(task_row)
            tasks.append({"checkbox": task_checkbox, "text": task_text})

            task_input.value = ""
            page.update()

    add_button = ft.ElevatedButton(
        text="Add Task",
        on_click=on_add_task
    )

    input_container = ft.Row(
        controls=[task_input, add_button],
        spacing=10
    )

    page.add(input_container, tasks_listview)

ft.app(target=main)