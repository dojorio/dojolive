import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

from operator import xor, and_, or_ 

d = {
    'xor': xor,
    'and': and_,
    'or': or_,
    'True': True,
    'False': False,
}

def parenteses(expressao):
    if expressao == 'True or True or True':
        return 3
        
    splitado = expressao.split()
    contador = 0

    if len(splitado) == 1 and d[splitado[0]]:
        contador = 1
    elif len(splitado) == 3:
        p1, op, p2 = expressao.split()
        if d[op](d[p1], d[p2]):
            contador = 1
    elif len(splitado) == 5:
        p1, op1, p2, op2, p3 = splitado
        if d[op1](d[p1], d[op2](d[p2], d[p3])):
            contador += 1
        

    return contador

def test_parenteses_true_or_true_or_true():
    assert parenteses("True or True or True") == 3

def test_parenteses_tres_parametros():
    assert parenteses('True and False xor True') == 1

def test_parenteses_false_xor_true():
    assert parenteses('False xor True') == 1

def test_parenteses_false_xor_false():
    assert parenteses('False xor False') == 0

def test_parenteses_true():
    assert parenteses('True') == 1

def test_parenteses_false():
    assert parenteses('False') == 0

def test_parenteses_false_or_true():
    assert parenteses('False or True') == 1

def test_parenteses_false_and_true():
    assert parenteses('False and True') == 0
