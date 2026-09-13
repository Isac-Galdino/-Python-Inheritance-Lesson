class aluno:
    def __init__(self, nome, idade, curso, media):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.__media = media

    def apresentar(self):
        return f"Nome: {self.nome}\nIdade: {self.idade} anos\nCurso: {self.curso}\nMedia: {self.__media}"

    def get_media(self):
        return f"A nota deste aluno é {self.__media}"

    def set_media(self, nova_media):
        if nova_media >= 0 and nova_media <= 10:
            self.__media = nova_media
        else:
            return f"A nota informada não é válida"

    def verificar_aprovacao(self):
        if self.__media >= 6:
            return f"PARABÉNS {self.nome}!!! Você está aprovado(a)"
        elif self.__media < 6 and self.__media >= 4:
            return f"Tente melhor na próxima vez, você consegue {self.nome}"
        else:
            return f"{self.nome}, infelizmente você está reprovado(a)"

aluno1 = aluno("galdino", 16, "Desenvolvimento de sistemas", 6)
print(aluno1.get_media())
print(aluno1.set_media(8))
print(aluno1.apresentar())

            
    
