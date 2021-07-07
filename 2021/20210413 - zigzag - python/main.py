import pytest

pytest.main([__file__, '-v', '-p', 'no:warnings'])


def zigzag(lista):
    quantidade = 0

    #for x, y, z in zip(lista, lista[1:], lista[2:]):
    for indice in range(len(lista) - 2):
        x, y, z = lista[indice], lista[indice + 1], lista[indice + 2]
        quantidade +=  x < y > z or x > y < z
    return quantidade


def test_0_0_0_1_0():
    assert zigzag([0, 0, 0, 1, 0]) == 1

def test_neg1_2_1():
    assert zigzag([-1, 2, 1]) == 1

def test_0_0_0():
    assert zigzag([0, 0, 0]) == 0
   
def test_1_2_1_2_1_2():
    assert zigzag([1, 2, 1, 2, 1, 2]) == 4

def test_1_2_1_2_1():
    assert zigzag([1, 2, 1, 2, 1]) == 3

def test_1_2_1_0_0():
    assert zigzag([1, 2, 1, 0, 0]) == 1

def test_1_2_1_2_2():
    assert zigzag([1, 2, 1, 2, 2]) == 2

def test_1_2_1_0():
    assert zigzag([1, 2, 1, 0]) == 1

def test_3_2_1():
    assert zigzag([3, 2, 1]) == 0

def test_1_2_1():
    assert zigzag([1, 2, 1]) == 1

def test_2_5_3():
    assert zigzag([2, 5, 3]) == 1

def test_2_5_6():
    assert zigzag([2, 5, 6]) == 0

def test_2_5_7():
    assert zigzag([2, 5, 7]) == 0

def test_6_5_7():
    assert zigzag([6, 5, 7]) == 1
