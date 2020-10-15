# Mantenha o seu cursor aqui: |

import pytest

from pessoa_fisica import salario

FATOR_R = 0.28
SALARIO_MINIMO = 1045
ANEXO_III = 0.06
ANEXO_V = 0.155

def calcula_retirada_liquida(faturamento, percentual_prolabore=0.28):
    percentual_das = ANEXO_III if percentual_prolabore >= FATOR_R else ANEXO_V

    prolabore = faturamento * percentual_prolabore if percentual_prolabore > 0 else SALARIO_MINIMO

    das = faturamento * percentual_das
    salario_liquido = salario(prolabore, socio=True)
    lucro = faturamento - prolabore - das
    return lucro + salario_liquido

@pytest.mark.parametrize("faturamento,percentual_prolabore,liquido", (
    (10000, 0.30, 9012.55),
    (10000, 0.20, 8230),
    (10000, 0, 8335.05),
    (10000, -1, 8335.05),
))
def test_percentuais_diferentes(faturamento, percentual_prolabore, liquido):
    assert calcula_retirada_liquida(
        faturamento, percentual_prolabore
    ) == liquido


@pytest.mark.parametrize("faturamento,liquido", (
    (15000, 13432.1),
    (10000, 9047.90),
    (6500, 5909.8),
    (5000, 4546),
))
def test_retirada_liquida(faturamento, liquido):
    assert calcula_retirada_liquida(faturamento) == pytest.approx(liquido)


pytest.main([__file__,'-v', '-p', "no:warnings"])
