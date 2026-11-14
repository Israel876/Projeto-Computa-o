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

# Orçamento
def perguntar_número(texto, atual=None):    # Ex: Preço do kWh (R$)
    # Pergunta um número ao usuário.
    # Se já existe um valor atual, mostra entre colchetes e, se o usuário
    # só apertar Enter, mantém esse valor.
    if atual is None:
        resposta = input(f"{texto}: ").strip()
    else:
        resposta = input(f"{texto} [atual: {atual}]: ").strip()
        if resposta == "":
            return atual

    # Troca vírgula por ponto, porque no Brasil se digita 0,85 e o float() só entende 0.85
    return float(resposta.replace(",", "."))

def pedir_configurações(configurações):
    # .get() devolve None se a chave ainda não existe (primeira vez),
    # e devolve o valor guardado se já existe.
    # A função altera o dicionário que recebeu, sem precisar de return.
    configurações["potência_w"] = perguntar_número(
        "Potência da impressora (W)", configurações.get("potência_w"))
    configurações["preço_kwh"] = perguntar_número(
        "Preço do kWh (R$)", configurações.get("preço_kwh"))
    configurações["margem_percentual"] = perguntar_número(
        "Margem de lucro (%)", configurações.get("margem_percentual"))

def calcular_custo_filamento(rolo, gramas):
    # Primeiro acha quanto custa 1 grama deste rolo, depois multiplica pelas gramas da peça
    preço_por_grama = rolo["preço"] / rolo["peso_inicial"]
    return preço_por_grama * gramas

def calcular_custo_energia(horas, potência_w, preço_kwh):
    # Converte watts para quilowatts (o preço da conta de luz é por kWh)
    potência_kw = potência_w / 1000
    return potência_kw * horas * preço_kwh

def calcular_preço_final(filamento, energia, margem_percentual):
    # Converte a porcentagem digitada (20) para fração (0.20) e aplica sobre o custo total
    margem = margem_percentual / 100
    return (filamento + energia) * (1 + margem)
    
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
                listar_estoque(rolos)    # mostra os rolos cadastrados

            case 2:
                print("\nCadastro de novo material")
                cadastrar_rolo(rolos)   # pede os dados e adiciona o rolo à lista

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
