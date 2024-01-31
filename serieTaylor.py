import math

PI = 3.141593


def convert_to_rad(angle):
    return angle * PI / 180


class SerieTaylor:
    def __init__(self, angle, n):
        self.angle = angle
        self.n = n

    def calculate_sin(self):
        angle_rad = convert_to_rad(self.angle)

        sin_angle = 0

        for n in range(self.n + 1):
            term = ((-1) ** n) * (angle_rad ** (2 * n + 1)) / math.factorial(2 * n + 1)
            sin_angle += term

        return sin_angle

    def calculate_cos(self):
        angle_rad = convert_to_rad(self.angle)

        cos_angle = 0

        for n in range(self.n + 1):
            term = ((-1) ** n) * (angle_rad ** (2 * n)) / math.factorial(2 * n)
            cos_angle += term

        return cos_angle

    def calculate_hyperbolic_sin(self):
        angle_rad = convert_to_rad(self.angle)

        sinh_angle = 0

        for n in range(self.n + 1):
            term = (angle_rad ** (2 * n + 1)) / math.factorial(2 * n + 1)
            sinh_angle += term

        return sinh_angle

    def calculate_hyperbolic_cos(self):
        angle_rad = convert_to_rad(self.angle)

        cosh_angle = 0

        for n in range(self.n + 1):
            term = (angle_rad ** (2 * n)) / math.factorial(2 * n)
            cosh_angle += term

        return cosh_angle


def executa_serie():
    try:
        angle = float(input("Insira o ângulo, em graus: "))
        n = int(input("Insira o valor de n para a série de Taylor que deseja executar: "))

        serie = SerieTaylor(angle, n)

        print("\nEscolha a operação:")
        print("1. Calcular seno")
        print("2. Calcular cosseno")
        print("3. Calcular seno hiperbólico")
        print("4. Calcular cosseno hiperbólico")

        escolha = int(input("Digite o número da operação desejada: "))

        if escolha == 1:
            resultado = serie.calculate_sin()
            print(f"O seno do ângulo {angle} é aproximadamente {resultado}")
        elif escolha == 2:
            resultado = serie.calculate_cos()
            print(f"O cosseno do ângulo {angle} é aproximadamente {resultado}")
        elif escolha == 3:
            resultado = serie.calculate_hyperbolic_sin()
            print(f"O seno hiperbólico do ângulo {angle} é aproximadamente {resultado}")
        elif escolha == 4:
            resultado = serie.calculate_hyperbolic_cos()
            print(f"O cosseno hiperbólico do ângulo {angle} é aproximadamente {resultado}")
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")

    except ValueError as e:
        print(f"Erro: {e}. Certifique-se de inserir valores numéricos.")


if __name__ == "__main__":
    executa_serie()
