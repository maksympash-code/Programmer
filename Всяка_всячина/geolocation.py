from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="user")

location = geolocator.geocode("Кам'янець-Подільський, Фортеця")

print(location.latitude, location.longitude)