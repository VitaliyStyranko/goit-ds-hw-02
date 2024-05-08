import sqlite3
from connect import create_connection, database


def get_user_tasks(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
    user_tasks = cursor.fetchall()
    return user_tasks


if __name__ == '__main__':

    tasks_for_user_id = 1  # desired user id

    with create_connection(database) as conn:
        tasks = get_user_tasks(conn, tasks_for_user_id)
        if tasks:
            print(f"Tasks for User id {tasks_for_user_id}:")
            for task in tasks:
                print(f"Task id: {task[0]}, Title: {task[1]}, Description: {task[2]}")
        else:
            print(f"No tasks found for user id: {tasks_for_user_id}")
