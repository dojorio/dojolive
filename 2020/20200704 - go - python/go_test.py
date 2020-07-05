# https://pt.wikipedia.org/wiki/Go

import pytest, numpy
pytest.main([__file__, '-v', '-p', 'no:warnings'])

def nas_linhas(tabuleiro, jogador, jogada):
    for n, linha in enumerate(tabuleiro):
        ultima_casa = None
        for casa, peça in enumerate(linha):
            if peça == jogador:
                if ultima_casa is not None:
                    for casa_anterior in range(ultima_casa, casa):
                        linha[casa_anterior] = jogador
                ultima_casa = casa
    return tabuleiro

def go(tabuleiro, jogador, jogada):
    linha, coluna = jogada
    tabuleiro[linha][coluna] = jogador

    tabuleiro = nas_linhas(tabuleiro, jogador, jogada)

    tabuleiro = numpy.transpose(tabuleiro)

    tabuleiro = nas_linhas(tabuleiro, jogador, jogada)

    tabuleiro = numpy.transpose(tabuleiro)          
    return tabuleiro.tolist()

def test_coloca_peça_1():
    assert go([[0, 0, 0]], 1, (0, 1)) == [[0, 1, 0]]

def test_coloca_peça_1_2d():
    tabuleiro = [
        [0, 0],
        [0, 0],
    ]
    assert go(tabuleiro, 1, (0, 1)) == [
        [0, 1],
        [0, 0],
    ]

def test_1_captura_2_2d():
    tabuleiro = [
        [0, 0, 0],
        [1, 2, 0],
        [0, 0, 0],
    ]
    assert go(tabuleiro, 1, (1, 2)) == [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]

def test_1_captura_2_2d_3_linhas():
    tabuleiro = [
        [1, 0, 0],
        [1, 2, 0],
        [1, 0, 0],
    ]
    assert go(tabuleiro, 1, (1, 2)) == [
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 0],
    ]

def test_1_captura_2_2d_3_linhas_com_2_na_vizinhanca():
    tabuleiro = [
        [2, 0, 0],
        [1, 2, 0],
        [2, 0, 0],
    ]
    assert go(tabuleiro, 1, (1, 2)) == [
        [2, 0, 0],
        [1, 1, 1],
        [2, 0, 0],
    ]

def test_coloca_peça_2():
    assert go([[0, 0, 0]], 2, (0, 1)) == [[0, 2, 0]]

def test_1_captura_2():
    assert go([[1, 2, 0]], 1, (0, 2)) == [[1, 1, 1]]

def test_2_captura_2():
    assert go([[2, 1, 0]], 2, (0, 2)) == [[2, 2, 2]]

def test_1_captura_2_tabuleiro_maior():
    assert go([[1, 2, 0, 0]], 1, (0, 2)) == [[1, 1, 1, 0]]

def test_1_captura_3_tabuleiro_maior():
    assert go([[0, 1, 2, 0]], 1, (0, 3)) == [[0, 1, 1, 1]]

def test_coloca_peça_mas_não_captura():
    assert go([[0, 2, 0, 0]], 1, (0, 2)) == [[0, 2, 1, 0]]

def test_1_captura_2_2d_vertical():
    tabuleiro = [
        [0, 1, 0],
        [0, 2, 0],
        [0, 0, 0],
    ]
    assert go(tabuleiro, 1, (2, 1)) == [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]

def test_1_captura_2_2d_horizontal_e_vertical():
    tabuleiro = [
        [1, 2, 0],
        [0, 2, 2],
        [0, 0, 1],
    ]
    assert go(tabuleiro, 1, (0, 2)) == [
        [1, 1, 1],
        [0, 2, 1],
        [0, 0, 1],
    ]
