from faker import Faker
import os
from db_query_generator import MySqlQueryGenerator

faker = Faker()

# Your table config goes here
table_config = {
    'table_name': 'users',
    'database': 'airlines',
    'rows': 1000,
    'columns': ['firstName', 'lastName', 'age', 'city'],
    'values': [lambda: faker.first_name(), lambda: faker.last_name(), lambda: faker.random_int(min=18, max=80),
               lambda: faker.city()]
}

# change the path if needed
resource_dir = "/Users/niteshnandan/workspace/system-infra-setups/resources/generated"
sql_file_name = f"{resource_dir}/001-usersTable.sql"

# Don't change any code below this line
with open(sql_file_name, "w") as file:
    for i in range(100):  # Simulate a stream with 10 chunks of data
        query = MySqlQueryGenerator(table_config)
        file.write(query)
        file.write("\n\n")

        file.flush()

print("Data stream written to file successfully.")
