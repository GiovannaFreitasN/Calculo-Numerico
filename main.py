def menu():
    while True:
        print("1. metodo da bisseção")
        print("2. metodo da falsa posição")
        print("3. metodo de Newton")
        print("4. metodo da secante")
        print("5. metodo de ponto fixo")
        print("6. metodo de Newton-Raphson")

        opcao = input("Escolha uma opção (1-6) ou 'sair' para encerrar: ")
        if opcao == '1':
            from bissecao import bissecao
            bissecao()
        elif opcao == '2':
            from falsa_posicao import falsa_posicao
            falsa_posicao()
        elif opcao == '3':
            from newton import newton
            newton()
        elif opcao == '4':
            from secante import secante
            secante()
        elif opcao == '5':
            from ponto_fixo import ponto_fixo
            ponto_fixo()
        elif opcao == '6':
            from newton_raphson import newton_raphson
            newton_raphson()
        elif opcao.lower() == 'sair':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    menu()
    # O código abaixo é para evitar que o terminal feche imediatamente após a execução
    input("Pressione Enter para sair...")
