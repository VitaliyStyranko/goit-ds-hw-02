import sqlite3
from connect import create_connection, database


def get_users_and_tasks_in_progress(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT users.fullname, tasks.title
        FROM users
        INNER JOIN tasks ON users.id = tasks.user_id
        INNER JOIN status ON tasks.status_id = status.id
        WHERE status.name = 'in progress'
    """)
    users_and_tasks_in_progress = cursor.fetchall()
    return users_and_tasks_in_progress


if __name__ == '__main__':
    with create_connection(database) as conn:
        users_and_tasks = get_users_and_tasks_in_progress(conn)
        if users_and_tasks:
            print("Users and their tasks in 'in progress' status:")
            for user, task in users_and_tasks:
                print(f"User: {user}, Task: {task}")
        else:
            print("No users and tasks found in 'in progress' status.")
