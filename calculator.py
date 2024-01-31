from math import sqrt


class Calculator:
    def __init__(self, value):
        self.value = value

    def sum(self, another_value):
        return self.value + another_value

    def subtract(self, another_value):
        return self.value - another_value

    def multiplication(self, another_value):
        return self.value * another_value

    def division(self, another_value):
        if another_value != 0:
            return self.value / another_value
        else:
            raise ValueError(f"O número inserido {another_value} é inválido pois sua divisão resultaria em uma "
                             f"indeterminação.")

    def square_root(self):
        if self.value >= 0:
            return sqrt(self.value)
        else:
            raise ValueError(f"O número inserido {self.value} é inválido por ser negativo.")


try:
    while True:
        value = input("Insira um número: ")
        if value.isdigit():
            value = float(value)
        else:
            print("Por favor, insira um número.")
            continue

        calculator = Calculator(value)

        print("Escolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Raiz Quadrada")
        print("6 - Sair")

        choice = int(input("Digite o número da operação desejada: "))

        if choice == 1:
            another_value = float(input("Insira o valor para somar: "))
            result = calculator.sum(another_value)
            print(f"A soma de {value} e {another_value} é {result}")
        elif choice == 2:
            another_value = float(input("Insira o valor para subtrair: "))
            result = calculator.subtract(another_value)
            print(f"A subtração de {value} por {another_value} é {result}")
        elif choice == 3:
            another_value = float(input("Insira o valor para multiplicar: "))
            result = calculator.multiplication(another_value)
            print(f"A multiplicação de {value} por {another_value} é {result}")
        elif choice == 4:
            another_value = float(input("Insira o valor para dividir: "))
            result = calculator.division(another_value)
            print(f"A divisão de {value} por {another_value} é {result}")
        elif choice == 5:
            result = calculator.square_root()
            print(f"A raiz quadrada de {value} é {result}")
        elif choice == 6:
            print("Operação encerrada.")
            break
        else:
            print("Opção inválida")

except ValueError as e:
    print(e)
