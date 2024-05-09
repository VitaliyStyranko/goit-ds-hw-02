import sqlite3
import faker
import random
from connect import create_connection, database


def generate_data(conn):
    
    fake = faker.Faker()

    num_users = 5
    num_statuses = 3
    num_tasks = 15

    for _ in range(num_users):
        fullname = fake.name()
        email = fake.email()
        conn.execute('INSERT INTO users (fullname, email) VALUES (?, ?)', (fullname, email))

    status_names = ['new', 'in progress', 'completed']
    for status_name in status_names:
        conn.execute('INSERT INTO status (name) VALUES (?)', (status_name,))

    for _ in range(num_tasks):
        title = fake.sentence()
        description = fake.paragraph()
        status_id = random.randint(1, num_statuses)
        user_id = random.randint(1, num_users)

        
        cursor = conn.cursor()

        cursor.execute('SELECT 1 FROM users WHERE id = ?', (user_id,))
        user_exists = cursor.fetchone() is not None

        cursor.execute('SELECT 1 FROM status WHERE id = ?', (status_id,))
        status_exists = cursor.fetchone() is not None

        if user_exists and status_exists:
            conn.execute('INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)',
                        (title, description, status_id, user_id))
        else:
            print(f"Invalid foreign key references (user: {user_id}, status: {status_id})")

    conn.commit()
                

if __name__ == '__main__':
    with create_connection(database) as conn:
        generate_data(conn)
        print(f"Database '{database}' successfully populated with seed data.")
                   








   


