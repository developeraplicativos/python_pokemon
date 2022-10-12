from Pokemon import *
from Pessoa import *
def escolha_incial(player):
    print('Olá {}, voce pode escolher o primeiro pokemons: '.format(player) )

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = Pokemon('Pikachu', level=1)
    squirtle  = Pokemon('Pikachu', level=1)

    print('Voce pode escolher entre 3 pokemons:')
    print('1 - pikachu', pikachu)
    print('2 - charmander', charmander)
    print('3 - squirtle', squirtle)

    while True:
        escolha = input('Qual você deseja? ')
        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha invalida')


player = Player('Emerson')
player.capturar(Pokemon('charmander',level=1) )

inimigo = Inimigo('Claudio', pokemons=[Pokemon('squirtle',level=2)])

player.batalhar(inimigo)