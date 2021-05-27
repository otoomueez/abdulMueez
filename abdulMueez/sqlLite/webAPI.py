from pip._vendor import requests
response = requests.get("http://goweather.herokuapp.com/weather/accra")
# print(response.status_code)
data_json = response.json()
print("Today's temperature :", data_json['temperature'])
print("Tomorrow's temperature is ", data_json['forecast'][0]['temperature'])
