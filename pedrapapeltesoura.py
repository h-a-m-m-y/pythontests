import random
opcaomenu = 1
while opcaomenu != '0':
    print('Escolha uma opção:')
    print('1. Tutorial')
    print('2. Jogar Contra Outra Pessoa')
    print('3. Jogar Contra a Máquina')
    print('0. Sair')
    opcaomenu = input('A opção escolhida é: ')
    #clear
    if opcaomenu == '1':
        print('TUTORIAL:')
        print('Cada jogador escolhe entre Pedra, Papel ou Tesoura, que deve ser escrito exatamente como aparece na tela.')
        print('Pedra vence Tesoura, que por sua vez vence Papel, que por sua vez vence Pedra.')
        print('Boa sorte e divirta-se!')
    elif opcaomenu == '2':
        jogador1 = input('Digite o nome do Jogador 1: ')
        jogador2 = input('Digite o nome do Jogador 2: ')
        escolhajogador1 = input('Jogador 1, escolha entre Pedra, Papel ou Tesoura: ')
        #clear
        escolhajogador2 = input('Jogador 2, escolha entre Pedra, Papel ou Tesoura: ')
        #clear
        if escolhajogador1 == 'Pedra' and escolhajogador2 == 'Tesoura':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 1 ({}) ganhou.'.format(jogador1, escolhajogador1, jogador2, escolhajogador2, jogador1))
        elif escolhajogador1 == 'Papel' and escolhajogador2 == 'Pedra':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 1 ({}) ganhou.'.format(jogador1, escolhajogador1, jogador2, escolhajogador2, jogador1))
        elif escolhajogador1 == 'Tesoura' and escolhajogador2 == 'Papel':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 1 ({}) ganhou.'.format(jogador1, escolhajogador1, jogador2, escolhajogador2, jogador1))
        elif escolhajogador1 == 'Tesoura' and escolhajogador2 == 'Pedra':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 2 ({}) ganhou.'.format(jogador1, escolhajogador1, jogador2, escolhajogador2, jogador2))
        elif escolhajogador1 == 'Pedra' and escolhajogador2 == 'Papel':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 2 ({}) ganhou.'.format(jogador1, escolhajogador1, jogador2, escolhajogador2, jogador2))
        elif escolhajogador1 == 'Papel' and escolhajogador2 == 'Tesoura':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 2 ({}) ganhou.'.format(jogador1, escolhajogador1, jogador2, escolhajogador2, jogador2))
        elif escolhajogador1 != 'Pedra' and escolhajogador1 != 'Papel' and escolhajogador1 != 'Tesoura' and escolhajogador2 != 'Pedra' and escolhajogador2 != 'Papel' and escolhajogador2 != 'Tesoura':
            print('A escolha de ambos jogadores é inválida.')
        elif escolhajogador1 != 'Pedra' and escolhajogador1 != 'Papel' and escolhajogador1 != 'Tesoura':
            print('A escolha de {} é inválida.'.format(jogador1))
        elif escolhajogador2 != 'Pedra' and escolhajogador2 != 'Papel' and escolhajogador2 != 'Tesoura':
            print('A escolha de {} é inválida'.format(jogador2))
        elif escolhajogador1 == escolhajogador2:
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o resultado foi empate!'.format(jogador1, escolhajogador1, jogador2, escolhajogador2))
    elif opcaomenu == '3':
        jogador1 = input('Digite o nome do Jogador 1: ')
        jogador2 = 'Máquina'
        escolhajogador1 = input('Jogador 1, escolha entre Pedra, Papel ou Tesoura: ')
        # clear
        escolhajogador2 = random.randint(1, 3)
        if escolhajogador2 == 1:
            escolhajogador2 = 'Pedra'
        elif escolhajogador2 == 2:
            escolhajogador2 = 'Papel'
        elif escolhajogador2 == 3:
            escolhajogador2 = 'Tesoura'
        # clear
        if escolhajogador1 == 'Pedra' and escolhajogador2 == 'Tesoura':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 1 ({}) ganhou.'.format(
                jogador1, escolhajogador1, jogador2, escolhajogador2, jogador1))
        elif escolhajogador1 == 'Papel' and escolhajogador2 == 'Pedra':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 1 ({}) ganhou.'.format(
                jogador1, escolhajogador1, jogador2, escolhajogador2, jogador1))
        elif escolhajogador1 == 'Tesoura' and escolhajogador2 == 'Papel':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 1 ({}) ganhou.'.format(
                jogador1, escolhajogador1, jogador2, escolhajogador2, jogador1))
        elif escolhajogador1 == 'Tesoura' and escolhajogador2 == 'Pedra':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 2 ({}) ganhou.'.format(
                jogador1, escolhajogador1, jogador2, escolhajogador2, jogador2))
        elif escolhajogador1 == 'Pedra' and escolhajogador2 == 'Papel':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 2 ({}) ganhou.'.format(
                jogador1, escolhajogador1, jogador2, escolhajogador2, jogador2))
        elif escolhajogador1 == 'Papel' and escolhajogador2 == 'Tesoura':
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o Jogador 2 ({}) ganhou.'.format(
                jogador1, escolhajogador1, jogador2, escolhajogador2, jogador2))
        elif escolhajogador1 != 'Pedra' and escolhajogador1 != 'Papel' and escolhajogador1 != 'Tesoura' and escolhajogador2 != 'Pedra' and escolhajogador2 != 'Papel' and escolhajogador2 != 'Tesoura':
            print('A escolha de ambos jogadores é inválida.')
        elif escolhajogador1 != 'Pedra' and escolhajogador1 != 'Papel' and escolhajogador1 != 'Tesoura':
            print('A escolha de {} é inválida.'.format(jogador1))
        elif escolhajogador2 != 'Pedra' and escolhajogador2 != 'Papel' and escolhajogador2 != 'Tesoura':
            print('A escolha de {} é inválida'.format(jogador2))
        elif escolhajogador1 == escolhajogador2:
            print('O Jogador 1 ({}) escolheu {}, o Jogador 2 ({}) escolheu {}, logo o resultado foi empate!'.format(jogador1, escolhajogador1, jogador2, escolhajogador2))
        else:
            print('Ocorreu um erro inesperado.')
    elif opcaomenu == '0':
        print('Até mais!')
    else:
        print('Opção inválida, tente novamente.')
