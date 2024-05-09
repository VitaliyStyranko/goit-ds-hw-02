import sqlite3
from connect import create_connection, database


def get_users_and_task_counts(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT users.fullname, COUNT(tasks.id) AS task_count
        FROM users
        LEFT JOIN tasks ON users.id = tasks.user_id
        GROUP BY users.id
    """)
    users_and_task_counts = cursor.fetchall()
    return users_and_task_counts


if __name__ == '__main__':
    with create_connection(database) as conn:
        users_and_task_counts = get_users_and_task_counts(conn)
        if users_and_task_counts:
            print("Users and their task counts:")
            for user, task_count in users_and_task_counts:
                print(f"User: {user}, Task Count: {task_count}")
        else:
            print("No users found.")
