# Mantenha o seu cursor aqui quando não estiver pilotando: |

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

NOTAS = {
    100: float('inf'),
    50: float('inf'),
    20: float('inf'),
    10: float('inf'),
}

def caixa_eletronico(valor_do_saque, notas_disponiveis=NOTAS):
    notas = {}

    for nota, qtde_disponivel in notas_disponiveis.items():
        if valor_do_saque >= nota:
            qtde_notas = valor_do_saque // nota
            if qtde_notas > qtde_disponivel:
                qtde_notas = qtde_disponivel
            valor_do_saque -= nota * qtde_notas
            notas[nota] = qtde_notas

    if valor_do_saque:
        return {}

    return notas

@pytest.mark.parametrize("valor_do_saque, notas_disponiveis, notas", (
    (10, {10: 1}, {10: 1}),
    (20, {10: 2}, {10: 2}),
    (40, {20: 1, 10: 3}, {20: 1, 10: 2}),
    (70, {10: 10}, {10: 7}),
    (80, {50: 2}, {}),
    (90, {50: 1}, {}),
    # (100, {100: 1}),
))
def test_caixa_eletronico_finito(valor_do_saque, notas_disponiveis, notas):
    assert caixa_eletronico(valor_do_saque, notas_disponiveis) == notas


@pytest.mark.parametrize("valor_do_saque, notas", (
    (10, {10: 1}),
    (20, {20: 1}),
    (30, {20: 1, 10: 1}),
    (40, {20: 2}),
    (70, {50: 1, 20: 1}),
    (80, {50: 1, 20: 1, 10: 1}),
    (90, {50: 1, 20: 2}),
    (100, {100: 1}),
))
def test_caixa_eletronico_infinito(valor_do_saque, notas):
    assert caixa_eletronico(valor_do_saque) == notas

