# implementação de agenda usando lista encadeada e tabela hash
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.next = None


class Agenda:
    def __init__(self):
        self.head = None
        self.current = None
        self.tail = None

    def verificar_lista_vazia(self):
        return self.head is None

    def adicionar_contato(self):
        nome = input("Insira o nome do contato que deseja adicionar: ")
        telefone = input("Insira o número de telefone do contato: ")

        novo_contato = Contato(nome, telefone)

        # caso de a lista estar vazia
        if self.verificar_lista_vazia():
            self.head = novo_contato
            self.tail = novo_contato
            return

        # caso contrário, percorre a lista atribuindo
        # ao current a variável de cada nó, até que chegue ao fim da lista
        self.current = self.head
        while self.current.next is not None:
            self.current = self.current.next

        # no fim da lista, atribui o contato
        self.current.next = novo_contato
        self.tail = novo_contato

    def apagar_contato(self):
        if self.verificar_lista_vazia():
            print("Agenda vazia.")
            return

        nome = input("Insira o nome do contato que deseja deletar: ")

        # contato a excluir é o primeiro da lista
        if self.head.nome == nome:
            self.head = self.head.next
            print(f"Contato de {nome} excluído.")
            if self.verificar_lista_vazia():
                return

        self.current = self.head

        while self.current.next:
            # contato não está no início da lista
            if self.current.next.nome == nome:
                self.current.next = self.current.next.next
                print(f"Contato de {nome} excluído.")

                # contato era o último da lista
                if self.current.next is None:
                    self.tail = self.current
                return
            else:
                self.current = self.current.next
        print(f"Contato {nome} não encontrado na agenda.")

    def exibir_contato(self):
        if self.verificar_lista_vazia():
            print("Agenda vazia.")
            return

        nome = input("Insira o nome do contato que deseja exibir: ")

        self.current = self.head

        while self.current:
            # início da iteração que vai percorrer toda a lista
            if self.current.nome == nome:
                print(f"{nome}: {self.current.telefone}.")
                return
            else:
                self.current = self.current.next
        print(f"Contato {nome} não encontrado na agenda.")

    def atualizar_contato(self):
        if self.verificar_lista_vazia():
            print("Agenda vazia.")
            return

        nome = input("Insira o nome do contato que deseja atualizar: ")

        self.current = self.head

        while self.current:
            # início da iteração que vai percorrer toda a lista
            if self.current.nome == nome:
                self.current.telefone = input("Insira o novo número de telefone para este contato: ")
                print(f"{nome}: {self.current.telefone}.")
                return
            else:
                self.current = self.current.next
        print(f"Contato {nome} não encontrado na agenda.")

    def listar_todos_contatos(self):
        if self.verificar_lista_vazia():
            print("Agenda vazia.")
            return

        self.current = self.head

        while self.current:
            print(f"{self.current.nome}: {self.current.telefone}.")
            self.current = self.current.next

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
