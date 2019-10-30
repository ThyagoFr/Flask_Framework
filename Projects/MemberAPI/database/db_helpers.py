import sqlite3
from flask import g
from pathlib import Path

path = Path(__file__).parent.absolute()

def db_connect():
    sql = sqlite3.connect(str(path) + "/members.db")
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g,"sqlite3_db"):
        g.sqlite3_db = db_connect()
    return g.sqlite3_db