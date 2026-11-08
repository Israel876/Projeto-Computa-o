
def menu():
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

#vamo ver se o cody vai funcionar 
