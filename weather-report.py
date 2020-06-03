import requests
import time
city = input("Enter city name: ")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=" + city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + url3
response = requests.get(url)
jsondata = response.json()
print (jsondata['main']['temp'])
print(jsondata['main']['humidity'])
print (jsondata['wind']['speed'])
print(jsondata['coord']['lat'])
print(jsondata['coord']['lon'])
print(time.ctime(jsondata['sys']['sunrise']))
print(time.ctime(jsondata['sys']['sunset']))
# Reading the JSON Data
print (jsondata)
for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
