import customtkinter as ctk
import theme

def show_home():
    print("home")

def show_tasks():
    print("tasks")

def show_calendar():
    print("calendar")

# Button data
button_specs = [
    {
        "name": "home_btn",
        "text": "Home",
        "row": 0,
        "command": show_home
    },
    {
        "name": "tasks_btn",
        "text": "Tasks",
        "row": 1,
        "command": show_tasks
    },
    {
        "name": "calendar_btn",
        "text": "Calendar",
        "row": 2,
        "command": show_calendar
    }
]

# Forms sidebar content
def build(parent):
    parent.grid_columnconfigure(0, weight=1)

    buttons = {}
    for spec in button_specs:
        btn = ctk.CTkButton(
            master=parent,
            text = spec["text"],
            fg_color = theme.SIDEBAR_BTN_FG,
            text_color= theme.SIDEBAR_BTN_TEXT,
            hover_color= theme.SIDEBAR_BTN_HOVER,
            command = spec["command"]
        )

        btn.grid(
            row = spec["row"],
            sticky = "ew",
            padx = 5,
            pady = 2.5
        )

        buttons[spec["name"]] = btn
    return buttons


