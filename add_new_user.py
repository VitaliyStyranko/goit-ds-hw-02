import sqlite3
from connect import create_connection, database  # Assuming 'connect.py' contains your connection functions


def add_new_user(conn, fullname, email):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))
    conn.commit()
    print(f"New user '{fullname}' added successfully.")


if __name__ == '__main__':
    new_user_fullname = "James Bond"  # desired full name
    new_user_email = "james.bond@example.org"  # desired email address

    with create_connection(database) as conn:
        add_new_user(conn, new_user_fullname, new_user_email)
