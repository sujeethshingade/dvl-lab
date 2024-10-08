import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

def get_lat_long(country_name):
    try:
        geolocator = Nominatim(user_agent="lat_long")
        location = geolocator.geocode(country_name)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return get_lat_long(country_name)
    except Exception as e:
        print(f"Error fetching data for {country_name}: {e}")
        return None, None

df = pd.read_csv('Countries-GDP.csv')

if 'Country Name' not in df.columns:
    raise ValueError("The CSV file must contain a 'Country Name' column.")

lat_long_list = []
for country in df['Country Name']:
    lat_long = get_lat_long(country)
    lat_long_list.append(lat_long)
    time.sleep(1)

df[['Latitude', 'Longitude']] = pd.DataFrame(lat_long_list)

df.to_csv('Updated_Countries-GDP.csv', index=False)

print(df)