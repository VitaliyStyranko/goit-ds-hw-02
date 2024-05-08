import sqlite3
from connect import create_connection, database 


def update_task_status(conn, task_id, new_status_name):
    
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM status WHERE name = ?", (new_status_name,))
    new_status_id = cursor.fetchone()
    if new_status_id:
        cursor.execute("UPDATE tasks SET status_id = ? WHERE id = ?", (new_status_id[0], task_id))
        conn.commit()
        print(f"Task {task_id} status updated to '{new_status_name}'")
    else:
        print(f"Status '{new_status_name}' not found.")


if __name__ == '__main__':

    task_id_to_update = 3  # desired task id
    new_status_name = 'completed'  # desired new status name

    with create_connection(database) as conn:
        update_task_status(conn, task_id_to_update, new_status_name)
