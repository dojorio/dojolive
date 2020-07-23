# Mantenha o seu cursor aqui: |

import pytest
import operator
pytest.main([__file__, '-v', '-p', 'no:warnings'])

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def polonesa(expressao):
    tokens = expressao.split(" ")
    pilha = []

    for token in tokens:
        try:
            pilha.append(int(token))
        except ValueError:
            operando2 = pilha.pop()
            operando1 = pilha.pop()

            pilha.append(OPS[token](operando1, operando2))
                
    return pilha[0]

@pytest.mark.parametrize('expressao, resultado', (
    ('1', 1),
    ('0', 0),
    ('0 0 +', 0),
    ('1 0 +', 1),
    ('1 0 3 + +', 4),
    ('1 1 2 + +', 4),
    ('1 1 -', 0),
    ('2 1 -', 1),
    ('1 2 -', -1),
    ('1 1 2 - -', 2),
    ('1 1 2 - +', 0),
    ('-1 -1 0 - +', -2),
    ('-1 -1 0 - -', 0),
    ('-1 -1 0 -2 + - -', -2),
    ('4 5 *', 20),
    ('4 5 2 * *', 40),
    ('4 2 /', 2),
    ('4 8 /', 0.5),
    ('4 8 / 5 +', 5.5),
))
def test_expressao(expressao, resultado):
    assert polonesa(expressao) == resultado

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        assert polonesa('0 0 /')
