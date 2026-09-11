#Revisao de objetos
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome;
        self.idade = idade;
    def detalhes(self):
        return f"Seu nome é {self.nome} e você tem {self.idade} anos";
pessoa1 = pessoa("galgal","17");
#print(pessoa1.detalhes());

#Revisão de heranças
class animal:
    def __init__(self, nome, idade):
        self.nome = nome;
        self.idade = idade;
    def detalhes(self):
        return f"Eu sou {self.nome} e tenho {self.idade} anos";
class cachorro(animal):
    def latir(self):
        return f"AU AU";
#faz com que a classe cachorro se comporte como um derivado para a classe animal
cachorro1 = cachorro("Lindinha", "3");
#faz com que, após a diferenciação de classes, a classe cachorro possa herdar as funções da classe animal
cachorro1.detalhes();
cachorro1.latir();
#print(cachorro1.detalhes())
#print(cachorro1.latir())

#Revisão de polimorfismo
#O polimorfismo me permite usar de métodos
class cachorro:
    def fazer_som(self):
        print("Au au");

class gato:
    def fazer_som(self):
        print("Miau miau");

def emitir_som(objeto_animal):
    objeto_animal.fazer_som();

c = cachorro();
g = gato();

#emitir_som(c);
#emitir_som(g);

#Revisão de o que é encapsulamento
class contabancaria:
    def __init__(self, titular, valor_inicial):
        self.titular = titular;
        self.__valor_inicial = valor_inicial;
    
    def depositar(self, valor):
        if valor > 0:
            self.__valor_inicial += valor;
            print(f"Olá {self.titular}! O depósito de R$ {valor} foi realizado");
        else:
            print("O valor de depósito é inválido");

    def mostrar_valor(self):
        return f"O valor após o depósito é {self.__valor_inicial}";

# v = contabancaria("Galdino", 1000);
# v.depositar(1000);
# print(v.mostrar_valor());

class game:
    def __init__(self, game_name, game_value):
        self.game_name = game_name;
        self.__game_value = game_value;
    
    def game_value_increase(self, increasment):
        self.__game_value += increasment;
        if increasment > 0:
            print(f"O {self.game_name} aumentou em R$ {self.increasment}");
        elif increasment < 0:
            print(f"O {self.game_name} abaixou em R$ {self.increasment}");
        elif increasment == 0:
            print(f"O {sef.game_name} não aumentou e nem abaixou de preço");

    def mostrar_preço(self):
        return f"O novo valor do {self.game_name} é de {self.__game_value}"

new_value = game("God Of War", 300)
new_value.game_value_increase(50)
print(new_value.mostrar_preço())
            
