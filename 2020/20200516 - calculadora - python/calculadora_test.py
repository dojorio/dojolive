import pytest
import operator


def calcule(expressao):
    if ' ' not in expressao.strip():
        return int(expressao)

    expressao = expressao.replace(" ", "")

    for op, f in [
        ('+', operator.add),
        ('**', operator.pow),
        ('*', operator.mul),
        ('-', operator.sub),
    ]:
        if op in expressao:
            operando1, operando2 = expressao.split(op)
            return f(int(operando1), int(operando2))


@pytest.mark.parametrize('expressao,resultado', [
    # nenhum operador
    ("0", 0),
    ("4", 4),
    ('10', 10),
    ('100', 100),
    ('100 ', 100),

    # um operador
    ('0 + 0', 0),
    ('0 + 1', 1),
    ('1 + 1', 0b10),
    ('1 + 2', 3),
    ('10 + 2', 12),
    ('10 + 20', 30),

    ('0 * 0', 0),
    ("1 * 1", 1),
    ("1 * 2", 2),
    ("5 * 2", 10),
    ("50 * 2", 100),

    ("5 - 2", 3),
    ("50 - 2", 48),

    ("5 ** 2", 25),

    ("50 - 120 * 3", -310),

    # ("(50 - 120) * 3", -210),
])
def test_calcule(expressao, resultado):
    assert calcule(expressao) == resultado
