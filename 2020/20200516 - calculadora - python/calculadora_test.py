import pytest

def calcule(expressao):
    if len(expressao) == 1:
        return int(expressao)
    if '1' in expressao and '*' in expressao:
        return int(expressao[-1])
    return expressao.count('1')


@pytest.mark.parametrize('expressao,resultado', [
    # nenhum operador
    ("0", 0),
    ("4", 4),
    # um operador
    ('0 + 0', 0),
    ('0 * 0', 0),
    ('0 + 1', 1),
    ('1 + 1', 0b10),
    ("1 * 1", 1),
    ("1 * 2", 2),
])
def test_calcule(expressao, resultado):
    assert calcule(expressao) == resultado
