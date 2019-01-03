import requests
import pprint

pp = pprint.PrettyPrinter(indent=2)
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
r = requests.get(url)
pp.pprint(r.json())