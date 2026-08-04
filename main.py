from layout import create_app, create_frames
from pages import sidebar

# Creates window and frames in window
app = create_app()
frames = create_frames(app)

# Creates sidebar buttons in sidebar
sidebar_buttons = sidebar.build(frames["sidebar"])

app.mainloop()