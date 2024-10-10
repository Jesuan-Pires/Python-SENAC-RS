lista = []

def adiciona_pessoa(nome, altura):
    dict_valores={
    "nome":nome,
    "altura":altura
    }
    lista.append(dict_valores)

while True:
        nome=input("Entre com o nome: ")
        altura=input("Entre com a altura: ")
        adiciona_pessoa(nome, altura)
        
        opcao=input("Deseja adicionar outra pessoa? [s/n]")
        if opcao == "n":
            if lista:    
                maior = lista[0]
                menor = lista[0]
                
                for pessoa in lista:
                    if pessoa["altura"] > maior["altura"]:
                        maior=pessoa
                    if pessoa['altura'] < maior["altura"]:
                        menor=pessoa
                        
                print(f"Maior pessoa: {maior['nome']} com altura {maior['altura']}")
                print(f"Menor pessoa: {menor['nome']} com altura {menor['altura']}")
            else:
                print("Nenhuma pessoa foi adicionada.")
            break
        