from Pokemon import *

import random

NOMES = ['carlos', 'jessy', 'james', 'picauinku', 'miau', 'astarauvesk']

POKEMON = [ Pokemon('Squarow'),Pokemon('chenchilachu'),Pokemon('pikachu'),Pokemon('rolinchu') ]

class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            for pokemon in self.pokemons:
                print("{} tem o pokemon {}".format(self, pokemon))
        else:
            print("{} não tem pokemon".format(self))



class Player(Pessoa):
    tipo = 'player'
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))

class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self,nome=None,pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMON))

        super().__init__(nome=nome, pokemons=pokemons)


inimigo = Inimigo()
inimigo.mostrar_pokemons()

