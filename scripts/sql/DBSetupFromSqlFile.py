import mysql.connector

# Database connection details
resource_dir = "/Users/niteshnandan/workspace/system-infra-setups/resources/"
config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost'
}

file_path = f"{resource_dir}/airlines/001-airlines-schema.sql"

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

with open(file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# Split the script into individual statements
sql_statements = sql_script.split(';')

# Execute each statement
for statement in sql_statements:
    if statement.strip():  # Skip empty statements
        cursor.execute(statement)

connection.commit()

cursor.close()
connection.close()

print("SQL script executed successfully.")
