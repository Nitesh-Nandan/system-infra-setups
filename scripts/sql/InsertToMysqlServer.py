import mysql.connector
from faker import Faker
from mysql.connector import Error
from db_query_generator import MySqlQueryGenerator

faker = Faker()

# Your table config goes here
table_config = {
    'table_name': 'users',
    'rows': 5,
    'columns': ['firstName', 'lastName', 'age', 'city'],
    'values': [lambda: faker.first_name(), lambda: faker.last_name(), lambda: faker.random_int(min=18, max=80),
               lambda: faker.city()]
}

# Your Mysql config goes here
mysql_config = {
    'host': 'localhost',
    'database': 'airlines',
    'user': 'root',
    'password': 'password'
}


# Don't modify any code below this line
def run_query():
    connection = getMySqlConnection()
    if connection is None:
        print("Failed to connect to the database")
        return
    cursor = connection.cursor()
    try:
        itr = 0
        while itr < 5:
            query = MySqlQueryGenerator(table_config)
            print(query)
            cursor.execute(query)
            connection.commit()
            print(f"Records Inserted Iteration: {itr}")
            itr += 1

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def getMySqlConnection():
    connection = mysql.connector.connect(
        host=mysql_config['host'],
        user=mysql_config['user'],
        database=mysql_config['database'],
        password=mysql_config['password']
    )

    if connection.is_connected():
        print("Connected to MySQL database")
        return connection
    else:
        print("Connection failed to MySql Database")
        return None


def databaseSetup(cursor):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_config['database']}")
    cursor.execute(f"Use {mysql_config['database']}")


if __name__ == "__main__":
    run_query()
