from layout import create_app, create_frames
from pages import sidebar, header, tasks
import theme

# Creates window and frames in window
app = create_app()
theme.init_fonts()
frames = create_frames(app)

frames["content"].grid_rowconfigure(0, weight=1)
frames["content"].grid_columnconfigure(0, weight=1)



# Creates sidebar and header content
sidebar_buttons = sidebar.build(frames["sidebar"])
header_buttons = header.build(frames["header"])

tasks_page = tasks.build(frames["content"])

# pages = {
#     "tasks": tasks.build(frames["content"]),
#     "calendar": calendar.build(frames["content"]),
#     "drive": drive.build(frames["content"]),
# }


app.mainloop()