import requests
from datetime import datetime

s_city = "Bryansk,RU"
city_id = 571476
appid = "480894262782f3b3d51aa1235d08c9bf"
lon = 34.380562
lat = 53.287498
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/onecall",
                       params={'lat': lat, 'lon': lon, 'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    max_pressure = ['',0]
    max_difference = ['', 0]
    for _,i in zip(range(5), data['daily']):
        if i['pressure'] > max_pressure[1]:
            max_pressure = [i['dt'], i['pressure']]
        current = abs(i['temp']['night'] - i['temp']['morn'])
        if current > max_difference[1]:
            max_difference = [i['dt'], current]

    print(f'Максимальное давление за предстоящие 5 дней: {int(max_pressure[1]*0.75006375541921)} mmHg, дата: {datetime.fromtimestamp(max_pressure[0])}')
    print(f'День с минимальной разницей между ночной и утренней температурой: {datetime.fromtimestamp(max_difference[0])}, разница:{max_difference[1]} °C')
except Exception as e:
    print("Exception (forecast):", e)
    pass
