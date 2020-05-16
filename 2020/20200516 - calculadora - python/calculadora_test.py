def calcule(expressao):
    if '1' in expressao:
        return 1
    return 0


assert calcule("0") == 0
assert calcule('0 + 0') == 0
assert calcule('0 * 0') == 0
assert calcule('0 + 1') == 1
assert calcule('1 + 1') == 2
