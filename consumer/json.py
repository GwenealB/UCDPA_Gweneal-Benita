import pandas

def consume(file:str):
  return pandas.read_json(file)