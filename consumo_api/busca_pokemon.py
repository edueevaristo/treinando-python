import requests
import json
# import pip
# replace requests with the name of module you want to install
# pip.main(['install', 'requests'])


def busca_pokemon(pokemon):
    print("Buscando dados...")
    response = requests.get(
        "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon))
    if response.status_code == 200:
        response_pokemon = response.json()
        return response_pokemon
    else:
        raise Exception("Não foi possível encontrar o endereço.")


pokemon = input("Qual seria o Pokemon desejado? \n")

poke = busca_pokemon(pokemon)
print(poke)
