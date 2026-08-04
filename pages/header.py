import customtkinter as ctk
import theme

def toggle_sidebar():
    print("sidebar toggled")

def refresh():
    print("refresh")

# Button data
BUTTON_SPECS = [
    {
        "name": "sidebar_toggle_btn",
        "text": "hmbrgr",
        "column": 0,
        "command": toggle_sidebar,
        "anchor": "w",
        "sticky": "w",
        "padx": theme.HEADER_LEFT_BTN_PADX,
        "pady": theme.HEADER_BTN_PADY
    },
    {
        "name": "refresh_btn",
        "text": "refresh",
        "column": 1,
        "command": refresh,
        "anchor": "e",
        "sticky": "e",
        "padx": theme.HEADER_RIGHT_BTN_PADX,
        "pady": theme.HEADER_BTN_PADY
    },
]

# Forms sidebar content
def build(parent):
    parent.grid_columnconfigure(1, weight=1)

    buttons = {}
    for spec in BUTTON_SPECS:
        btn = ctk.CTkButton(
            master=parent,
            text = spec["text"],
            fg_color = theme.SIDEBAR_BTN_FG,
            text_color = theme.SIDEBAR_BTN_TEXT,
            anchor = spec.get("anchor", "center"),
            hover_color = theme.SIDEBAR_BTN_HOVER,
            command = spec["command"]
        )

        btn.grid(
            column=spec["column"],
            row=0,
            sticky=spec.get("sticky"),
            padx=spec.get("padx", 0),
            pady=spec.get("pady", 2.5),
        )

        buttons[spec["name"]] = btn
    return buttons