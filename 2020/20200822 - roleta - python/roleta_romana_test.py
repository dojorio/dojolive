# http://dojopuzzles.com/problemas/exibe/roleta-romana/

# Mantenha o seu cursor aqui: |
import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])


def roleta(numero_de_pessoas, inicio, passo):
    inicio -= 1
    pessoas = list(range(1, numero_de_pessoas+1))

    while len(pessoas) > 1:
        inicio = (inicio + passo - 1) % len(pessoas)
        pessoas.pop(inicio)
    return pessoas[0]

def test_10_2_3():
    # 1234567890
    # 123_56_89_
    # 12__56__9_
    # 1___56____
    # 1___5_____
    # ____5_____
    # 4 7 10 3  
    assert roleta(10, 2, 3) == 5

def test_6_1_2():
    # 2 4 6 3 1 5
    assert roleta(6, 1, 2) == 5

def test_4_1_2():
    # 2 4 3
    assert roleta(4, 1, 2) == 1

def test_3_1_2():
    # 2 1 3
    assert roleta(3, 1, 2) == 3


def test_2_1_2():
    # 2
    assert roleta(2, 1, 2) == 1

def test_1_1_2():
    assert roleta(1, 1, 2) == 1

def test_5_1_2():
    # 2 4 1 5 3
    assert roleta(5, 1, 2) == 3
