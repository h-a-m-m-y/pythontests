opcaomenu = 1
while opcaomenu != '0':
    print('Escolha uma opção:')
    print('1. Tutorial')
    print('2. Jogar')
    print('0. Sair')
    opcaomenu = input('A opção escolhida é: ')
    #clear
    if opcaomenu == '1':
        print('TUTORIAL:')
        print('Para escolher em qual espaço substituir por O ou X, digite o número correspondente.')
        print('O jogador que alinhar três X ou O na vertical, horizontal ou diagonal primeiro, vence.')
        print('Os números devem ser escritos exatamente como aparecem.')
    elif opcaomenu == '2':
        cimaesquerda = '7'
        cimameio = '8'
        cimadireita = '9'
        meioesquerda = '4'
        meiomeio = '5'
        meiodireita = '6'
        baixoesquerda = '1'
        baixomeio = '2'
        baixodireita = '3'
        rodada = 0
        vencedor = 0
        while rodada <= 5 and vencedor == 0:
            if cimaesquerda == 'X' and cimameio == 'X' and cimadireita == 'X' or meioesquerda == 'X' and meiomeio == 'X' and meiodireita == 'X' or baixoesquerda == 'X' and baixomeio == 'X' and baixodireita == 'X' or cimaesquerda == 'X' and meioesquerda == 'X' and baixoesquerda == 'X' or cimameio == 'X' and meiomeio == 'X' and baixomeio == 'X' or cimadireita == 'X' and meiodireita == 'X' and baixodireita == 'X' or cimaesquerda == 'X' and meiomeio == 'X' and baixodireita == 'X' or cimadireita == 'X' and meiomeio == 'X' and baixoesquerda == 'X':
                print('{}|{}|{}'.format(cimaesquerda, cimameio, cimadireita))
                print('-----')
                print('{}|{}|{}'.format(meioesquerda, meiomeio, meiodireita))
                print('-----')
                print('{}|{}|{}'.format(baixoesquerda, baixomeio, baixodireita))
                print('O Jogador que usou o X ganhou!')
                vencedor = vencedor + 1
            elif cimaesquerda == 'O' and cimameio == 'O' and cimadireita == 'O' or meioesquerda == 'O' and meiomeio == 'O' and meiodireita == 'O' or baixoesquerda == 'O' and baixomeio == 'O' and baixodireita == 'O' or cimaesquerda == 'O' and meioesquerda == 'O' and baixoesquerda == 'O' or cimameio == 'O' and meiomeio == 'O' and baixomeio == 'O' or cimadireita == 'O' and meiodireita == 'O' and baixodireita == 'O' or cimaesquerda == 'O' and meiomeio == 'O' and baixodireita == 'O' or cimadireita == 'O' and meiomeio == 'O' and baixoesquerda == 'O':
                print('{}|{}|{}'.format(cimaesquerda, cimameio, cimadireita))
                print('-----')
                print('{}|{}|{}'.format(meioesquerda, meiomeio, meiodireita))
                print('-----')
                print('{}|{}|{}'.format(baixoesquerda, baixomeio, baixodireita))
                print('O Jogador que usou o O ganhou!')
                vencedor = vencedor + 1
            elif rodada >= 5:
                print('Deu velha!')
                vencedor = vencedor + 1
            else:
                rodada = rodada + 1
                print('{}|{}|{}'.format(cimaesquerda, cimameio, cimadireita))
                print('-----')
                print('{}|{}|{}'.format(meioesquerda, meiomeio, meiodireita))
                print('-----')
                print('{}|{}|{}'.format(baixoesquerda, baixomeio, baixodireita))
                jogada = input('Digite o número correspondente ao espaço desejado: ')
                if jogada == '7':
                    cimaesquerda = 'X'
                elif jogada == '8':
                    cimameio = 'X'
                elif jogada == '9':
                    cimadireita = 'X'
                elif jogada == '4':
                    meioesquerda = 'X'
                elif jogada == '5':
                    meiomeio = 'X'
                elif jogada == '6':
                    meiodireita = 'X'
                elif jogada == '1':
                    baixoesquerda = 'X'
                elif jogada == '2':
                    baixomeio = 'X'
                elif jogada == '3':
                    baixodireita = 'X'
                print('{}|{}|{}'.format(cimaesquerda, cimameio, cimadireita))
                print('-----')
                print('{}|{}|{}'.format(meioesquerda, meiomeio, meiodireita))
                print('-----')
                print('{}|{}|{}'.format(baixoesquerda, baixomeio, baixodireita))
                jogada = input('Digite o número correspondente ao espaço desejado: ')
                if jogada == '7':
                    cimaesquerda = 'O'
                elif jogada == '8':
                    cimameio = 'O'
                elif jogada == '9':
                    cimadireita = 'O'
                elif jogada == '4':
                    meioesquerda = 'O'
                elif jogada == '5':
                    meiomeio = 'O'
                elif jogada == '6':
                    meiodireita = 'O'
                elif jogada == '1':
                    baixoesquerda = 'O'
                elif jogada == '2':
                    baixomeio = 'O'
                elif jogada == '3':
                    baixodireita = 'O'
    elif opcaomenu == '0':
        print('Até mais!')
    else:
        print('Opção Inválida, tente novamente!')
