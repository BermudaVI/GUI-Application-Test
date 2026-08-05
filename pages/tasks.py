import tkinter as tk
import customtkinter as ctk
import theme
from layout import build_page_frame

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


    return frame