import requests
import pprint

pp = pprint.PrettyPrinter(indent=2)
url = "https://pokeapi.co/api/v2/pokemon/bulbasaur"
r = requests.get(url)
pp.pprint(r.json())