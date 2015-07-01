from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

#Set up logging if application has not been started in debug mode
if not app.debug:
    import logging
    import sys

    # Create log format
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s','%Y-%m-%d %H:%M:%S')

    # Create console handler
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    # Enable log handlers
    app.logger.addHandler(console)

    app.config.from_object(os.environ.get('SETTINGS'))
