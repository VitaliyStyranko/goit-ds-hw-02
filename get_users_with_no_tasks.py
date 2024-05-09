import sqlite3
from connect import create_connection, database


def get_users_without_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);
    """)
    users_without_tasks = cursor.fetchall()
    return users_without_tasks


if __name__ == '__main__':
    with create_connection(database) as conn:
        users = get_users_without_tasks(conn)
        if users:
            print("Users without tasks:")
            for user in users:
                print(user)
        else:
            print("All users have tasks assigned.")
