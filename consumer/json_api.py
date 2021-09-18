# Example of how one would consume data provided from a JSON API

import requests

from .json import consume as t_consume
url = 'https://raw.githubusercontent.com/GwenealB/airbnb_analysis_project/main/data/AB_NYC_2019.json'

def consume(url):
  # Initialize data with empty data, in case of request failure
  data = None
  req = requests.get(url=url)
  if(req.status_code == 200):
    data = t_consume(req.text)
  else:
    print('Something bad happened!')
  return data