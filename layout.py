import tkinter as tk
import customtkinter as ctk

# ctk.set_appearance_mode("system")

def create_app():
    # Creates widnow and defines properties
    app = ctk.CTk()
    app.minsize(600, 450)
    app.title("GUI Experiments")
    app.resizable(True, True)

    # Grid weight config
    app.grid_rowconfigure(0, weight=0) # header
    app.grid_rowconfigure(1, weight=1) # sidebar, content, etc.

    app.grid_columnconfigure(0, weight=0) # sidebar
    app.grid_columnconfigure(1, weight=1) # content

    return app

# Create's frames, places into a dict. Returns dict.
def create_frames(app):
    frames = {}
    for spec in frame_specs:
        frame = ctk.CTkFrame(app)
        frame.configure(
            fg_color=spec.get("color", "transparent"),
            width=spec.get("width"),
            height=spec.get("height"),
            border_width=spec.get("border_width", 0),
        )

        if "border_color" in spec:
            frame.configure(border_color=spec["border_color"])
            
        frame.grid(
                row=spec["row"],
                column=spec["column"],
                padx=spec.get("padx", 0),
                pady=spec.get("pady", 0),
                sticky=spec.get("sticky", "nsew"),
                columnspan=spec.get("columnspan", 1),
                rowspan=spec.get("rowspan", 1),
                )
        frames[spec["name"]] = frame
    return frames

# Frame data
frame_specs = [
    {
        "name": "header",
        "row": 0,
        "column": 0,
        "columnspan": 2,
        "padx": 5,
        "pady": (5, 2.5),
        "color": "#bbe44b",
        "sticky": "ew"
    },
    {
        "name": "sidebar",
        "row": 1,
        "column": 0,
        "padx": (5, 2.5),
        "pady": (2.5, 5),
        "color": "#ff0000",
        "sticky": "nsw"
    },
    {
        "name": "content",
        "row": 1,
        "column": 1,
        "padx": (2.5, 5),
        "pady": (2.5, 5),
        "color": "#0011ff",
        "sticky": "nsew"
    }
]