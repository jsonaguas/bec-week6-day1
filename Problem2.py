#Task 1:
''' 
python3 -m venv venv
source venv/bin/activate
pip install requests
'''
import requests
#Task 2:
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    if response.status_code == 200:
        planets_data = response.json()['bodies']
        planets = []
        for planet in planets_data:
            if planet['isPlanet'] and 'mass' in planet and planet['mass'] is not None:
                name = planet['englishName']
                mass = planet['mass']['massValue'] * (10 ** planet['mass']['massExponent'])
                orbit_period = planet['sideralOrbit']
                planets.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})
                print(f"Planet: {name}, Mass: {mass} kg, Orbit Period: {orbit_period} days")
        return planets
    else:
        print("Failed to fetch data")
        return []

#Task 3:
def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda x: x['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']

planets = fetch_planet_data()
if planets:
    name, mass = find_heaviest_planet(planets)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")