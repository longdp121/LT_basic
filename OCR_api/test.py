import requests
import datetime as dt

today = dt.date.today().strftime('%Y-%m-%d')
print(type(today))

url = "https://covid-19-data.p.rapidapi.com/report/country/name"

#querystring = {"name":"Italy","date":f'{today}'}
querystring = {"name":"Italy","date":today}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "0f7f236931mshf02b49bcf045a08p1bde7cjsn2776b52e51b8"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)