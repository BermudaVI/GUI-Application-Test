import tkinter as tk
import customtkinter as ctk
import theme

def build_top_bar():
    print("I need help")

# Tasks page
def build_page(parent):
    frame = ctk.CTkFrame(parent, fg_color=theme.CONTENT_BG)
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_columnconfigure(0, weight=1)

    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # To be modified 
    frame.grid(sticky="nsew")
    return frame