# ALUNOS
# Pedro Pereira de Brito Neto
# RA: 1902175

# Scarlet Fernanda Machado Barros da Silva
# RA: 1902346


class Sala:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.horarios = ['16:00', '17:00', '18:00', '19:30', '20:00', '22:00', '23:00']

    def adicionar_horario(self, horario):
        self.horarios.append(horario)

    def exibirdados(self):
        print('Nome da sala: ', self.nome)
        print('A capacidade da sala é:', self.capacidade)
        print('Horarios Disponíveis: ')
        for x in self.horarios:
            print(x)


class Filme:
    def __init__(self, nomept, noriginal, diretor, anoLan, tipo, sinopse, premios):
        self.nomePt = nomept
        self.nomeOriginal = noriginal
        self.diretor = diretor
        self.lancamentoAno = anoLan
        self.tipo = tipo
        self.sinopse = sinopse
        self.indicPremio = premios

    def exibir_filme(self):
        p = ("--------------------------------")
        print(p)
        print('Nome do Filme:', self.nomePt)
        print('Nome Original do Filme:', self.nomeOriginal)
        print('Diretor', self.diretor)
        print('Ano de lançamento', self.lancamentoAno)
        print('Tipo de Filme:', self.tipo)
        print('Sinopse:', self.sinopse)
        if self.indicPremio is not None:
            print('Indicações e Prêmios: ', self.indicPremio)
        print(p)


class Funcionarios:
    def __init__(self, numcarteira, nome, funcao, salario):
        self.numcarteira = numcarteira
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def exibir_funcionario(self):
        p = ('------------------')
        print(p)
        print('Numero da carteira:', self.numcarteira)
        print('Nome:', self.nome)
        print('Função:', self.funcao)
        print('Salario R$:', "%.2f" % self.salario)
        print(p)


# Classes que herdam de funcionários
class Pipoqueiro(Funcionarios):
    def __init__(self, numcarteira, nome, funcao, salario):
        super().__init__(numcarteira, nome, funcao, salario)


class Caixa(Funcionarios):
    def __init__(self, numcarteira, nome, funcao, salario):
        super().__init__(numcarteira, nome, funcao, salario)


class Projecionista(Funcionarios):
    def __init__(self, numcarteira, nome, funcao, salario):
        super().__init__(numcarteira, nome, funcao, salario)


class Faxineiro(Funcionarios):
    def __init__(self, numcarteira, nome, funcao, salario):
        super().__init__(numcarteira, nome, funcao, salario)


# Filme
filme1 = Filme('O Rei Leão', 'The King Lion', 'Pedro Brito', 2019, 'INFANTIL', 'Filme conta a historio de um leao que se torna rei', None)
filme2 = Filme('Matriz', 'Matrix', 'Lilly e Lana Wachowski', 1999, 'Ficcão-Científica e Ação', 'Um jovem programador é atormentado por estranhos pesadelos nos quais sempre está conectado por cabos a um imenso sistema de computadores do futuro. À medida que o sonho se repete, ele começa a levantar dúvidas sobre a realidade. E quando encontra os misteriosos Morpheus e Trinity, ele descobre que é vítima do Matrix, um sistema inteligente e artificial que manipula a mente das pessoas e cria a ilusão de um mundo real enquanto usa os cérebros e corpos dos indivíduos para produzir energia.',
'Oscar Alwards')

print('Primeiro Filme')
filme1.exibir_filme()

print('Segundo Filme')
filme2.exibir_filme()


# Estanciando Salas
listadehorarios = ['16:00', '17:00', '18:00', '19:30', '20:00', '22:00', '23:00']

sala1 = Sala('XD Surround Extreme 01', 20)
sala2 = Sala('3D Surround', 30)
sala3 = Sala('2D', 40)

sala1.exibirdados()
sala2.exibirdados()
sala3.exibirdados()

# Estanciando Funcionários

projecionista2 = Projecionista(10014, 'Felipe', 'Projecionista', 2500)
projecionista1 = Projecionista(10012, 'João', 'Projecionista', 2500)

caixa1 = Pipoqueiro(10011, 'Pedro', 'Caixa', 1500)
caixa2 = Pipoqueiro(10016, 'Jhonatan', 'Caixa', 1500)

pipoqueiro1 = Pipoqueiro(10015, 'Pedro', 'Pipoqueiro', 1500)
pipoqueiro2 = Pipoqueiro(10014, 'Carolina', 'Pipoqueira', 1500)

faxineiro1 = Faxineiro(10013, 'Eduardo', 'Faxineiro', 1200)
faxineiro2 = Faxineiro(10013, 'Amélia', 'Faxineira', 1200.00)


# exibir dados do funcionario

pipoqueiro1.exibir_funcionario()
pipoqueiro2.exibir_funcionario()

projecionista1.exibir_funcionario()
projecionista2.exibir_funcionario()

caixa1.exibir_funcionario()
caixa2.exibir_funcionario()

faxineiro1.exibir_funcionario()
faxineiro2.exibir_funcionario()
