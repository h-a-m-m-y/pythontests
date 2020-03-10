opcaomenu = 1
while opcaomenu != '0':
    print('Escolha uma opção:')
    print('1. Tutorial')
    print('2. Jogar')
    print('0. Sair')
    opcaomenu = input('A opção escolhida é: ')
    if opcaomenu == '1':
        print('TUTORIAL:')
        print('Cada jogador escolhe se quer Par ou Ímpar e em seguida, um número,.')
        print('A soma dos números será feita e então será feita a verificação se o número é par ou ímpar.')
        print('O jogador que escolher a correspondente vencerá.')
    elif opcaomenu == '2':
        nomejogador1 = input('Digite o nome do primeiro jogador: ')
        nomejogador2 = input('Digite o nome do segundo jogador: ')
        escolhajogador1 = input('{}, você quer Par ou Ímpar? '.format(nomejogador1))
        if escolhajogador1 == 'Par':
            escolhajogador2 = 'Ímpar'
        elif escolhajogador1 == 'Ímpar':
            escolhajogador2 = 'Par'
        else:
            escolhajogador1 = 'Inválida!'
            escolhajogador2 = 'Inválida!'
            print('Escolha inválida!')
        numerojogador1 = int(input('{}, digite um número: '.format(nomejogador1)))
        numerojogador2 = int(input('{}, digite um número: '.format(nomejogador2)))
        numerofinal = numerojogador1 + numerojogador2
        if escolhajogador1 == 'Inválida!':
            print('Escolha de {} é inválida!'.format(nomejogador1))
        elif escolhajogador2 == 'Inválida!':
            print('Escolha de {} é inválida!'.format(nomejogador2))
        if numerofinal % 2 == 0 and escolhajogador1 == 'Par':
            print('{} é Par, logo {} ganhou!'.format(numerofinal, nomejogador1))
        elif numerofinal % 2 == 0 and escolhajogador2 == 'Par':
            print('{} é Par, logo {} ganhou!'.format(numerofinal, nomejogador2))
        elif numerofinal % 2 != 0 and escolhajogador1 == 'Ímpar':
            print('{} é Ímpar, logo {} ganhou!'.format(numerofinal, nomejogador1))
        elif numerofinal % 2 != 0 and escolhajogador2 == 'Ímpar':
            print('{} é Ímpar, logo {} ganhou!'.format(numerofinal, nomejogador2))
        else:
            print('Ocorreu um erro!')
else:
    print('Até mais!')
