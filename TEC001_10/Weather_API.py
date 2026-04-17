import requests

url1 ="http://api.openweathermap.org/geo/1.0/direct?q=Hanoi&appid=7420f93521126924f8c8e56284af3d52" 
response1 = requests.get(url1).json()
lat = response1[0]['lat']
lon = response1[0]['lon']
url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=7420f93521126924f8c8e56284af3d52"
response2 = requests.get(url2).json()
print(f"Temperature in Hanoi: {response2['main']['temp']}K or {response2['main']['temp'] - 273.15:.2f}°C")
