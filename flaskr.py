# all the imports
import sqlite3
from flask import Flask, request, sessions, g, redirect, url_for, abort, render_template, flash
from __future__ import with_statement
from contextlib import closing

# configuration
DATABASE = 'tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request():
    g.db.close()

if __name__ == '__main__':
    app.run()