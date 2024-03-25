#EXPLICAÇÃO DA POO(trazendo mais esclarecimentos)

#Na orientação ao objeto possui conceitos
# O primeiro é o conceito de classe

# Self = Própio(Eu)

class User: #Recomendado usar letra maiscula no inicio da classe, para diferenciar

    #ASSIM SE DEFINE UMA CLASSE!
    def __init__(self):
          self.nome = None
          self.matricula = None
          self.cpf = None
          self.username = None
          self.senha = None
          self.email = None
          self.fone = None
          self.dt_nascimento = None
          self.livros_emprestados = [] #Lista vazia pq terá mais de um

# Atributos acima
#No java, ele usa "this" ao invés de self
# Atributo funciona como uma variavel, pois recebe valor
# Com a classe definida, podemos instanciar(construir/criar) um obj dessa classe invocando seu metodo construtor
#_______________________________________________________________________________________________________________

user1 = User() # Os parenteses vc usa quando chama uma função. A função daqui é o init, do metodo construtor
user2 = User()
user3 = User()
user4 = User()

# Assim q invoca uma função, acima

# O user1 é o nosso objeto pq ele recebe algo da classe, a referencia da memoria do obj pq ela armazena
# O user1 é uma variável diferente

# Variável é um espaço de memÓria!!!! IMPORTANTE!

#VC DEFINE A CLASSE UMA VEZ, MAS O PRODUTO(OBJ) PD SER VARIAS VEZES

user1.nome #Para acessar o atributo do obj, fazemos assim:
#nomeObjeto.nomeAtributo

print(user1.nome, user1.fone, user1.livros_emprestados)
#O self só se usa na classe, para definir q os atributos são própios delas

#_______________________________________________________________________________________________________________

class Livro:
    def __init__(self):
        pass