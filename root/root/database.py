import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        print('Start connection')
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection(
    db_name='pg_database',
    db_host='127.0.0.1',
    db_port='5432',
    db_user='postgres',
    db_password='postgres',
)

with connection.cursor() as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS client (id serial primary key, email varchar unique, phone_number varchar, firstname varchar, surname varchar, fathersname varchar, pasport varchar, balance double precision);")
    connection.commit()

# with connection.cursor() as cur:
#     cur.execute("INSERT INTO client VALUES (2, 'qwe@qwe.ru', '89385384096', 'Олег', 'ewq', null, '1234 123456', null);")
#     connection.commit()
