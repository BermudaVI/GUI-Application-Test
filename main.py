from layout import create_app, create_frames

app = create_app()
frames = create_frames(app)

app.mainloop()