# Mantenha o seu cursor aqui quando não estiver pilotando: |

# Dez reais -> 10
# Onze reais -> 11
# Vinte e um -> 21

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

NUMEROS = {
    "mil": 1000.0,
    "seiscentos": 600.0,
    "quatrocentos": 400.0,
    "cem": 100.0,
    "cento": 100.0,
    "setenta": 70.0,
    "trinta": 30.0,
    "vinte": 20.0,
    "doze": 12.0,
    "um": 1.0,
    "dois": 2.0,
    "três": 3.0,
    "quatro": 4.0,
    "nove": 9.0,
    "oito": 8.00,
    "centavo": 0.01,
}

def conversor(extenso):
    resta = extenso.replace(' real', '').replace(' reais', '').replace(' e ', ' ')
    resta = resta.split(' ')
    valor_total = 0
    for n in resta:
        if n == "mil":
            if valor_total == 0:
                valor_total = 1
            valor_total *= 1000
        elif n in ('centavo','centavos'):
            valor_total *= 0.01
        else:
            valor_total += NUMEROS[n]
    return valor_total

@pytest.mark.parametrize('extenso, esperado', (
    ('um real', 1.0),
    ('dois reais', 2.0),
    ('três reais', 3.0),
    ('quatro reais', 4.0),
    ('vinte reais', 20.0),
    ('vinte e um reais', 21.0),
    ('setenta e nove reais', 79.0),
    ('quatrocentos reais', 400.0),
    ('cem reais', 100.0),
    ('cento e um reais', 101.0),
    ('seiscentos e trinta e oito reais', 638.0),
    ('mil reais', 1000.0),
    ('dois mil reais', 2000.0),
    ('mil seiscentos e trinta e oito reais', 1638.0),
    ('um centavo', 0.01),
    ('dois centavos', 0.02),
    ('um real e doze centavos', 1.12),
))
def test_conversor(extenso, esperado):
    assert conversor(extenso) == esperado
