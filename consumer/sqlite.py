import pandas, sqlite3



def consume(table_name:str):
  conn = sqlite3.connect('database/sqlite.db')
  return pandas.read_sql_query(f'SELECT * FROM {table_name}', conn)