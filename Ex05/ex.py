import csv

class Agenda:
    def __init__(self):
        self.contatos = {}
        self.carregar_contatos()

    def grava(self, nome, telefone, tipo_telefone='celular', email='', aniversario=''):
        if nome in self.contatos:
            print(f"Erro: O contato '{nome}' já existe na agenda.")
            return False
        self.contatos[nome] = {'telefone': telefone, 'tipo_telefone': tipo_telefone, 'email': email, 'aniversario': aniversario}
        self.salvar_contatos()
        return True
    
    def apaga(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            self.salvar_contatos()
            return True
        else:
            print(f"Erro: O contato '{nome}' não encontrado.")
            return False
    
    def altera(self, nome, telefone=None, tipo_telefone=None, email=None, aniversario=None):
        if nome in self.contatos:
            if telefone is not None:
                self.contatos[nome]['telefone'] = telefone
            if tipo_telefone is not None:
                self.contatos[nome]['tipo_telefone'] = tipo_telefone
            if email is not None:
                self.contatos[nome]['email'] = email
            if aniversario is not None:
                self.contatos[nome]['aniversario'] = aniversario
            self.salvar_contatos()
            return True
        else:
            print(f"Erro: O contato '{nome}' não encontrado.")
            return False
    
    def salvar_contatos(self):
        with open('contatos.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Telefone', 'Tipo Telefone', 'Email', 'Aniversário'])
            for nome, info in self.contatos.items():
                writer.writerow([nome, info['telefone'], info['tipo_telefone'], info['email'], info['aniversario']])

    def carregar_contatos(self):
        try:
            with open('contatos.csv', mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.contatos[row['Nome']] = {
                        'telefone': row['Telefone'],
                        'tipo_telefone': row['Tipo Telefone'],
                        'email': row['Email'],
                        'aniversario': row['Aniversário']
                    }
        except FileNotFoundError:
            print("Nenhum arquivo de contatos encontrado. Iniciando uma agenda nova.")

    def lista_nomes(self):
        for i, nome in enumerate(sorted(self.contatos.keys()), start=1):
            print(f"{i}. {nome} - {self.contatos[nome]}")

    def busca(self, nome):
        if nome in self.contatos:
            print(f"{nome}: {self.contatos[nome]}")
        else:
            print(f"Erro: O contato '{nome}' não encontrado.")

    def menu(self):
        while True:
            print("\nAgenda - Escolha uma opção:")
            print("1. Adicionar contato")
            print("2. Apagar contato")
            print("3. Alterar contato")
            print("4. Listar contatos")
            print("5. Buscar contato")
            print("6. Sair")
            escolha = input("Opção: ")
            if escolha == '1':
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                tipo_telefone = input("Tipo de Telefone (celular, fixo, residência, trabalho): ")
                email = input("Email: ")
                aniversario = input("Aniversário (dd/mm/aaaa): ")
                self.grava(nome, telefone, tipo_telefone, email, aniversario)
            elif escolha == '2':
                nome = input("Nome do contato a apagar: ")
                self.apaga(nome)
            elif escolha == '3':
                nome = input("Nome do contato a alterar: ")
                telefone = input("Novo Telefone (deixe em branco para não alterar): ")
                tipo_telefone = input("Novo Tipo de Telefone (deixe em branco para não alterar): ")
                email = input("Novo Email (deixe em branco para não alterar): ")
                aniversario = input("Novo Aniversário (deixe em branco para não alterar): ")
                self.altera(nome, telefone if telefone else None, tipo_telefone if tipo_telefone else None, email if email else None, aniversario if aniversario else None)
            elif escolha == '4':
                self.lista_nomes()
            elif escolha == '5':
                nome = input("Nome do contato a buscar: ")
                self.busca(nome)
            elif escolha == '6':
                print("Saindo da agenda.")
                break
            else:
                print("Opção inválida.")