import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import certifi
import ssl

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="climate change app", scheme='http')
# INPUT latitude/long
location = geolocator.reverse("-37.817403,144.956776")
print (location.raw['address']['postcode'])
