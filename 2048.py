# Projecto 2 - 2048
# 80858 - Beatriz Grilo
# 81045 - Rui Ventura

NLINHAS = NCOLUNAS = 4

## =========================================================================== ##
## --------------------------------------------------------------------------- ##
## |                              TAD Coordenada                             | ##
## --------------------------------------------------------------------------- ##
## =========================================================================== ##

# ----------------------------------------------------------------------------- #
# |                                 CONSTRUTOR                                | #
# ----------------------------------------------------------------------------- #

def cria_coordenada(l, c):
    ''' cria_coordenada : inteiro x inteiro -> coordenada
        - Recebe dois argumentos, inteiros entre 1 e NLINHAS/NCOLUNAS e devolve
        uma coordenada. Devolve um erro se os parametros forem invalidos '''
    if isinstance(l, int) and 1 <= l <= NLINHAS and \
       isinstance(c, int) and 1 <= c <= NCOLUNAS:
        return (l, c)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')

# ----------------------------------------------------------------------------- #
# |                                 SELETORES                                 | #
# ----------------------------------------------------------------------------- #

def coordenada_linha(coord):
    ''' coordenada_linha : coordenada -> inteiro
        - Recebe uma coordenada e devolve o inteiro que e o valor da linha '''
    return coord[0]

def coordenada_coluna(coord):
    ''' coordenada_linha : coordenada -> inteiro
        - Recebe uma coordenada e devolve o inteiro que e o valor da coluna '''
    return coord[1]

# ----------------------------------------------------------------------------- #
# |                               RECONHECEDORES                              | #
# ----------------------------------------------------------------------------- #

def e_coordenada(arg):
    ''' e_coordenada : universal -> logico
        - Verifica se o argumento passado e a uma coordenada, verificando se a
        sua representacao corresponde a definida '''
    return isinstance(arg, tuple) and len(arg) == 2 and \
           isinstance(arg[0], int) and isinstance(arg[1], int) and \
           1 <= arg[0] <= NLINHAS and 1 <= arg[1] <= NCOLUNAS

# ----------------------------------------------------------------------------- #
# |                                   TESTES                                  | #
# ----------------------------------------------------------------------------- #

def coordenadas_iguais(c1, c2):
    ''' coordenadas_iguais : coordenada x coordenada -> logico
        - Testa se duas coordenadas sao iguais e compara as suas componentes en-
        tre si. (a, b) = (c, d) if a == c AND b == d '''
    return coordenada_linha(c1) == coordenada_linha(c2) and \
           coordenada_coluna(c1) == coordenada_coluna(c2)


## =========================================================================== ##
## --------------------------------------------------------------------------- ##
## |                             TAD Tabuleiro                               | ##
## --------------------------------------------------------------------------- ##
## =========================================================================== ##

# ----------------------------------------------------------------------------- #
# |                                 CONSTRUTOR                                | #
# ----------------------------------------------------------------------------- #

def cria_tabuleiro():
    ''' cria_tabuleiro: {} -> tabuleiro
        - Cria um dicionario que tem 2 chaves, uma para o tabuleiro de jogo em si
        representado por um lista e uma para a pontuacao, um inteiro '''
    lst_tab = list()
    # Uma lista com NLINHAS listas, cada uma com NCOLUNAS elementos
    for i in range(NLINHAS):
        lst_tab = lst_tab + [[0] * NCOLUNAS]
    return {'tabuleiro': lst_tab, 'pontuacao': 0}

# ----------------------------------------------------------------------------- #
# |                                 SELETORES                                 | #
# ----------------------------------------------------------------------------- #

def tabuleiro_posicao(tab, coord):
    ''' tabuleiro_posicao: tabuleiro x coordenada -> inteiro
        - Devolve o valor da peca na posicao de coordenadas 'coord' do tabuleiro
        'tab' '''
    if e_coordenada(coord):
        return tab['tabuleiro'][coordenada_linha(coord) - 1] \
                               [coordenada_coluna(coord) - 1]
    else:
        raise ValueError('tabuleiro_posicao: argumentos invalidos')

def tabuleiro_pontuacao(tab):
    ''' tabuleiro_pontuacao: tabuleiro -> inteiro
        - Devolve a pontuacao actual do tabuleiro 'tab' '''
    return tab['pontuacao']

def tabuleiro_posicoes_vazias(tab):
    ''' tabuleiro_posicoes_vazias: tabuleiro -> lista
        - Calcula e devolve uma lista com as coordenadas de todas as posicoes va-
        zias do tabuleiro 'tab' '''
    vazias = []
    for i in range(1, NLINHAS + 1):
        for j in range(1, NCOLUNAS + 1):
            c = cria_coordenada(i, j)
            if tabuleiro_posicao(tab, c) == 0:
                vazias = vazias + [c]
    return vazias

# ----------------------------------------------------------------------------- #
# |                               MODIFICADORES                               | #
# ----------------------------------------------------------------------------- #

def tabuleiro_preenche_posicao(tab, coord, val):
    ''' tabuleiro_preenche_posicao: tabuleiro x coordenada x inteiro -> tabuleiro
        - Preenche a posicao de coordenadas 'coord' com o valor 'v'. Devolve o
        tabuleiro 'tab' modificado '''
    if e_coordenada(coord) and isinstance(val, int):
        tab['tabuleiro'][coordenada_linha(coord) - 1] \
                        [coordenada_coluna(coord) - 1] = val
        return tab
    else:
        raise ValueError('tabuleiro_preenche_posicao: argumentos invalidos')

def tabuleiro_actualiza_pontuacao(tab, val):
    ''' tabuleiro_actualiza_pontuacao: tabuleiro x inteiro -> tabuleiro
        - Adiciona a pontuacao do tabuleiro 'tab' o valor 'v'. Devolve o tabulei-
        ro 'tab' com a pontuacao actualizada '''
    if isinstance(val, int) and val >= 0 and val % 4 == 0:
        tab['pontuacao'] = tab['pontuacao'] + val
        return tab
    else:
        raise ValueError('tabuleiro_actualiza_pontuacao: argumentos invalidos')

def tabuleiro_reduz(tab, jogada):
    ''' tabuleiro_reduz: tabuleiro x cad. caracteres -> tabuleiro
        - Reduz o tabuleiro 'tab' na direcao correspondente a 'jogada', efectuan-
        do ou nao combinacoes. Devolve o tabuleiro reduzido '''
    if not e_jogada(jogada):
        raise ValueError('tabuleiro_reduz: argumentos invalidos')
    else:
        coord_orig, prox_coord = 0, 0 # Inicializacao
        # Distincao entre movimentacoes horizontais e verticais. Permite tabulei-
        # ros de dimensoes n x p
        if jogada in ('N', 'S'):
            for j in range(1, NCOLUNAS + 1):
                travadas = [] # Coords de posicoes onde houve combo
                # Por linha/coluna fica vazia para minimizar iteracoes
                for k in range(NLINHAS - 1):
                    for i in range(2, NLINHAS + 1 - k):            
                        if jogada == 'N':
                            # Peca a mover
                            coord_orig = cria_coordenada(i, j)
                            # Posicao de destino
                            prox_coord = cria_coordenada(i - 1, j)
                        else:
                            coord_orig = cria_coordenada(NLINHAS + 1 - i, j)
                            prox_coord = cria_coordenada(NLINHAS + 1 - (i - 1),\
                                                         j)
                        # Move a peca, se possivel. Combina e trava as coordena-
                        # das que combinaram durante um varrimento (linha ou col-
                        # una)
                        tab, travadas = move_peca(tab, coord_orig, prox_coord, \
                                                  travadas)
        elif jogada in ('E', 'W'):
            for j in range(1, NLINHAS + 1):
                travadas = []
                for k in range(NCOLUNAS - 1):
                    for i in range(2, NCOLUNAS + 1 - k):            
                        if jogada == 'E':
                            coord_orig = cria_coordenada(j, NCOLUNAS + 1 - i)
                            prox_coord = cria_coordenada(j, NCOLUNAS + 1 - \
                                                         (i - 1))
                        else:
                            coord_orig = cria_coordenada(j, i)
                            prox_coord = cria_coordenada(j, i - 1)
                        tab, travadas = move_peca(tab, coord_orig, prox_coord, \
                                                  travadas)
        return tab
    
# Auxiliares (tabuleiro_reduz) ##################################################

def move_peca(tab, coord_orig, prox_coord, travadas):
    ''' move_pecas : tabuleiro x coordenada x coordenada x lista ->
        -> tabuleiro x lista 
        - Recebe um tabuleiro e as coordenadas das pecas a mover, juntamente com
        uma lista de coordenadas de posicoes entre as quais ocorrerem previamente
        combinacoes. Devolve o tabuleiro modificado, se possivel (combinacao ou
        nao) e a lista com as coordenadas onde houve combinacao'''
    valor_orig = tabuleiro_posicao(tab, coord_orig)
    prox_valor = tabuleiro_posicao(tab, prox_coord)
    
    if prox_valor == 0:
        if valor_orig != 0:
            tabuleiro_preenche_posicao(tab, prox_coord, valor_orig)
            tabuleiro_preenche_posicao(tab, coord_orig, 0)
    elif valor_orig == prox_valor:
        if coordenada_na_lista(coord_orig, travadas):
            return tab, travadas
        else:
            valor = valor_orig + prox_valor
            tabuleiro_preenche_posicao(tab, prox_coord, valor)
            tabuleiro_preenche_posicao(tab, coord_orig, 0)
            tabuleiro_actualiza_pontuacao(tab, valor)
            travadas = travadas + [coord_orig] + [prox_coord]
    
    return tab, travadas

def coordenada_na_lista(coord, lst):
    ''' coordenada_na_lista : coordenada x lista -> logico
        - Recebe uma coordenada e uma lista. Verifica se esta se encontra na
        lista e devolve o valor logico que comprove/refute tal condicao '''
    for c in lst:
        if coordenadas_iguais(coord, c):
            return True
    return False

# FIM AUXILIARES ################################################################

# ----------------------------------------------------------------------------- #
# |                               RECONHECEDORES                              | #
# ----------------------------------------------------------------------------- #

def e_tabuleiro(arg):
    ''' e_tabuleiro: universal -> logico
        - Verifica se 'arg' e do TAD tabuleiro. Verifica a representacao, a di-
        mensao de 'arg' e se tem as chaves 'tabuleiro' e 'pontuacao'. Verifica 
        ainda se o tabuleiro tem a dimensao certa '''
    e_tab = isinstance(arg, dict) and len(arg) == 2 and \
            'tabuleiro' in arg and isinstance(arg['tabuleiro'], list) and \
            'pontuacao' in arg and isinstance(arg['pontuacao'], int) and \
            len(arg['tabuleiro']) == NLINHAS
    if e_tab:
        for i in range(NLINHAS):
            e_tab = e_tab and len(arg['tabuleiro'][i]) == NCOLUNAS
    return e_tab

# ----------------------------------------------------------------------------- #
# |                                   TESTE                                   | #
# ----------------------------------------------------------------------------- #

def tabuleiro_terminado(tab):
    ''' tabuleiros_iguais: tabuleiro x tabuleiro -> logico
        - Reduz uma copia do tabuleiro em todas as direcoes. Se o original for i-
        gual a copia (implica que esta preenchido), o tabuleiro esta
        terminado '''
    return len(tabuleiro_posicoes_vazias(tab)) == 0 and \
           tabuleiros_iguais(tab, tabuleiro_reduz(copia_tabuleiro(tab), 'N')) and \
           tabuleiros_iguais(tab, tabuleiro_reduz(copia_tabuleiro(tab), 'S')) and \
           tabuleiros_iguais(tab, tabuleiro_reduz(copia_tabuleiro(tab), 'E')) and \
           tabuleiros_iguais(tab, tabuleiro_reduz(copia_tabuleiro(tab), 'W'))

def tabuleiros_iguais(tab1, tab2):
    ''' tabuleiros_iguais: tabuleiro x tabuleiro -> logico
        - Verifica se os tabuleiros 'tab1' e 'tab2' sao iguais. Compara o valor
        das posicoes e a pontuacao de cada um '''
    iguais = True
    for i in range(1, NLINHAS + 1):
        for j in range(1, NCOLUNAS + 1):
            c = cria_coordenada(i, j)
            iguais = iguais and tabuleiro_posicao(tab1, c) == \
                                tabuleiro_posicao(tab2, c)
            if not iguais:
                return iguais
    return iguais and tab1['pontuacao'] == tab2['pontuacao']

# ----------------------------------------------------------------------------- #
# |                              TRANSFORMADORES                              | #
# ----------------------------------------------------------------------------- #

def escreve_tabuleiro(tab):
    ''' escreve_tabuleiro: tabuleiro -> {}
        - Escreve a representacao externa do tabuleiro 'tab' '''
    if e_tabuleiro(tab):
        for i in range(1, NLINHAS + 1):
            linha = ''
            for j in range(1, NCOLUNAS + 1):
                linha = linha + ('[ ' + str(tabuleiro_posicao(\
                                            tab, cria_coordenada(i, j))) + ' ] ')
            print(linha)
        print('Pontuacao: ' + str(tabuleiro_pontuacao(tab)))
    else:
        raise ValueError('escreve_tabuleiro: argumentos invalidos')

## =========================================================================== ##
## --------------------------------------------------------------------------- ##
## |                            Funcoes Adicionais                           | ##
## --------------------------------------------------------------------------- ##
## =========================================================================== ##

def pede_jogada():
    ''' pede_jogada: {} -> cad. caracteres
        - Pede ao jogador para introduzir uma jogada, devolvendo a mesma, se for
        valida. '''
    jogada = input('Introduza uma jogada (N, S, E, W): ')
    while not e_jogada(jogada):
        print('Jogada invalida.')
        jogada = input('Introduza uma jogada (N, S, E, W): ')
    return jogada

def copia_tabuleiro(tab):
    ''' tabuleiro -> tabuleiro
        - Recebe um tabuleiro 'tab', cria e devolve uma copia do mesmo '''
    tab_copia = cria_tabuleiro()
    for i in range(1, NLINHAS + 1):
        for j in range(1, NCOLUNAS + 1):
            c = cria_coordenada(i, j)
            tabuleiro_preenche_posicao(tab_copia, c, tabuleiro_posicao(tab, c))
    tabuleiro_actualiza_pontuacao(tab_copia, tabuleiro_pontuacao(tab))
    return tab_copia

from random import random
def preenche_posicao_aleatoria(tab):
    ''' preenche_posicao_aleatoria: tabuleiro -> {}
        - Recebe um tabuleiro 'tab' e preenche uma posicao aleatoria com o valor
        2 ou 4 consoante a probabilidade associada, dado que existem posicoes
        vazias '''
    escolhas = (2, 2, 2, 2, 4) # Quatro 2 e um 4 => 80% de 2, 20% de 4 
    vazias = tabuleiro_posicoes_vazias(tab)

    return tabuleiro_preenche_posicao(tab, vazias[int(random() * len(vazias))], \
                                      escolhas[int(random() * len(escolhas))])

# EXTRA #########################################################################

def e_jogada(arg):
    ''' e_jogada: universal -> logico
        - Verifica se 'arg' e um caracter e uma das quatro direcoes validas e de-
        volve um valor logico, se e ou nao uma jogada valida '''
    return isinstance(arg, str) and arg in ('N', 'S', 'E', 'W')

# FIM EXTRA #####################################################################

## =========================================================================== ##
## --------------------------------------------------------------------------- ##
## |                                  JOGO                                   | ##
## --------------------------------------------------------------------------- ##
## =========================================================================== ##

def jogo_2048():
    ''' jogo_2048: {} -> {}
        - Inicia um jogo de 2048 (consola) '''
    tabuleiro_jogo = cria_tabuleiro()
    preenche_posicao_aleatoria(preenche_posicao_aleatoria(tabuleiro_jogo))
    
    achieved_2048, quit = False, False
    while not (tabuleiro_terminado(tabuleiro_jogo) or quit):
        escreve_tabuleiro(tabuleiro_jogo)
        tab_copia = copia_tabuleiro(tabuleiro_jogo)
        tabuleiro_reduz(tabuleiro_jogo, pede_jogada())
        # Se houver espaco ou o tabuleiro for diferente, preenche aleatoriamente
        if len(tabuleiro_posicoes_vazias(tabuleiro_jogo)) > 0 and \
           not tabuleiros_iguais(tabuleiro_jogo, tab_copia):
            preenche_posicao_aleatoria(tabuleiro_jogo)
            
        escreve_tabuleiro(tabuleiro_jogo)
        # Conseguiu uma posicao com 2048?
        if not achieved_2048 and posicao_no_tabuleiro(tabuleiro_jogo, 2048):
            achieved_2048 = True
            print('#===================================#\n' + \
                  '# Ganhou! :D Pode continuar a jogar #\n' + \
                  '#===================================#')
            continua = input('Pretende continuar (S/N)? ')[0]
            while not continua in ('S', 'N'):
                print('Resposta invalida.')
                continua = input('Pretende continuar? (S/N)')
            if continua == 'N':
                quit = True
    print('Jogo terminado.')

def posicao_no_tabuleiro(tab, val):
    ''' posicao_no_tabuleiro : tabuleiro x val -> logico
        - Recebe um tabuleiro e um inteiro. Percorre o tabuleiro 'tab' e verifi-
        ca se o valor 'val' se encontra no tabuleiro.'''
    if e_tabuleiro(tab) and isinstance(val, int):
        for i in range(1, NLINHAS + 1):
            for j in range(1, NCOLUNAS + 1):
                if tabuleiro_posicao(tab, cria_coordenada(i, j)) == val:
                    return True
    return False