import sqlite3
from connect import create_connection, database


def add_task_for_user(conn, user_id, title, description, status_id):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (?, ?, ?, ?)
    """, (title, description, status_id, user_id))
    conn.commit()
    print(f"New task: '{task_title}', title: '{task_description}' added for user id {user_id}")


if __name__ == '__main__':
    user_id_to_assign_task = 5  # desired user id
    task_title = "Supper Task"
    task_description = "This is a new task."
    task_status_id = 1  # desired status id

    with create_connection(database) as conn:
        add_task_for_user(conn, user_id_to_assign_task, task_title, task_description, task_status_id)
