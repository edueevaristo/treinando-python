import requests
# import pip
# # replace requests with the name of module you want to install
# pip.main(['install', 'requests'])


def busca_endereco(cep):
    print("Buscando dados...")
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        endereco = response.json()
        return endereco
    else:
        raise Exception("Não foi possível encontrar o endereço.")


cep = input("Qual seria o seu CEP ? \n")
cepInt = int(cep)

endereco = busca_endereco(cep)
print(endereco)
