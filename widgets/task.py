import customtkinter as ctk
import theme

class Task:
    def __init__(self, task_id, title, due, position, notes, status):
        self.id = task_id
        self.title = title
        self.due = due
        self.position = position
        self.notes = notes
        self.status = status

class TaskWidget(ctk.CTkFrame):
    def __init__(self, parent, task):
        super().__init__(
            parent,
            fg_color=theme.CONTENT_BG,
            border_color=theme.BORDER,
            border_width=1
            )

        # Grabs the values from tasks
        self.task = task

        self.checkbox = ctk.CTkCheckBox(
            self,
            fg_color=theme.ACCENT,
            hover_color=theme.ACCENT,
            border_color=theme.TEXT_SECONDARY,
            border_width=1,
            text=task.title,
            text_color=theme.TEXT,
            font=theme.BODY_FONT
        )

        self.due_date_label = ctk.CTkLabel(
            self,
            text=task.due,
            text_color=theme.TEXT_SECONDARY,
            font=theme.SMALL_FONT,
            anchor="w"
        )

        self.details_label = ctk.CTkLabel(
            self,
            text=task.notes,
            text_color=theme.TEXT_SECONDARY,
            font=theme.SMALL_FONT,
            anchor="w"
        )

        self.grid_columnconfigure(0, weight=0) # Checkbox
        self.grid_columnconfigure(1, weight=1) # Task name
        self.grid_columnconfigure(2, weight=0) # Due date
        self.grid_columnconfigure(3, weight=1) # Details

        self.checkbox.grid(
            row=0,
            column=0,
            padx=theme.CARD_INSET,
            pady=theme.FRAME_GAP
        )

        self.due_date_label.grid(
            row=0,
            column=2,
            sticky="w",
            padx=theme.FRAME_GAP,
            pady=theme.FRAME_GAP
        )

        self.details_label.grid(
            row=0,
            column=3,
            sticky="w",
            padx=theme.FRAME_GAP,
            pady=theme.FRAME_GAP
        )