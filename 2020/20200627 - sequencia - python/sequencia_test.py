import pytest
pytest.main([__file__, "-v"])


def grupamento(numeros):
    numero1 = numeros.pop(0)
    resposta = [numero1]
   
    while numeros:
        numero = numeros.pop(0)
        if numero1+1 == numero:
            numero1 = numero
        else:
            resposta.append(numero)
    return resposta


#     tam = len(numeros)
#         
#         if(tam > 1):
#         
#             if numeros[0] - numeros[1] == 1:
#                 numeros.pop(0)
#             else:
#                 resposta.append(numeros.pop(0))
#         else:
#             resposta.append(numeros.pop(0))
#     
#     return resposta
    
    
# def test_1():
#     assert grupamento ([1]) == [[1]]

# def test_2():
#     assert grupamento([1, 2]) == [[1, 2]]

# def test_3():
#     assert grupamento([1, 2, 4]) == [[1, 2], [4]]

# def test_4():
#     assert grupamento([1, 2, 4, 5]) == [[1, 2], [4, 5]]

def test_5():
    assert grupamento([1, 2, 3, 4, 5]) == [[1, 5]]

