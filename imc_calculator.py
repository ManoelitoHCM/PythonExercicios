from math import pow


class IMCCalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_imc(self):
        if self.weight > 0 and self.height > 0:
            return round(self.weight / (pow(self.height, 2)), 3)
        else:
            raise ValueError(f"Um dos valores para altura ou peso inseridos é inválido por ser zero ou inferior.")


try:

    while True:
        weight = input("Insira seu peso, em kg: ")
        if weight.isdigit():
            weight = float(weight)
        else:
            print("Por favor, insira seu peso em kg: ")
            continue

        height = input("Insira sua altura, em cm: ")
        if height.isdigit():
            height = float(height) / 100
        else:
            print("Por favor, insira sua altura em cm: ")
            continue
        break

    calculator = IMCCalculator(weight, height)

    imc = calculator.calculate_imc()

    if imc < 18.5:
        print(f"Seu IMC é inferior a 18.5 e você é classificado(a) como abaixo do peso.")
    elif 18.5 <= imc < 25.0:
        print(f"Seu IMC é igual a {imc} e você é classificado(a) como saudável.")
    elif 25.0 <= imc < 30.0:
        print(f"Seu IMC é igual a {imc} e você é classificado(a) com peso em excesso.")
    elif 30.0 <= imc < 35.0:
        print(f"Seu IMC é igual a {imc} e você é classificado(a) com obesidade grau I.")
    elif 35.0 <= imc < 40.0:
        print(f"Seu IMC é igual a {imc} e você é classificado(a) com obesidade grau II (severa).")
    elif imc >= 40.0:
        print(f"Seu IMC é igual a {imc} e você é classificado(a) com obesidade grau III (mórbida).")

except ValueError as e:
    print(e)
