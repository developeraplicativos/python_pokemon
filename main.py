import pickle

from Pokemon import *
from Pessoa import *

def escolha_incial(player):
    print('Olá {}, voce pode escolher o primeiro pokemons: '.format(player) )

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PikachuFogo('Charmander', level=1)
    squirtle  = PokemonAr('Squirtle', level=1)

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

def salvar_jogo(player):
    try:
        with open('database.db','wb') as arquivo:
            pickle.dump(player, arquivo)
            print('jogo salvo com sucesso')
    except Exception as error:
        print('error: ')
        print(error)

def load_jogo():
    try:
        with open('database.db','rb') as arquivo:
            player = pickle.load(arquivo)
            print('loading com sucesso')
            return player
    except Exception as error:
        print('save não encontrado ')
        print(error)

if __name__ == '__main__':
    player = load_jogo()

    if not player:
        print('Bem vindo ao mundo pokemon.')
        nome = input('Qual seu nome?')
        player = Player(nome)
        print('Olá, {}. Capture pokemons e lute contra seus inimigos.'.format(nome))
        if player.pokemons:
            print('você já possui pokemon')
            player.mostrar_dinheiro()
        else:
            print('voce não tem pokemon, escolha um!')
            escolha_incial(player)

        print('Você já pode lutar contra jorge tadeu')
        jorge = Inimigo(nome='Jorge Tadeu', pokemons=[PokemonAgua('Squirtle',level=1)])
        player.batalhar(jorge)
        salvar_jogo(player)

    while True:
        print('o que deseja fazer?')
        print('0 - Fechar o game')
        print('1 - Andar pelo mundo')
        print('2 - Lutar contra inimigo')

        escolha = input('Sua escolha')
        if escolha == '0':
            print('fechando o jogo')
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        else:
            print('Escolha invalida')

