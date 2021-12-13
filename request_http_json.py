import requests

def consulta():
    response = requests.get('http://')
    print(response.status_code)
    print(response.json())
    for pessoa in response.json():
        print(pessoa['id'], pessoa['nome'],pessoa['idade'])

def insere():
    nome = 'Rafael'
    idade = 31
    pessoa = {"nome":nome, "idade": idade}
    response = requests.post('http://', json=pessoa)
    print(response.status_code)
    print(response.json())

consulta()
#insere()
 