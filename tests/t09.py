## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                  TEST 09                                   ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Reconhecedores: e_tabuleiro, tabuleiro_terminado -- #
T = cria_tabuleiro()
e_tabuleiro(T)
C = cria_coordenada(1, 2)
T = tabuleiro_preenche_posicao(T, C, 2)
e_tabuleiro(T)
e_tabuleiro(C)
C = cria_coordenada(1, 4)
T = tabuleiro_preenche_posicao(T, C, 2)
e_tabuleiro(T)
escreve_tabuleiro(T)
J = pede_jogada()
W
T = tabuleiro_reduz(T, J)
e_tabuleiro(T)
C = cria_coordenada(1, 4)
T = tabuleiro_preenche_posicao(T, C, 2)
e_tabuleiro(T)
tabuleiro_terminado(T)
escreve_tabuleiro(T)
J = pede_jogada()
S
T = tabuleiro_reduz(T, J)
C = cria_coordenada(1, 4)
T = tabuleiro_preenche_posicao(T, C, 2)
escreve_tabuleiro(T)
e_tabuleiro(T)
tabuleiro_terminado(T)