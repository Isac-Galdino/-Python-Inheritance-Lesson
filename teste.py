# criando uma classe de aluno e uma classe de professor para serem usados em uma herança de ambas as classes
class aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def detalhes(self):
        return f"{self.nome} tem {self.idade} anos"

class professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def detalhes(self):
        return f"{self.nome} tem {self.idade} anos"

class pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def detalhes(self):
        return f"{self.nome} tem {self.idade} anos."

class aluno(pessoa):
    def __init__(self, nome, idade, estilo):
        super().__init__(nome, idade)
        self.estilo = estilo
        print("Estilo:", self.estilo)

class professor(pessoa):

    def __init__(self, nome, idade, materia):
        super().__init__(nome, idade)
        self.materia = materia
    def detalhes(self):
        super().detalhes()
        print("Matéria:", self.materia)

aluno1 = aluno("João", 20, "engenharia")
professor1 = professor("luzia", 59, "englhish")
print(aluno1.detalhes())
print(professor1.detalhes())