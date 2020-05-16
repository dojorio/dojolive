import pytest
import operator


def calcule(expressao):
    expressao = expressao.replace(" ", "")
    expressao = expressao.replace('**', '^')

    for op, f in [
        ('-', operator.sub),
        ('+', operator.add),
        ('*', operator.mul),
        ('^', operator.pow),
    ]:
        if op in expressao:
            expressao1, expressao2 = expressao.split(op, 1)
            return f(calcule(expressao1), calcule(expressao2))

    return int(expressao)


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
    ("200 * 2 * 3", 1200),
    ("200 * 2 * 3 * 4", 4800),
    ("200 + 2 * 3 + 4", 210),

    ("200 * 2 ** 3 + 4", 1604),

    ("(200 + 2) * 3 + 4", 0),

    # ("(50 - 120) * 3", -210),
])
def test_calcule(expressao, resultado):
    assert calcule(expressao) == resultado
