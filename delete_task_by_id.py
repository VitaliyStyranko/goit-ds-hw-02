import sqlite3
from connect import create_connection, database 

def delete_task_by_id(conn, task_id):
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print(f"Task with ID {task_id} deleted successfully.")

if __name__ == '__main__':
    task_id_to_delete = 16  # desired task id

    with create_connection(database) as conn:
        delete_task_by_id(conn, task_id_to_delete)
