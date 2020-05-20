import pytest


NOTAS = [1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0]

def atm(valor):
    resultado = {}
    for nota in NOTAS[::-1]:
        if quantidade_de_notas := valor // nota > 0:
            resultado[nota] = quantidade_de_notas
            valor -= resultado[nota] * nota

    return resultado

@pytest.mark.parametrize(
    "valor,notas",
    (
        (1.0, {1.0: 1}),
        (5.00, {5.00: 1}),
        (20.0, {20.00: 1}),
        (3.0, {2.00: 1, 1.00: 1}),
        (4.0, {2.00: 2}),
    ),
)
def test_atm(valor, notas):
    assert atm(valor) == notas
