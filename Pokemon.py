import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        self.level = level

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 200)

        if nome:
            self.nome = nome
        else:
            self.nome = self.especie

        self.vida = self.level * 10;
        self.ataque = self.level * 5;

    def __str__(self):
        return "Pokemon {} ({})".format(self.especie, self.level)

    def atacar(self, pokemon):
        pokemon.vida = pokemon.vida - self.ataque
        print('{} perdeu {} pontos de vida'.format(pokemon, self.ataque))

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
        else:
            return False
class PokemonEletrico(Pokemon):
    tipo = 'eletricidade'
    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon ) )
        return super().atacar(pokemon)



class PikachuFogo(Pokemon):
    tipo = 'fogo'
    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo em {}".format(self, pokemon ) )
        return super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = 'agua'
    def atacar(self, pokemon):
        print("{} lançou um jato de água em {}".format(self, pokemon ) )
        return super().atacar(pokemon)

class PokemonAr(Pokemon):
    tipo = 'ar'
    def atacar(self, pokemon):
        print("{} lançou uma rajada de ar em {}".format(self, pokemon ) )
        return super().atacar(pokemon)
