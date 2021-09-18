import pandas
__folder = 'data/'
AB_NYC_2019 = __folder + 'AB_NYC_2019.csv'
AB_NYC_2020 = __folder + 'AB_NYC_2020.csv'
AB_NYC_2021 = __folder + 'AB_NYC_2021.csv'
def consume(file:str):
  return pandas.read_csv(file)
