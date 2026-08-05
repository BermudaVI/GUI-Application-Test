import tkinter as tk
import customtkinter as ctk
import theme

ctk.set_appearance_mode("system")

# Frame data
FRAME_SPECS = [
    {
        "name": "header",
        "row": 0,
        "column": 0,
        "columnspan": 2,
        "padx": theme.WINDOW_PAD,
        "pady": (theme.WINDOW_PAD, theme.FRAME_GAP),
        "color": theme.HEADER_BG,
        "sticky": "ew"
    },
    {
        "name": "sidebar",
        "row": 1,
        "column": 0,
        "padx": (theme.WINDOW_PAD, theme.FRAME_GAP),
        "pady": (theme.FRAME_GAP, theme.WINDOW_PAD),
        "color": theme.SIDEBAR_BG,
        "sticky": "nsw"
    },
    {
        "name": "content",
        "row": 1,
        "column": 1,
        "padx": (theme.FRAME_GAP, theme.WINDOW_PAD),
        "pady": (theme.FRAME_GAP, theme.WINDOW_PAD),
        "color": theme.CONTENT_BG,
        "sticky": "nsew"
    }
]

def create_app():
    # Creates widnow and defines properties
    app = ctk.CTk()
    app.minsize(600, 450)
    app.title("Workspace Dashboard")
    app.resizable(True, True)
    app.configure(fg_color=theme.WINDOW_BG)

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
            border_width=spec.get("border_width", 0)
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

