import sqlite3

DATABASE = "tasks.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_task(title):
    conn = get_connection()

    conn.execute(
        "INSERT INTO tasks(title) VALUES (?)",
        (title,)
    )

    conn.commit()
    conn.close()


def get_tasks():
    conn = get_connection()

    tasks = conn.execute(
        "SELECT id, title FROM tasks"
    ).fetchall()

    conn.close()

    return tasks


def delete_task(task_id):
    conn = get_connection()

    cursor = conn.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return cursor.rowcount