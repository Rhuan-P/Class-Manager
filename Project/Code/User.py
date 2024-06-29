# Definição da Superclasse Usuario
User_List = []
class Usuario:

    def __init__(self, nome, idade, endereco, telefone, email, data_nascimento, genero, cpf, matricula):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.cpf = cpf
        self.matricula = matricula
        User_List.append(self.__dict__)
    def login(self, matricula, cpf):
        if self.matricula == matricula and self.cpf == cpf:
            return True
        else:
            return False
       
    def info(self):
        return (f'Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}, '
                f'Telefone: {self.telefone}, Email: {self.email}, '
                f'Data de Nascimento: {self.data_nascimento}, Gênero: {self.genero}, '
                f'CPF: {self.cpf}, Matrícula: {self.matricula}')

    def mais():
        return f'{User_List}'

# Definição da Subclasse Aluno 
class Aluno(Usuario):
    def __init__(self,turma,**kw):
        self.turma = turma
        super().__init__(**kw)

    def info(self):
        return f'{super().info()}, Turma: {self.turma}'

# Definição da Subclasse Professor
class Professor(Usuario):
    def __init__(self, salario, **kw):
        super().__init__(**kw)
        self.salario = salario
        
    def info(self):
        return f'{super().info()}, Salario: R$ {self.salario:.2f}'
    



