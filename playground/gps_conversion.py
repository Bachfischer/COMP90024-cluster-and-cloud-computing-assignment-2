import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import certifi
import ssl

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="climate change app", scheme='http')

# returns the postcode for the given longititude and latitude
def get_postcode(long, lat):
    gps_string = long + "," + lat
    location = geolocator.reverse(gps_string)
    return location.raw['address']['postcode']
