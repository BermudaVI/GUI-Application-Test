import tkinter as tk
import customtkinter as ctk
import theme
from layout import build_page_frame
from widgets.task import TaskWidget, Task


# Tasks specific funcs
def new_task():
    print("new task")

def new_list():
    print("new list")

# Tasks page
def build(parent):
    frame = build_page_frame(parent)

    # Tasks page setup
    # Widget declarations
    header_text = ctk.CTkLabel(
        frame,
        text="Tasks",
        text_color=theme.TEXT,
        font=theme.SMALL_HEADING_FONT,
        anchor="w"
    )

    new_task_btn = ctk.CTkButton(
        frame,
        text= "+ New Task",
        text_color=theme.TEXT,
        font=theme.BUTTON_FONT,
        fg_color="transparent",
        anchor="e",
        width=1,
        command=new_task
    )

    new_list_btn = ctk.CTkButton(
        frame,
        text= "+ New List",
        text_color=theme.TEXT,
        font=theme.BUTTON_FONT,
        fg_color="transparent",
        anchor="e",
        width=1,
        command=new_list
    )

    search_bar = ctk.CTkEntry(
        frame,
        placeholder_text="Search...",
        text_color=theme.TEXT,
        justify="left",
        border_width=0,
        fg_color=theme.CONTENT_BG,
        font=theme.BODY_FONT
    )

    tasks_area = ctk.CTkScrollableFrame(
        frame
    )

    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=0)
    frame.grid_columnconfigure(1, weight=1)

    header_text.grid(
        row=0,
        column=0,
        sticky="w",
        padx=theme.PAGE_SIDES,
        pady=theme.PAGE_TOP
    )

    new_task_btn.grid(
        row=0,
        column=1,
        sticky="e",
        padx=theme.PAGE_SIDES,
        pady=theme.PAGE_TOP
    )

    search_bar.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=theme.PAGE_SIDES,
        pady=theme.SECTION
    )

    new_list_btn.grid(
        row=1,
        column=1,
        sticky="e",
        padx=theme.PAGE_SIDES,
        pady=theme.SECTION
    )

    tasks_area.grid(
        row=2,
        column=0,
        columnspan=2,
        sticky="nsew",
        padx=theme.PAGE_SIDES,
        pady=theme.PAGE_BOTTOM
    )

    # Get Task Data
    tasks = [
        {
            "kind": "tasks#task",
            "id": "THo0TFhVbEtENlNlZHZLSA",
            "etag": "\"QHPfUrSKoUU\"",
            "title": "Test",
            "updated": "2026-08-08T06:35:41.778Z",
            "selfLink": "https://www.googleapis.com/tasks/v1/lists/MDA5MjI5MzkyMTY5MTg2OTAyNTc6MDow/tasks/THo0TFhVbEtENlNlZHZLSA",
            "position": "00000000000000000000",
            "notes": "Details Here.",
            "status": "needsAction",
            "due": "2026-08-15T00:00:00.000Z",
            "links": [],
            "webViewLink": "https://tasks.google.com/task/Lz4LXUlKD6SedvKH?sa=6"
        },
        {
            "kind": "tasks#task",
            "id": "d0JnWDhqa2JEQ2F1RzZaag",
            "etag": "\"XunNpZhfTY8\"",
            "title": "Test2",
            "updated": "2026-08-08T06:24:47.060Z",
            "selfLink": "https://www.googleapis.com/tasks/v1/lists/MDA5MjI5MzkyMTY5MTg2OTAyNTc6MDow/tasks/d0JnWDhqa2JEQ2F1RzZaag",
            "position": "00000000000000000001",
            "notes": "Other Details Here.",
            "status": "needsAction",
            "due": "2026-08-15T00:00:00.000Z",
            "links": [],
            "webViewLink": "https://tasks.google.com/task/wBgX8jkbDCauG6Zj?sa=6"
        }
    ]

    # Create Task Widgets

    for data in tasks:
        task = Task(
        data["id"],
        data["title"],
        data.get("due"),
        data["position"],
        data.get("notes"),
        data["status"]
    )

    task1 = TaskWidget(
        tasks_area,
        task
    )

    task1.pack(
        fill="x",
        padx=theme.CARD_INSET,
        pady=theme.FRAME_GAP
    )

    return frame

