# Try Except

try:
    a = int(input("Digite o Dividendo: "))
    c = int(input("Digite o Divisor: "))
    resultado = a / c
except ValueError:
    print("Você não digitou um número válido!")
except ZeroDivisionError:
    print("Impossivel dividir por 0 ")
else:
    print("Nenhum erro.")
finally:
    print("Este Bloco sempre será executado.")



