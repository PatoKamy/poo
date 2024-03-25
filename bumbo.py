


























class Livro:
    def __init__(self, titulo, genero, editora, author, exemplares, qtd=0):
        self.titulo = titulo
        self.genero = genero
        self.editora = editora
        self.autor = author
        self.num_exemplares = exemplares
        self.qtd_emprestados = qtd

    def emprestar(self):
        if self.num_exemplares > self.qtd_emprestados:
            self.qtd_emprestados -= 1
            return True
        else:
            return False

    def devolver(self):
        if self.qtd_emprestados > 0 and (self.qtd_emprestados <= self.num_exemplares):
            self.qtd_emprestados += 1
            return True
        else:
            return False


class User:
    def __init__(self, nome, mat, cpf, us, senha, user, livro=[], ):
        self.nome = nome
        self.matricula = mat
        self.cpf = cpf
        self.username = us
        self.senha = senha
        self.cadastrar_user = user
        self.livros_emprestados = livro


    def cadastrar_user(self):
        novoUser = {'nome': input('Informe o nome do contato:'),
                'matricula': input('Informe a matricula do contato:'),
                'cpf': input('Informe o cpf do contato:'),
                'username': input('Informe o username do contato:'),
                'senha': input('Informe a senha do contato:')}

    while True:
      if input(" Gostaria de cadastrar um novo usuario? [S/N] R:").upper() == 'S': break
    else:





