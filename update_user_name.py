import sqlite3
from connect import create_connection, database 

def update_user_name(conn, user_id, new_name):
    
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET fullname = ? WHERE id = ?", (new_name, user_id))
    conn.commit()
    print(f"User with ID {user_id} name updated to '{new_name}'")

if __name__ == '__main__':
    user_id_to_update = 4  # desired user id
    new_name = "James Bond 007"  # desired new name

    with create_connection(database) as conn:
        update_user_name(conn, user_id_to_update, new_name)
