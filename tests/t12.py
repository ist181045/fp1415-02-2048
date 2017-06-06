## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                 TEST 12                                    ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Abstraction: coordinate and board -- #
T = cria_tabuleiro()
C1 = cria_coordenada(3, 2)
C2 = cria_coordenada(2, 3)
T = tabuleiro_preenche_posicao(T, C1, 2)
T = tabuleiro_preenche_posicao(T, C2, 4)
L = tabuleiro_posicoes_vazias(T)
coordenada_na_lista(C1, L)
coordenada_na_lista(C2, L)
coordenada_na_lista(cria_coordenada(1, 1), L)
# - (additional hidden tests) - #
T = cria_tabuleiro()
print(', '.join(str(coord) for coord in tabuleiro_posicoes_vazias(T)))
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 3), 8)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 1), 32)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 4), 256)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 3), 2048)
print(', '.join(str(coord) for coord in tabuleiro_posicoes_vazias(T)))
T = cria_tabuleiro()
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(1, 4), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(2, 3), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(3, 2), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 1), 2)
T = tabuleiro_preenche_posicao(T, cria_coordenada(4, 4), 2)
T = tabuleiro_reduz(T, 'E')
escreve_tabuleiro(T)
