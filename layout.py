import tkinter as tk
import customtkinter as ctk
import theme

# ctk.set_appearance_mode("system")

# Frame data
FRAME_SPECS = [
    {
        "name": "header",
        "row": 0,
        "column": 0,
        "columnspan": 2,
        "padx": 5,
        "pady": (5, 2.5),
        "color": theme.HEADER,
        "sticky": "ew"
    },
    {
        "name": "sidebar",
        "row": 1,
        "column": 0,
        "padx": (5, 2.5),
        "pady": (2.5, 5),
        "color": theme.SIDEBAR,
        "sticky": "nsw"
    },
    {
        "name": "content",
        "row": 1,
        "column": 1,
        "padx": (2.5, 5),
        "pady": (2.5, 5),
        "color": theme.CONTENT,
        "sticky": "nsew"
    }
]

def create_app():
    # Creates widnow and defines properties
    app = ctk.CTk()
    app.minsize(600, 450)
    app.title("GUI Experiments")
    app.resizable(True, True)
    app.configure(fg_color=theme.WINDOW)

    # Grid weight config
    app.grid_rowconfigure(0, weight=0) # header
    app.grid_rowconfigure(1, weight=1) # sidebar, content, etc.

    app.grid_columnconfigure(0, weight=0) # sidebar
    app.grid_columnconfigure(1, weight=1) # content

    return app

# Create's frames, places into a dict. Returns dict.
def create_frames(app):
    frames = {}
    for spec in FRAME_SPECS:
        frame = ctk.CTkFrame(master=app)
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

