# Coloque o seu cursor aqui: |
# https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Pascal

# 1
# 1 1
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 

import pytest
from textwrap import dedent
pytest.main([__file__, '-vv', '-p', 'no:warnings'])

def pascal(numero_de_linhas):

    n = numero_de_linhas
    triangulo = []

    for y in range(n):
        linha = []
        for x in range(y+1):
            if x == 0 or x == y:
                linha.append(1)
            else:
                linha.append(triangulo[y-1][x-1] + triangulo[y-1][x])
  
        triangulo.append(linha)

    return triangulo

def test_pascal():
    assert pascal(1) == [[1]]

def test_pascal_duas_linhas():
    assert pascal(2) == [[1], [1, 1]]

def test_pascal_tres_linhas():
    assert pascal(3) == [[1], [1, 1], [1, 2, 1]]

def test_pascal_quatro_linhas():
    assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

def test_pascal_cinco_linhas():
    assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def test_pascal_seis_linhas():
    assert pascal(6) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

def test_pascal_sete_linhas():
    assert pascal(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]


def triangulo(numero_de_linhas):
    triangulo_em_listas = pascal(numero_de_linhas)

    s = ""
    ultima_linha = triangulo_em_listas[-1]
    tam_linha = len('   '.join(str(x) for x in ultima_linha))

    for i, linha in enumerate(triangulo_em_listas):
        if i > 0:
            s += "\n"            
        linha_print = '   '.join(str(x) for x in linha)
        s += linha_print.center(tam_linha)
    return s


def test_imprime_triangulo():
    assert triangulo(1) == "1"

def test_imprime_triangulo_duas_linhas():
    assert triangulo(2) == (
        "  1  \n"
        "1   1"
    )