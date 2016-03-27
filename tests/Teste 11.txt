## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                 TESTE 11                                   ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Teste: pede_jogada; transformador de saida: escreve_tabuleiro
T = cria_tabuleiro()
escreve_tabuleiro(T)
C = cria_coordenada(1, 2)
T = tabuleiro_preenche_posicao(T, C, 2)
escreve_tabuleiro(T)
C = cria_coordenada(2, 3)
T = tabuleiro_preenche_posicao(T, C, 4)
T = tabuleiro_actualiza_pontuacao(T, 48)
escreve_tabuleiro(T)
C = cria_coordenada(2, 2)
T = tabuleiro_preenche_posicao(T, C, 8)
escreve_tabuleiro(T)
C = cria_coordenada(3, 3)
T = tabuleiro_preenche_posicao(T, C, 2048)
T = tabuleiro_actualiza_pontuacao(T, 2048)
escreve_tabuleiro(T)
C = cria_coordenada(1, 1)
T = tabuleiro_preenche_posicao(T, C, 256)
escreve_tabuleiro(T)
T = cria_tabuleiro()
C = cria_coordenada(1, 2)
T = tabuleiro_preenche_posicao(T, C, 2)
C = cria_coordenada(1, 4)
T = tabuleiro_preenche_posicao(T, C, 2)
escreve_tabuleiro(T)
J = pede_jogada()
S
T = tabuleiro_reduz(T, J)
C = cria_coordenada(1, 4)
T = tabuleiro_preenche_posicao(T, C, 2)
escreve_tabuleiro(T)