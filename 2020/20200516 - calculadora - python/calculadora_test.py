import pytest

def calcule(expressao):
    if len(expressao) == 1:
        return int(expressao)

    expressao = expressao.replace(" ", "")
    operando1 = expressao[0]
    operador = expressao[1]
    operando2 = expressao[2]

    if operador == '+':
        return int(operando1) + int(operando2)
    elif operador == '*':
        return int(operando1) * int(operando2)
    elif operador == '-':
        return int(operando1) - int(operando2)


@pytest.mark.parametrize('expressao,resultado', [
    # nenhum operador
    ("0", 0),
    ("4", 4),
    # um operador
    ('0 + 0', 0),
    ('0 + 1', 1),
    ('1 + 1', 0b10),
    ('1 + 2', 3),

    ('0 * 0', 0),
    ("1 * 1", 1),
    ("1 * 2", 2),
    ("5 * 2", 10),

    ("5 - 2", 3),
])
def test_calcule(expressao, resultado):
    assert calcule(expressao) == resultado
