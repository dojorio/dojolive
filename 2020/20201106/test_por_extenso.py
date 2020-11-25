# Mantenha o seu cursor aqui quando não estiver pilotando: |

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

NOMES = {
    1: "um",
    2: "dois",
    3: "tres",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",    
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "quatorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezessete",
    18: "dezoito",
    19: "dezenove",
    20: "vinte",
    30: "trinta",
    40: "quarenta",
    50: "cinquenta",
    60: "sessenta",
    70: "setenta",
    80: "oitenta",
    90: "noventa",
    100: 'cem',
    300: 'trezentos',
    500: 'quinhentos',
    900: 'novecentos',
}

def por_extenso(valor):
    moeda = "real" if valor == 1 else "reais"

    try:
        valor_extenso = NOMES[valor]
    except KeyError:
        dezena = valor // 10 * 10
        unidade = valor - dezena

        valor_extenso = f'{NOMES[dezena]} e {NOMES[unidade]}'
    
    return f"{valor_extenso} {moeda}"

def test_cento_e_um():
    assert por_extenso(101.0) == 'cento e um reais'

@pytest.mark.parametrize(
    "valor, extenso",
    (
        (100.0, "cem"),
        (300.0, "trezentos"),
        (500.0, "quinhentos"),
        (900.0, "novecentos"),
    )
)
def test_so_centenas(valor, extenso):
    assert por_extenso(valor) == f"{extenso} reais"

@pytest.mark.parametrize(
    "valor, extenso",
    (
        (41.0, "quarenta e um"),
        (67.0, "sessenta e sete"),
        (99.0, "noventa e nove"),
    )
)
def test_dezena_e_unidade(valor, extenso):
    assert por_extenso(valor) == f"{extenso} reais"


@pytest.mark.parametrize(
    "valor, extenso",
    (
        (30.0, "trinta"),
        (50.0, "cinquenta"),
        (80.0, "oitenta"),
    )
)
def test_so_dezenas(valor, extenso):
    assert por_extenso(valor) == f"{extenso} reais"

@pytest.mark.parametrize(
    "valor, extenso",
    (
        (2.0, "dois"),
        (3.0, "tres"),
        (5.0, "cinco"),
        (8.0, "oito"),
        (13.0, "treze"),
        (17.0, "dezessete"),
    )
)
def test_sub_20(valor, extenso):
    assert por_extenso(valor) == f"{extenso} reais"

def test_1():
    assert por_extenso(1.0) == "um real"
