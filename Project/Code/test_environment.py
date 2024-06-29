from User import *
from random import choice, randint

nomes = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"]
idades = [20, 25, 30, 35, 40]
enderecos = ["Rua X, 123", "Avenida Y, 456", "Travessa Z, 789", "Rua W, 321", "Avenida V, 654"]
telefones = ["111111111", "222222222", "333333333", "444444444", "555555555"]
emails = ["alice@example.com", "bob@example.com", "carlos@example.com", "diana@example.com", "eduardo@example.com"]
datas_nascimento = ["01/01/2000", "02/02/1995", "03/03/1990", "04/04/1985", "05/05/1980"]
generos = ["Feminino", "Masculino", "Outro"]
cpfs = ["111.111.111-11", "222.222.222-22", "333.333.333-33", "444.444.444-44", "555.555.555-55"]
matriculas = ["001", "002", "003", "004", "005"]
turmas = ["Turma A", "Turma B", "Turma C", "Turma D", "Turma E"]
salarios = [3000.00, 3500.00, 4000.00, 4500.00, 5000.00]

for x in range(2):
    Aluno(
    nome = choice(nomes),
    idade = choice(idades),
    endereco = choice(enderecos),
    telefone = choice(telefones),
    email = choice(emails),
    data_nascimento = choice(datas_nascimento),
    genero = choice(generos),
    cpf = choice(cpfs),
    matricula = choice(matriculas),
    turma = choice(turmas)
    )

    Professor(
    nome = choice(nomes),
    idade = choice(idades),
    endereco = choice(enderecos),
    telefone = choice(telefones),
    email = choice(emails),
    data_nascimento = choice(datas_nascimento),
    genero = choice(generos),
    cpf = choice(cpfs),
    matricula = choice(matriculas),
    salario = choice(salarios)
    )


