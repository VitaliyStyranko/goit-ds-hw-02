import sqlite3
from connect import create_connection, database


def get_tasks_for_users_with_email_domain(conn, email_domain):
    cursor = conn.cursor()
    cursor.execute("""SELECT tasks.* FROM tasks 
                   JOIN users ON tasks.user_id = users.id 
                   WHERE users.email LIKE '%@example.net'""")  # desired email domain

    tasks_for_users_with_email_domain = cursor.fetchall()
    return tasks_for_users_with_email_domain


if __name__ == '__main__':
    email_domain_to_search = 'example.net'  # desired email domain

    with create_connection(database) as conn:
        tasks = get_tasks_for_users_with_email_domain(conn, email_domain_to_search)
        if tasks:
            print("Tasks for users with email domain '%s':" % email_domain_to_search)
            for task in tasks:
                print(task)
        else:
            print(f"No tasks found for users with email domain '{email_domain_to_search}'")
