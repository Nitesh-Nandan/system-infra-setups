"""
Don't Modify this file.
"""


def MySqlQueryGenerator(config):
    validate_sql_config(config)

    table_name = config['table_name']
    database = config['database']
    num_rows = 5 if 'rows' not in config else config['rows']
    columns = config['columns']
    values_functions = config['values']

    values_list = []
    for _ in range(num_rows):
        values = [func() for func in values_functions]
        values_list.append(values)

    columns_str = ', '.join(f'`{col}`' for col in columns)
    values_str = ',\n\t'.join([f"({', '.join(repr(value) for value in values)})" for values in values_list])
    query = f"INSERT INTO {database}.`{table_name}` ({columns_str})\nVALUES\n\t{values_str};"

    return query


def validate_sql_config(config):
    if config['table_name'] is None or config['table_name'].strip() == "":
        print("table_name is missing in config")
        raise ValueError("table_name is missing in config")

    if config['columns'] is None or len(config['table_name']) == 0:
        print("Columns names are missing in config")
        raise ValueError("Columns names are missing in config")

    if config['values'] is None or len(config['table_name'].strip()) == 0:
        print("Columns value are missing in config")
        raise ValueError("Columns value are missing in config")

    if len(config['columns']) != len(config['values']):
        print("Size of Column and Value list should be same.")
        raise ValueError("Size of Column and Value list should be same.")
