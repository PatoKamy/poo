class User:
    def __init__(self, nome, mat, cpf, us, senha, ema, fone, dtn, livro =[]):
        self.nome = nome
        self.matricula = mat
        self.cpf = cpf
        self.username = us
        self.senha = senha
        self.email = ema
        self.fone = fone
        self.dt_nascimento = dtn
        self.livros_emprestados = livro

#_____________________
list_user = []
x = input("Nome: ")
y = input("Matricula: ")
z = input("Cpf:")
h = input("Nome do usuario: ")
o = input("Senha: ")
i = input("E-mail: ")
j = input("Telefone: ")
k = input("Data de nascimento: ")
user1 = User(x, y, z, h, o , i , j, k) #parametro q será passado para o atributo
print(user1.email)