class Usuario:
    def _init_(self, nome, cpf, email, livros=None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.livros_emprestados = livros if livros is not None else []

class Bibliotecario:
    def _init_(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def adicionar_livro(self, livro):
        livro.num_exemplares += 1
        print(f'O livro {livro.titulo} foi adicionado ao estoque.')

    def emprestar_livro(self, usuario, livro):
        if livro.num_exemplares > livro.qtd_emprestado:
            usuario.livros_emprestados.append(livro)
            livro.qtd_emprestado += 1
            print(f'O livro {livro.titulo} foi emprestado para {usuario.nome}.')
        else:
            print('Desculpe, este livro não está disponível no momento.')

    def devolver_livro(self, usuario, livro):
        if livro in usuario.livros_emprestados:
            usuario.livros_emprestados.remove(livro)
            livro.qtd_emprestado -= 1
            print(f'O livro {livro.titulo} foi devolvido por {usuario.nome}.')
        else:
            print('Este livro não foi emprestado por você.')

    def menu(self, usuario, livro):
        while True:
            print("# MENU #"
                  "\n1 - Emprestar livro"
                  "\n2 - Devolver livro"
                  "\n3 - Adicionar livro ao estoque"
                  "\n4 - Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.emprestar_livro(usuario, livro)
            elif opcao == '2':
                self.devolver_livro(usuario, livro)
            elif opcao == '3':
                if isinstance(usuario, Bibliotecario):
                    self.adicionar_livro(livro)
                else:
                    print("Desculpe, apenas o bibliotecário pode adicionar livros ao estoque.")
            elif opcao == '4':
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

class Livro:
    def _init_(self, titulo, genero, autor, editora, num_exemplares, qtd_emprestado=0):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.editora = editora
        self.num_exemplares = num_exemplares
        self.qtd_emprestado = qtd_emprestado

nome = input('Digite seu nome ')
cpf = input('Digite seu CPF ')
email = input('Digite seu email ')
novo_usuario1 = Usuario(nome, cpf, email)

titulo = input('Digite o título do livro ')
genero = input('Digite o gênero do livro ')
autor = input('Digite o autor ')
editora = input('Digite a editora do livro ')
num_exemplares = int(input('Digite a quantidade de exemplares '))
novo_livro = Livro(titulo, genero, autor, editora, num_exemplares)

nome = input('Digite o nome do bibliotecario ')
cpf = input('Digite o cpf do bibliotecario ')
bibliotecario1 = Bibliotecario(nome, cpf)

bibliotecario1.menu(novo_usuario1, novo_livro)