import requests
import json
import pandas as pd


def get_postcodes1(lat, lon):
    #print(lat, lon)
    if lat is not None and lon is not None:  
        url = f"https://api.postcodes.io/postcodes?lat={lat}&lon={lon}"
        response = requests.get(url)
 
        try:
            data = response.json()
            if data['status'] == 200 and data['result']:
                min_distance = float('inf')
                closest_postcode = None

                for result in data['result']:
                    if result['distance'] < min_distance:
                        min_distance = result['distance']
                        closest_postcode = result['postcode']

                return closest_postcode
            else:
                print("No results found")
                return None
        except ValueError:
            print("Error parsing JSON")
            return None
        except KeyError:
            print("Unexpected JSON structure")
            return None
    else:
        print("Latitude and longitude must not be None")
        return None