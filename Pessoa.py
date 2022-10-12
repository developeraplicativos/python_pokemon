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
            for index,pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem pokemon".format(self))
    def escolha_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{} irá batalhar com {}'.format(self,pokemon_escolhido))
            return pokemon_escolhido
        else:
            print('este inimigo não tem pokemons')
    def batalhar(self, Pessoa):
        print('{} começou uma batalha com {}'.format(self, Pessoa))
        pokemon_inimigo = Pessoa.escolha_pokemon()
        seu_pokemon = self.escolha_pokemon()

        if pokemon_inimigo and seu_pokemon:
            while True:
                vitoria = seu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print('{} ganhou a batalha'.format(self))
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(seu_pokemon)
                if vitoria_inimiga:
                    print('{} ganhou a batalha'.format(Pessoa))
                    break

        else:
            print('Essa batalha não pode ocorrer')


class Player(Pessoa):
    tipo = 'player'
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))
    def escolha_pokemon(self):
        self.mostrar_pokemons()
        while True:
            escolha = input('{}, escola o seu pokemon: '.format(self))

            if self.pokemons:
                try:
                    pokemon_escolhida = self.pokemons[int(escolha)]
                    print('o pokemon escolhido foi {}'.format(pokemon_escolhida))
                    return pokemon_escolhida
                except:
                    print('escolha invalida')
            else:
                print('este jogador não possue pokemon')

class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self,nome=None,pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMON))

        super().__init__(nome=nome, pokemons=pokemons)


