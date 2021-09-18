import pandas, sqlite3

__folder = ''
AB_NYC_2019 = __folder + 'AB_NYC_2019'
AB_NYC_2020 = __folder + 'AB_NYC_2020'
AB_NYC_2021 = __folder + 'AB_NYC_2021'


def consume(table_name:str):
  conn = sqlite3.connect('database/sqlite.db')
  data = pandas.read_sql_query(f'SELECT * FROM {table_name}', conn)
  conn.close()
  return data