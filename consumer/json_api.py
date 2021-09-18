# Example of how one would consume data provided from a JSON API

import requests
import pandas

url = 'https://raw.githubusercontent.com/GwenealB/airbnb_analysis_project/main/data/AB_NYC_2019.json'

# Initialize data with empty data, in case of request failure
data = pandas.DataFrame([])
req = requests.get(url=url)
if(req.status_code == 200):
  data = pandas.read_json(req.text)
else:
  print('Something bad happened!')