# Dados e funções dos rolos
def cadastrar_rolo(rolos):
    # Pede ao usuário os dados do rolo
    # .strip() tira espaços sobrando; .upper() deixa o material em maiúsculas
    material = input("Material (PLA, PETG...): ").strip().upper()
    cor = input("Cor: ").strip()
    preço = float(input("Preço pago (R$): "))
    peso = float(input("Peso inicial (g): "))

    # Monta o dicionário do rolo, com um campo nomeado para cada informação
    rolo = {
        "id": len(rolos) + 1,       # número do rolo (1, 2, 3...)
        "material": material,
        "cor": cor,
        "preço": preço,
        "peso_inicial": peso,       # usado depois para calcular o preço por grama
        "gramas_restantes": peso,   # começa cheio e vai diminuindo a cada impressão
    }

    # Adiciona o rolo ao final da lista
    rolos.append(rolo)
    print(f"Rolo {rolo['id']} cadastrado!")

def listar_estoque(rolos):
    # Se a lista estiver vazia, avisa e sai da função
    if not rolos:
        print("Nenhum rolo cadastrado.")
        return

     # Percorre a lista e mostra uma linha por rolo
    for r in rolos:
        print(f"[{r['id']}] {r['material']} {r['cor']} - "
              f"{r['gramas_restantes']:.0f} g restantes")
        
# Menu
def menu():
    # Lista que guarda todos os rolos cadastrados (cada rolo é um dicionário)
    rolos = []

    while True:
        print("\n----- Seja Bem-Vindo ao CODY -----")
        print("Seu assistente do Laboratório de Impressão 3D\n")

        print("1. Verificar Estoque")
        print("2. Cadastrar novo Material")
        print("3. Criar Pedido")
        print("4. Explicação do Cody")
        print("5. Sair do Programa")

        opcao = input("\nEscolha um número (1-5): ")

        if not opcao.isdigit():
            print("\nDigite apenas números!")
            continue

        opcao = int(opcao)

        match opcao:

            case 1:
                print("\nOpa chefe! Vamos verificar seu estoque!")

            case 2:
                print("\nCadastro de novo material")

            case 3:
                print("\nVamos criar um pedido!")

            case 4:
                print("\nOlá! Eu sou o CODY, seu assistente de laboratório.")

            case 5:
                print("\nEncerrando o CODY. Até logo!")
                break

            case _:
                print("\nEscolha um número de 1 a 5.")


menu()

#aaaaaaaaaaa
print('ISRAEL')