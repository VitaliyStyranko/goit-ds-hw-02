import sqlite3
from connect import create_connection, database


def get_tasks_by_status(conn, status_name):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM tasks 
        WHERE status_id = (SELECT id FROM status WHERE name = ?)
    """, (status_name,))
    tasks_with_status = cursor.fetchall()
    return tasks_with_status


if __name__ == '__main__':
    status_name_to_query = 'new'  # desired status name

    with create_connection(database) as conn:
        tasks = get_tasks_by_status(conn, status_name_to_query)
        if tasks:
            print(f"Tasks with status '{status_name_to_query}':")
            for task in tasks:
                print(task)
        else:
            print(f"No tasks found with status '{status_name_to_query}'")
