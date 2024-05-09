from sqlite3 import Error
from connect import create_connection, database


def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_users_table = '''
      CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      fullname VARCHAR(100) NOT NULL,
      email VARCHAR(100) UNIQUE NOT NULL
      );
      '''
    sql_create_status_table = '''
      CREATE TABLE IF NOT EXISTS status (
      id INTEGER PRIMARY KEY,
      name VARCHAR(50) UNIQUE NOT NULL
      );
      '''
    sql_create_tasks_table = '''
      CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title VARCHAR(100),
      description TEXT,
      status_id INTEGER NOT NULL,
      user_id INTEGER NOT NULL,
      FOREIGN KEY (status_id) REFERENCES status (id) ON DELETE CASCADE,
      FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
      );
      '''

with create_connection(database) as conn:
    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_status_table)
        create_table(conn, sql_create_tasks_table)
        print("Tables created successfully")
    else:
        print("Error! Cannot create the database connection.")

