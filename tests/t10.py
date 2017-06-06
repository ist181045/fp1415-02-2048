## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                 TEST 10                                    ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Teste: tabuleiros_iguais -- #
T1 = cria_tabuleiro()
T2 = cria_tabuleiro()
tabuleiros_iguais(T1, T2)
C = cria_coordenada(1, 2)
T1 = tabuleiro_preenche_posicao(T1, C, 2)
C = cria_coordenada(2, 3)
T1 = tabuleiro_preenche_posicao(T1, C, 4)
C = cria_coordenada(1, 2)
T2 = tabuleiro_preenche_posicao(T2, C, 2)
C = cria_coordenada(2, 3)
T2 = tabuleiro_preenche_posicao(T2, C, 4)
tabuleiros_iguais(T1, T2)
C = cria_coordenada(1, 1)
T2 = tabuleiro_preenche_posicao(T2, C, 256)
tabuleiros_iguais(T1, T2)