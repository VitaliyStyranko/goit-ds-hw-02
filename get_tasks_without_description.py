import sqlite3
from connect import create_connection, database


def get_tasks_without_description(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM tasks
        WHERE description IS NULL OR description = ''
    """)
    tasks_without_description = cursor.fetchall()
    return tasks_without_description


if __name__ == '__main__':
    with create_connection(database) as conn:
        tasks = get_tasks_without_description(conn)
        if tasks:
            print("Tasks without description:")
            for task in tasks:
                print(task)
        else:
            print("No tasks found without description.")
