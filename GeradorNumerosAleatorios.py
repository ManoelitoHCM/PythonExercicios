import random


class AdivinhadorNumero:
    def __init__(self):
        self.numero_aleatorio = random.randint(1, 1000)

    def adivinhar(self, guess):
        if 1 <= guess <= 1000:
            if self.numero_aleatorio == guess:
                return "Parabéns, você acertou!"
            elif self.numero_aleatorio < guess:
                return "O número é menor do que seu palpite."
            elif self.numero_aleatorio > guess:
                return "O número é maior do que seu palpite."
        else:
            raise ValueError("O palpite inserido está fora do intervalo! Insira um número válido.")


try:
    adivinhador = AdivinhadorNumero()

    count = 0

    while True:
        guess = int(input(
            "Foi gerado um número inteiro de 1 a 1000 pela máquina. Insira um palpite para tentar adivinhar. Caso "
            "deseje sair, digite -1: "))

        if guess == -1:
            break

        resultado = adivinhador.adivinhar(guess)
        print(resultado)

        count += 1

        if "Parabéns" in resultado:
            print(f"Você adivinhou o número em {count} tentativas.")
            break

except ValueError as e:
    print(e)
