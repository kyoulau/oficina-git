# Pede ao usuário para inserir os números e o operador
num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Verifica qual operador foi escolhido e realiza o cálculo
if operador == '+':
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif operador == '-':
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif operador == '*':
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")

elif operador == '/':
    # Adiciona uma verificação para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro! Divisão por zero não é permitida.")

else:
    print("Operador inválido. Por favor, use um dos seguintes: +, -, *, /")