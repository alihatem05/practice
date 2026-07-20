from database import (
    init_db,
    add_task,
    get_tasks,
    delete_task
)

init_db()


def create_task(title: str):
    add_task(title)


def list_tasks():
    return get_tasks()


def remove_task(task_id: int):
    return delete_task(task_id)