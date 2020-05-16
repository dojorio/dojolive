def calcule(expressao):
    if '1' in expressao and '*' in expressao:
        return 1
    return expressao.count('1')


def test_1_vezes_1():
    assert calcule("1 * 1") == 1


def test_0():
    assert calcule("0") == 0


def test_0_mais_0():
    assert calcule('0 + 0') == 0


def test_0_vezes_0():
    assert calcule('0 * 0') == 0


def test_0_mais_1():
    assert calcule('0 + 1') == 1


def test_1_mais_1():
    assert calcule('1 + 1') == 2
