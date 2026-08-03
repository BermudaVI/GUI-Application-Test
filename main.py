import tkinter as tk
import customtkinter as ctk

# Window Properties
app = ctk.CTk()
app.minsize(600, 450)
app.title("GUI Experiments")
app.resizable(True, True)

# Grid weight config
app.grid_rowconfigure(0, weight=0) # header
app.grid_rowconfigure(1, weight=1) # sidebar, content, etc.

app.grid_columnconfigure(0, weight=0) # sidebar
app.grid_columnconfigure(1, weight=1) # content

# Frame data
frame_specs = [
    # Name, row, col, padx, pady, bg_color
    {
        "name": "header",
        "height": 100,
        "row": 0,
        "column": 0,
        "columnspan": 2,
        "padx": 2,
        "pady": 2,
        "color": "#ffffff",
        "sticky": "ew"
    },
    {
        "name": "sidebar",
        "row": 1,
        "column": 0,
        "padx": 5,
        "pady": 5,
        "color": "#ff0000",
        "sticky": "nsw"
    },
    {
        "name": "content",
        "row": 1,
        "column": 1,
        "padx": 5,
        "pady": 5,
        "color": "#0011ff",
        "sticky": "nsew"
    }
]

# Puts created frames into frames dict.
frames = {}
for spec in frame_specs:
    frame = ctk.CTkFrame(app, fg_color=spec["color"])

    if "width" in spec:
        frame.configure(width=spec["width"])
    if "height" in spec:
        frame.configure(height=spec["height"])

    frame.grid(
               row=spec["row"],
               column=spec["column"],
               padx=spec["padx"],
               pady=spec["pady"],
               sticky=spec.get("sticky", "nsew"),
               columnspan=spec.get("columnspan", 1),
               rowspan=spec.get("rowspan", 1)
               )
    frames[spec["name"]] = frame


app.mainloop()
