# Mantenha o seu cursor aqui quando não estiver pilotando: |

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])


def area(predios):
    if len(predios) == 1:
        return predios[0]

    resultados = []
    for posicao, valor in enumerate(predios):
        if posicao == 0:
            continue
        max1 = max(predios[0:posicao])
        max2 = max(predios[posicao:])
        res1 = max1*posicao
        res2 = max2*(len(predios)-posicao)
        resultados.append(res1+res2)
    return min(resultados)


@pytest.mark.parametrize("predios, resultado", (
    ([1, 1, 7, 6, 6, 6], 30),
    ([1, 2, 5, 3, 5], 19),
    ([5, 3, 5, 2, 1], 19),
    ([7, 7, 3, 7, 7], 35),
    ([5, 3, 2, 4], 17),
    ([2,4,1], 9),
    ([1], 1),
    ([5], 5),
    ([1,1], 2),
    ([3,1], 4),
    ([3,1,4], 10),
    ([3,1,5], 11),
    ([4,1,3], 10),
    ([4,3,1], 9),
    ([4,2,1], 8),
))
def test_area(predios, resultado):
    assert area(predios) == resultado
