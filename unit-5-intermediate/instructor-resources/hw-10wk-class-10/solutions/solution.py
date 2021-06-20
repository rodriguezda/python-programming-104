import requests
import geocoder

# All capital letters is the convention for a constant - a variable that never changes.
API_BASE_URL = "https://api.darksky.net/forecast/60bb82076d33e48d2cb2480bd4a8f897/"

destinations = ["The Space Needle",
    "Crater Lake",
    "The Golden Gate Bridge",
    "Yosemite National Park",
    "Las Vegas, Nevada",
    "Grand Canyon National Park",
    "Aspen, Colorado",
    "Mount Rushmore",
    "Yellowstone National Park",
    "Sandpoint, Idaho",
    "Banff National Park",
    "Capilano Suspension Bridge"]

for point in destinations:
    # Get the latitude and longitude from `geocoder`.
    loc = geocoder.arcgis(point)

    # Print out `geopy`'s results.
    print("{0} is located at ({1:.4f}, {2: .4f})".format(point, loc.latlng[0], loc.latlng[1]))

    # Construct the full API URL (format not necessary, but makes it easier!).
    full_api_url = "{0}{1},{2}".format(API_BASE_URL, loc.latlng[0], loc.latlng[1])

    # Call the Dark Sky API.
    result = requests.request('GET', full_api_url).json()

    # Print out the Dark Sky results in a readable way.
    print("At {0} right now, it's {1} with a temperature of {2}\n".format(point, result["currently"]["summary"], result["currently"]["temperature"]))
