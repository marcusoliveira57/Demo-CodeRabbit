import sqlite3


def connect_db():
    return sqlite3.connect("banco.db")


def get_user(user_id):
    with connect_db() as db:
        return db.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,),
        ).fetchall()
