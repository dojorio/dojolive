import pytest
pytest.main([__file__, "-v"])

def grupamento(numeros):

    list_len = len(numeros) - 1

    grupos =[]
    grupo = []

    for i, numero in enumerate(numeros):
        if not grupo:
            grupo.append(numero)
            continue
        if i == list_len:
            if (numero - numeros[i-1]) == 1:
                grupo.append(numero)
                continue
            else:
                grupo.append(numeros[i-1])
                grupos.append(grupo)
                grupos.append([numero])
                grupo=[]
                continue
  
        if (numero - numeros[i-1]) == 1:
            continue
        else:
            if numeros[i-1] not in grupo:
                grupo.append(numeros[i-1])
            grupos.append(grupo)
            grupo = []
            grupo.append(numero)          
          
    if grupo:
        grupos.append(grupo)
    
    return grupos


def test_1():
    assert grupamento ([1]) == [[1]]

def test_2():
    assert grupamento([1, 2]) == [[1, 2]]

def test_3():
    assert grupamento([1, 2, 4]) == [[1, 2], [4]]

def test_4():
    assert grupamento([1, 2, 4, 5]) == [[1, 2], [4, 5]]

def test_5():
    assert grupamento([1, 2, 3, 4, 5]) == [[1, 5]]

def test_6():
    assert grupamento([1, 2, 4, 5, 7, 9, 10]) == [[1, 2], [4, 5], [7], [9,10]]

def test_7():
    assert grupamento([100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]) == [[100,105], [110,111], [113,115], [150]]


#assert grupamento(lista) == [100-103]
