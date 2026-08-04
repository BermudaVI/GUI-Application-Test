from layout import create_app, create_frames
from pages import sidebar, header, tasks

# Creates window and frames in window
app = create_app()
frames = create_frames(app)

# Creates sidebar and header content
sidebar_buttons = sidebar.build(frames["sidebar"])
header_buttons = header.build(frames["header"])

tasks_page = tasks.build(frames["content"])

app.mainloop()