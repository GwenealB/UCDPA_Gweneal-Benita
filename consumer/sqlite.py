import pandas, sqlite3

conn = sqlite3.connect('database/sqlite.db')
table_name = 'AB_NYC_2019'
data = pandas.read_sql_query(f'SELECT * FROM {table_name}', conn)

