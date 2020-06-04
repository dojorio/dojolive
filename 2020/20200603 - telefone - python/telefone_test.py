# http://dojopuzzles.com/problemas/exibe/encontre-o-telefone/
# https://repl.it/join/nuaknpij-chicolucio

import pytest

'''
ABC    ->  2 
DEF    ->  3 
GHI    ->  4 
JKL    ->  5 
MNO    ->  6 
PQRS   ->  7 
TUV    ->  8 
WXYZ   ->  9 
'''


def teclado(teclas):
    telefone = ""
    for tecla in teclas:
        if tecla == "Z":
            tecla = "X"

        if tecla >= "S":
            subtrair = 66
        elif tecla >= "A":
            subtrair = 65
        else:
            telefone += tecla
            continue

        telefone += str((ord(tecla) - subtrair) // 3 + 2)

    return telefone


@pytest.mark.parametrize(
    "teclas,expected",
    (
            ("A", "2"),
            ("AA", "22"),
            ("AAA", "222"),
            ("BB", "22"),
            ("C", "2"),
            ("D", "3"),
            ("ABC", "222"),
            ("EBC", "322"),
            ("EFG", "334"),
            ("1-AB", "1-22"),
            ("1-SS", "1-77"),
            ("1-ST", "1-78"),
            ("1-ZZ", "1-99"),
            ("1-XX", "1-99"),
            ("1-V", "1-8"),
            ("1-DOJO-RIO", "1-3656-746"),
    )
)
def test_teclado(teclas, expected):
    assert teclado(teclas) == expected


pytest.main([__file__, "-v"])
