import sqlite3
from connect import create_connection, database
def find_users_by_email(conn, email_pattern):
    
    cursor = conn.cursor()
    cursor.execute("SELECT id, fullname, email FROM users WHERE email LIKE ?", (email_pattern,))
    
    matching_users = cursor.fetchall()
    return matching_users

if __name__ == '__main__':
    email_pattern_to_search = '%@example.net'  # desired user email

    with create_connection(database) as conn:
        matching_users = find_users_by_email(conn, email_pattern_to_search)
        if matching_users:
            for user in matching_users:
                #  print(f"User ID: {user[0]}, Email: {user[1]}")
                print(f"Users with matching email addresses: {user}")
                # print(user)
        else:
            print("No users found with matching email addresses.")
