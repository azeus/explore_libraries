from geopy.geocoders import Nominatim
import argparse

def get_coordinates(city):
   geolocator = Nominatim(user_agent="my_app")
   location = geolocator.geocode(city)
   return (location.latitude, location.longitude)

def main():
   parser = argparse.ArgumentParser(description='Get coordinates for a city')
   parser.add_argument('city', help='Name of the city')
   args = parser.parse_args()
   print(get_coordinates(args.city))

if __name__ == "__main__":
   main()

