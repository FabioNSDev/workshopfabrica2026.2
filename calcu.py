
def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def calculadora():
    while True:
        try:
            menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                print("Programa encerrado.")
                break

            numero_1 = float(input("Digite o primeiro número: "))
            numero_2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = somar(numero_1, numero_2)
                print(f"Resultado: {numero_1} + {numero_2} = {resultado}")
            elif opcao == "2":
                resultado = subtrair(numero_1, numero_2)
                print(f"Resultado: {numero_1} - {numero_2} = {resultado}")
            elif opcao == "3":
                resultado = multiplicar(numero_1, numero_2)
                print(f"Resultado: {numero_1} * {numero_2} = {resultado}")
            elif opcao == "4":
                resultado = dividir(numero_1, numero_2)
                print(f"Resultado: {numero_1} / {numero_2} = {resultado}")
            else:
                print("Opção inválida!")
                continue

        except ValueError:
            print("Erro: digite apenas números válidos.")
        except ZeroDivisionError:
            print("Erro: divisão por zero.")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Programa encerrado.")
            break

calculadora()