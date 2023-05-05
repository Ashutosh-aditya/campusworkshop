"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaak1u7avj5o493k5qg-a.oregon-postgres.render.com",
        database="todo_87wz",
        user="todo_87wz_user",
        password="V1DpI39berf4kqAgWV8oA1klPR7iZc5b")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
