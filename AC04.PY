

class Cinema:
    def __init__(self):
        self.salas = []
        self.filmes = []
        self.horarios = []

    def adicionarsalas(self, salas):
        self.salas.append(salas)

    def add_filmes(self, filmes):
        self.filmes.append(filmes)

    def exibirdados(self, salas, filmes):
        print('A sala é', self.salas)
                #print('O horario é', self.horarios)
        print('O nome do filme é:', self.filmes)


class Sala:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade

    def exibirdados(self):
        print('Nome da sal: ', self.nome)
        print('A capacidade da sala é:', self.capacidade)


class Filme(Cinema):
    def __init__(self, nomept, noriginal, diretor, anoLan, tipo, sinopse):
        self.nomePt = nomept
        self.nomeOriginal = noriginal
        self.diretor = diretor
        self.lancamentoAno = anoLan
        self.tipo = tipo
        self.sinopse = sinopse
        self.indicPremio = None

    def exibir_filme(self):
        print('Nome do Filme:', self.nomePt)
        print('Nome Original do Filme:', self.nomeOriginal)
        print('Diretor', self.diretor)
        print('Ano de lançamento', self.lancamentoAno)
        print('Tipo de Filme:', self.tipo)
        print('Sinopse:', self.sinopse)
        if self.indicPremio is None:
            print('Sem premio ou indicações')
        else:
            print(self.indicPremio)


class Funcionarios:
    def __init__(self, numcarteira, nome, funcao, salario):
        self.numcarteira = numcarteira
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def exibir_funcionario(self):
        print('Numero da carteira:', self.numcarteira)
        print('------------------')
        print('Nome:', self.nome)
        print('------------------')
        print('Função:', self.funcao)
        print('------------------')
        print('Salario', self.salario)
        print('------------------')
        



filme1 = Filme('O Rei Leão', 'The King Lion', 'Pedro Brito', 2019, 'INFANTIL', 'Filme conta a historio de um leao que se torna rei')
filme1.exibir_filme()

sala1 = Sala('Sala 01', 20)
sala2 = Sala('Sala 02', 30)
sala2.exibirdados()


funcionario1 = Funcionarios(10010, 'Scarlet', 'Pipoqueira', 1100)
funcionario1.exibir_funcionario()




