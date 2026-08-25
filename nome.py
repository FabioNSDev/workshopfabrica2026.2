import requests

while True:
    def buscar_idade(nome):
        url = f"https://api.agify.io/?name={nome}"
        resposta = requests.get(url)

        if resposta.status_code != 200:
            return None

        return resposta.json()

    nome = input("Digite um nome: ")

    if nome.isalpha():
        dados = buscar_idade(nome)
    else:
        print("Digite um Nome Válido")  
        dados = buscar_idade(nome)

    if dados is not None:
        print(f"Nome: {dados['name']}")
        print(f"Idade estimada: {dados['age']}")
        print(f"Quantidade: {dados['count']}")

        sair = input("Deseja buscar outro nome? (s/n): ").strip().lower()
        if sair != "s":
            print("Programa encerrado.")
            break
    else:
        print("Não foi possivel buscar")
    