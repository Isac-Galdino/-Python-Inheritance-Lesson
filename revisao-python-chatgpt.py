class aluno:
    def __init__(self, nome, idade, curso, media, email):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        if media >= 0 and media <= 10:
            self.__media = media
        else:
            raise ValueError("A média informada é inválida. Informe uma média válida")

        if "@" not in email:
            raise ValueError("O email informado é inválido")
        else:
            self.__email = email

    def apresentar(self):
        return f"Nome: {self.nome}\nIdade: {self.idade} anos\nCurso: {self.curso}\nMedia: {self.__media}"

    def get_media(self):
        return f"A média deste aluno é {self.__media}"
    
    def set_media(self, nova_media):
        if nova_media >= 0 and nova_media <= 10:
            self.__media = nova_media
            return("Média alterada com sucesso!!")
        else:
            return f"A média não pode ser menor que 0 e maior que 10. Informe uma média válida"

    def verificar_aprovacao(self):
        if self.__media >= 6:
            return f"PARABÉNS {self.nome}!!! Você está aprovado(a)"
        elif self.__media < 6 and self.__media >= 4:
            return f"Tente melhor na próxima vez, você consegue {self.nome}"
        else:
            return f"{self.nome}, infelizmente você está reprovado(a)"
        
aluno1 = aluno("Isac Galdino Ferreira", 16, "Desenvolvimento de Sistemas", 8, "isac.galdino.gmail.com")
print(aluno1.set_media(9))
print(aluno1.get_media())
print(aluno1.verificar_aprovacao())
      

            
    
