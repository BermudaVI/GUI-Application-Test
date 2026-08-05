import tkinter as tk
import customtkinter as ctk
import theme


def build_top_bar(parent):
    print("I need help")

# Tasks page
def build(parent):
    frame = ctk.CTkFrame(parent, fg_color=theme.CONTENT_BG)

    # Universal grid setup
    frame.grid(
        row = 0,
        column = 0,
        sticky = "nsew",
        padx = theme.WINDOW_PAD,
        pady = theme.WINDOW_PAD
        )

    # Tasks page setup

    # Widget declarations
    header_text = ctk.CTkLabel(
        frame,
        text="Tasks",
        text_color=theme.TEXT,
        font=theme.HEADING_FONT,
        anchor="w"
    )

    new_task_btn = ctk.CTkButton(
        frame,
        text= "+ New Task",
        text_color=theme.TEXT,
        font=theme.BODY_FONT,
        anchor="e"
    )

    new_list_btn = ctk.CTkButton(
        frame,
        text= "+ New List",
        text_color=theme.TEXT,
        font=theme.BODY_FONT
    )

    tasks_area = ctk.CTkScrollableFrame(
        frame,
        )

    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    header_text.grid(
        row=0,
        column=0,
        sticky="w",
        padx=theme.WINDOW_PAD,
        pady=theme.WINDOW_PAD
    )

    new_task_btn.grid(
        row=0,
        column=1,
        sticky="e",
        padx=theme.WINDOW_PAD,
        pady=theme.WINDOW_PAD
    )
    
    tasks_area.grid(
        row=2,
        columnspan=2,
        sticky="nsew",
        )


    return frame