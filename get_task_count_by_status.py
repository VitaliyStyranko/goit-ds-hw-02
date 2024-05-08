import sqlite3
from connect import create_connection, database  

def get_task_count_by_status(conn):
    
    cursor = conn.cursor()
    cursor.execute("""
        SELECT status.name, COUNT(tasks.id) AS task_count
        FROM status LEFT JOIN tasks ON status.id = tasks.status_id
        GROUP BY status.name
    """)
    task_counts = cursor.fetchall()
    return task_counts

if __name__ == '__main__':
    with create_connection(database) as conn:
        task_counts = get_task_count_by_status(conn)
        if task_counts:
            print("Task counts by status:")
            for status, count in task_counts:
                print(f"{status}: {count}")
        else:
            print("No task counts found.")
