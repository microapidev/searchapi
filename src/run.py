import os
from src.app import create_app, db
import flask_whooshalchemy as wa
from src.app.models.models import Movies

app = create_app()
wa.whoosh_index(app, Movies)


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Movies": Movies}
