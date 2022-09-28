class Pokemon:
    def __init__(self, especie, level=1, nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = self.especie

    def __str__(self):
        return "Pokemon {} ({})".format(self.especie, self.level)

    def atacar(self, pokemon):
        print("{} lançou um raio do trocão em {}".format(self, pokemon ) )

class PokemonEletrico(Pokemon):
    tipo = 'eletricidade'
    def atacar(self, pokemon):
        print("{} lançou um raio do trocão em {}".format(self, pokemon ) )


class Pikachu(PokemonEletrico):
    tipo = 'eletricidade'
    def atacar(self, pokemon):
        print("{} lançou um raio do trocão em {}".format(self, pokemon ) )

meu_pokemon_elentrico = PokemonEletrico('picachu')
print(meu_pokemon_elentrico.atacar('boruto'))