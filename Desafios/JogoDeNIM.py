def select(msg):
    '''
    Função para validar um input dado pelo usuário, permitindo apenas que seja recebido um valor inteiro.
    :param msg: Mensagem do input.
    :return: Variável na qual a mensagem está armazenada
    '''
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print()
            print('Dado inválido, digite novamente!')
            print()
            continue
        else:
            break
    return x


def computador_escolhe_jogada(n, m):
    '''
    Função usada para escolher a jogada do computador.
    :param n: Total de peças no tabuleiro.
    :param m: Limite de peças que pode ser retirado.
    :return: Valor escolhido pelo computador de acordo com a estratégia vencedora.
    '''
    t_peça = 0
    for c in range(1, (m + 1)):
        if (n - c) % (m + 1) == 0:
            t_peça = c
    if t_peça == 0:
        t_peça = m
    else:
        if t_peça == 1:
            print('O computador tirou uma peça.')
        else:
            print(f'O computador tirou {t_peça} peças.')
    if (n - t_peça) != 0:
        if (n - t_peça) == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print(f'Agora restam {n - t_peça} peças no tabuleiro.')
        print()
    return t_peça


def usuario_escolhe_jogada(n, m):
    '''
    Função para escolher a jogada do usuário
    :param n: Total de peças no tabuleiro.
    :param m: Limite de peças que pode ser retirado.
    :return: Valor escolhido pelo usuário.
    '''
    while True:
        t_peça = select('Quantas peça você vai tirar? ')
        if n - t_peça < 0:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
            continue
        if (t_peça >= 1) and (t_peça <= m):
            if t_peça == 1:
                print(f'Voce tirou uma peça.')
            else:
                print(f'Voce tirou {t_peça} peças.')
            break
        else:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
    if (n - t_peça) == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
    else:
        print(f'Agora restam {n - t_peça} no tabuleiro.')
    print()
    return t_peça


def partida():
    '''
    Função usada para executar uma partida, alternando entre o usuário e o computador, de acordo com a estratégia
    vencedora, para que o computador sempre ganhe.
    '''
    n = select('Quantas peças? ')
    m = select('Limite de peças por jogada? ')
    print()
    if n % (m + 1) == 0:
        print('Você começa!')
        print()
        tot = n
        vencedor = 0
        while True:
            # Vez do Usuário
            p_usuario = usuario_escolhe_jogada(tot, m)
            tot -= p_usuario  # O total recebe o que tem nele menos p_usuário
            if tot == 0:
                vencedor = 'usuário'
                break

            # Vez do Computador
            p_computador = computador_escolhe_jogada(tot, m)
            tot -= p_computador  # O total recebe o que tem nele menos p_computador
            if tot == 0:
                vencedor = 'computador'
                break
        print(f'Fim do jogo! O {vencedor} ganhou!')
    else:
        print('Computador começa!')
        print()
        tot = n
        vencedor = 0
        while tot > 0:
            # Vez do Computador
            p_computador = computador_escolhe_jogada(tot, m)
            tot -= p_computador  # O total recebe o que tem nele menos p_computador
            if tot == 0:
                vencedor = 'computador'
                break

            # Vez do Usuário
            p_usuario = usuario_escolhe_jogada(tot, m)
            tot -= p_usuario  # O total recebe o que tem nele menos p_usuário
            if tot == 0:
                vencedor = 'usuário'
                break
        print(f'Fim do jogo! O {vencedor} ganhou!')


def campeonato():
    '''
    Função usada para executar um campeonato (repetindo a função partida 3 vezes).
    '''
    for c in range(1, 4):
        print(f'**** Rodada {c} ****')
        print()
        partida()
        print()
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você 0 X 3 Computador')


def main():
    '''
    Função principal, usada para decidir se o usuário jogará uma partida isolada ou um campeonato.
    '''
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada\n'
          '2 - para jogar um campeonato ')
    while True:
        esc = select('>> ')
        print('')
        if esc == 1:
            print('Voce escolheu uma partida!')
            print()
            partida()
            break
        if esc == 2:
            print('Voce escolheu um campeonato!')
            print()
            campeonato()
            break
        else:
            print('Dado inválido, digite novamente!')
            continue


main()
