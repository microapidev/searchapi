import os
from src.app import create_app, db
from src.app.models.models import Movies

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Movies": Movies}
