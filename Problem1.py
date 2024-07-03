#Task 1:
''' 
python3 -m venv venv
source venv/bin/activate
pip install requests
'''

# Task 2: 
import requests

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        print(f"Name: {name}, Abilities: {abilities}")
    else:
        print(f"Failed to fetch data for {pokemon_name}")

fetch_pokemon_data("pikachu")

# Task 3:
def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if response.status_code == 200:
            data = response.json()
            total_weight += data['weight']
        else:
            print(f"Failed to fetch data for {pokemon}")
            return None
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
for pokemon_name in pokemon_names:
    fetch_pokemon_data(pokemon_name)

average_weight = calculate_average_weight(pokemon_names)
print(f"Average Weight: {average_weight}")