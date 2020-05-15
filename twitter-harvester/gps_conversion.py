import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import certifi
import ssl

# creates a geolocator object
def create_geolocator():
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    geolocator = Nominatim(user_agent="climate change app", scheme='http')
    return geolocator

# returns the postcode for the given longititude and latitude
def get_postcode(long, lat):
    geolocator = create_geolocator()
    gps_string = long + "," + lat
    location = geolocator.reverse(gps_string)
    return location.raw['address']['postcode']
