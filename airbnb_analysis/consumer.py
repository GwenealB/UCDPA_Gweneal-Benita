import pandas, requests, sqlite3


consumer_data_folder = 'data/'
class CSV:
  AB_NYC_2019 = lambda: consumer_data_folder + 'AB_NYC_2019.csv'
  AB_NYC_2020 = lambda: consumer_data_folder + 'AB_NYC_2020.csv'
  AB_NYC_2021 = lambda: consumer_data_folder + 'AB_NYC_2021.csv'
  @staticmethod
  def consume(file:str):
    return pandas.read_csv(file)

class JSON:
  @staticmethod
  def consume(file:str):
    return pandas.read_json(file)

class JSONApi:
  # Example of how one would consume data provided from a JSON API
  url = 'https://raw.githubusercontent.com/GwenealB/airbnb_analysis_project/main/data/AB_NYC_2019.json'

  @staticmethod
  def consume(url):
    # Initialize data with empty data, in case of request failure
    data = None
    req = requests.get(url=url)
    if(req.status_code == 200):
      data = JSON(req.text)
    else:
      print('Something bad happened!')
    return data


class SQLite:
  DATABASE_LOCATION = 'database/sqlite.db'
  AB_NYC_2019 = 'AB_NYC_2019'
  AB_NYC_2020 = 'AB_NYC_2020'
  AB_NYC_2021 = 'AB_NYC_2021'
  @staticmethod
  def consume(table_name:str):
    conn = sqlite3.connect(SQLite.DATABASE_LOCATION)
    data = pandas.read_sql_query(f'SELECT * FROM {table_name}', conn)
    conn.close()
    return data
