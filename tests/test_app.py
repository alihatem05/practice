import os

import app
import database


def setup_function():
    if os.path.exists("tasks.db"):
        os.remove("tasks.db")

    database.init_db()


def test_create_task():

    app.create_task("Learn GitHub Actions")

    tasks = app.list_tasks()

    assert len(tasks) == 1
    assert tasks[0][1] == "Learn GitHub Actions"


def test_delete_task():

    app.create_task("Docker")

    task_id = app.list_tasks()[0][0]

    deleted = app.remove_task(task_id)

    assert deleted == 1
    assert app.list_tasks() == []


def test_delete_missing_task():

    deleted = app.remove_task(999)

    assert deleted == 0