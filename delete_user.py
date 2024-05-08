import sqlite3
from connect import create_connection, database  # Assuming 'connect.py' contains your connection functions


def delete_user(conn, user_id):

    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print(f"User with ID {user_id} deleted successfully.")


if __name__ == '__main__':
    user_id_to_delete = 6  # Change this to the id of the user you want to delete

    with create_connection(database) as conn:
        delete_user(conn, user_id_to_delete)
