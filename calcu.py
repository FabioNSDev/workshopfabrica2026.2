def calculadora():
    while True:
        try:
            numero_1 = input("Digite o primeiro número: ")
            numero_2 = input("Digite o segundo número: ")

            numero_1 = float(numero_1)
            numero_2 = float(numero_2)

            operacao = input("Digite o valor da função (+, -, *, /): ")

            if operacao == "+":
                print(f"O soma de {numero_1} e {numero_2} será = {numero_1 + numero_2}")

            elif operacao == "-":
                print(f"A subtração de {numero_1} e {numero_2} será = {numero_1 - numero_2}")
            elif operacao == "*":
                print(f"A multiplicação de {numero_1} e {numero_2} será = {numero_1 * numero_2}")
            elif operacao == "/":
                print(f"A divisão de {numero_1} e {numero_2} será = {numero_1 / numero_2}")
            else:
                print("Operação inválida:")
                continue

            continuar = input("Deseja continuar? (s/n)")

            if continuar.lower() != "s":
                break

        except ValueError:
            print("Digite apenas valores válidos!")

        except ZeroDivisionError:
            print("Divisão por zero!")

calculadora()