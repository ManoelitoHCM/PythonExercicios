class Agenda:
    def __init__(self):
        self.contatos = {}

    def verificar_vazio(self):
        return not self.contatos

    def adicionar_contato(self):
        nome = input("Insira o nome do contato: ")
        telefone = input("Insira o número de telefone do contato: ")

        if not nome or not telefone.isnumeric():
            print("Erro: Entrada não pode ser vazia.")
            return

        self.contatos[nome] = int(telefone)
        print(f"Contato {nome}: {telefone} adicionado com sucesso.")

    def apagar_contato(self):
        if self.verificar_vazio():
            print("Agenda vazia.")
            return

        nome = input("Digite o nome do contato que você deseja apagar: ")
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato de {nome} removido com sucesso.")
        else:
            print("Erro: Contato não encontrado.")

    def exibir_contato(self):
        if self.verificar_vazio():
            print("Agenda vazia.")
            return

        nome = input("Digite o nome do contato que você deseja exibir: ")
        telefone = self.contatos.get(nome, "Contato não encontrado.")
        print(f"{nome}: {telefone}")

    def atualizar_contato(self):
        if self.verificar_vazio():
            print("Agenda vazia.")
            return

        nome = input("Digite o nome do contato que você deseja atualizar: ")
        telefone = input("Digite o novo número para este contato: ")

        if nome in self.contatos:
            print(f"Contato atualizado com sucesso para {nome}: {telefone}.")
            self.contatos[nome] = int(telefone)
        else:
            print("Erro: Contato não encontrado.")

    def listar_todos_contatos(self):
        if self.verificar_vazio():
            print("Agenda vazia.")
            return

        for nome, telefone in self.contatos.items():
            print(f"{nome}: {telefone}")

    def executar_agenda(self):
        try:
            while True:
                print("Esta é uma agenda simples. Selecione uma das opções abaixo para realizar uma operação.")
                print("1 - Adicionar contato")
                print("2 - Apagar contato")
                print("3 - Exibir contato")
                print("4 - Atualizar contato")
                print("5 - Listar todos os contatos")
                print("6 - Sair")

                choice = input("Escolha uma opção 1-5: ")

                if choice.isdigit():
                    choice = int(choice)
                else:
                    print("Digite uma opção válida")
                    continue

                if choice == 1:
                    self.adicionar_contato()
                elif choice == 2:
                    self.apagar_contato()
                elif choice == 3:
                    self.exibir_contato()
                elif choice == 4:
                    self.atualizar_contato()
                elif choice == 5:
                    self.listar_todos_contatos()
                elif choice == 6:
                    print("Programa encerrado.")
                    break
                else:
                    print("Opção inválida")

        except ValueError as e:
            print(e)


minha_agenda = Agenda()
minha_agenda.executar_agenda()
