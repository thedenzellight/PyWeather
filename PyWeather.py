from calendar import formatstring
from aiohttp import request
from geopy.geocoders import Nominatim
import time
from datetime import datetime
import pyowm
import sys
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import formatting

findthename = input("Выберите название города на английском: ")


apikey = '7e5c2a051d8340c2cec76ffbc2b58f94'

owm = OWM(apikey)

mgr = owm.weather_manager()




timern = datetime.date(datetime.now()), datetime.date(datetime.now())


print("Starting at", datetime.date(datetime.now()), datetime.date(datetime.now()))

geolocator = Nominatim(user_agent="weather")
location = geolocator.geocode(findthename)
print("-------------------------------------------------")
print("N: ", location.latitude, "°", "E: ", location.longitude, "°")
print("-------------------------------------------------")
loclat = location.latitude
loclon = location.longitude
print("Sending request to api...")
time.sleep(1)
one_call = mgr.one_call(lat=loclat, lon=loclon)

print("Утром в", findthename, "Температура", one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None), 'C°')
print("Вечером в", findthename, "Температура", one_call.forecast_daily[0].temperature('celsius').get('eve', None), 'C°')
print("Ночью в", findthename, "Температура", one_call.forecast_daily[0].temperature('celsius').get('feels_like_night', None), 'C°')
print("Сейчас в", findthename, one_call.forecast_hourly[3].wind().get('speed', 0), 'км/ч ветра.')
print("Сейчас в", findthename, one_call.current.humidity, '% влажности.')

print(" ")
print("Ended at", datetime.date(datetime.now()), datetime.date(datetime.now()))

time.sleep(50)