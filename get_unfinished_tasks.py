import sqlite3
from connect import create_connection, database 

def get_unfinished_tasks(conn):
    
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM tasks
        WHERE status_id != (SELECT id FROM status WHERE name = 'completed')
    """)
    unfinished_tasks = cursor.fetchall()
    return unfinished_tasks

if __name__ == '__main__':
    with create_connection(database) as conn:
        unfinished_tasks = get_unfinished_tasks(conn)
        if unfinished_tasks:
            print("Unfinished tasks:")
            for task in unfinished_tasks:
                print(task)
        else:
            print("No unfinished tasks found.")
