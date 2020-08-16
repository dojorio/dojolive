# Mantenha o seu cursor aqui quando não estiver pilotando: |

import pytest
from math import sqrt

pytest.main([__file__, '-v', '-p', 'no:warnings'])


# def verifica_se_e_primo(numero):
#     for n in range(2, int(sqrt(numero))+1):
#         if numero % n == 0:            
#             return False
#     return True


def fatores(numero):
    fatores = []

    for divisor in range(2, int(sqrt(numero))+1):
        while numero % divisor == 0:
            fatores.append(divisor)
            numero /= divisor

    if numero != 1:
        fatores.append(numero)

    return fatores


@pytest.mark.parametrize("numero,expected", (
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (6, [2, 3]),
    (8, [2, 2, 2]),
    (12, [2, 2, 3]),
    (16, [2, 2, 2, 2]),
    (18, [2, 3, 3]),
    (25, [5, 5]),
    (49, [7, 7]),
    (77, [7, 11]),
    (26, [2, 13]),
    (17, [17]),
    (1024, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
    (510510 ,[2,3,5,7,11,13,17])
))
def test_fatores(numero, expected):
    assert fatores(numero) == expected


# @pytest.mark.parametrize("numero,expected", (
#     (2, True),
#     (4, False),
#     (17, True),
# ))
# def test_primos(numero, expected):
#     assert verifica_se_e_primo(numero) == expected