# Mantenha o seu cursor aqui: |

"""

IRPF:
Base de cálculo      | Alíquota | Dedução
Até 1.903,98         | Isento   | Isento
1.903,99-2.826,65    | 7,5      | 142,80
De 2.826,66-3.751,05 | 15       | 354,80
De 3.751,06-4.664,68 | 22,5     | 636,13
Acima de 4.664,68    | 27,5     | 869,36

INSS:
Até 1045        | 7,5% | -
1045,01-2089,60 | 9%   | 15,67
2089,61-3134,40 | 12%  | 78,36
3134,41-6101,06 | 14%  | 141,05  

"""
import pytest
pytest.main([__file__,'-v', '-p', "no:warnings"])

def calculo_inss(salario_bruto):
    teto = 6101.06
    tabela = {
        1045: (0.075, 0),
        2089.6: (0.09, 15.67),
        3134.4: (0.12, 78.36),
        teto: (0.14, 141.05)
    }
    if salario_bruto >= teto:
        salario_bruto = teto

    for limite, aliquota in tabela.items():
        if salario_bruto <= limite:
            aliquota_inss, deducao = aliquota
            break

    return round(salario_bruto * aliquota_inss - deducao, 2)

def calculo_irpf(salario_base):
    tabela = {
        4664.68: (0.275, 869.36),
        3751.05: (0.225, 636.13),
        2826.65: (0.15, 354.8),
        1903.98: (0.075, 142.8),
        0: (0, 0),
    }
        

    for limite, valores in tabela.items():
        if salario_base >= limite:
            aliquota_irpf, deducao = valores
            break

    return round(salario_base * aliquota_irpf - deducao, 2)
    

def salario(salario_bruto):
    
    salario_base = salario_bruto - calculo_inss(salario_bruto)

    return (
        salario_base -
        calculo_irpf(salario_base)
    )

# Testes inss
@pytest.mark.parametrize("salario, inss", (
    (1044, 78.3),
    (2000, 164.33),
    (2080, 171.53),
    (2100, 173.64),
    (3134.4, 297.77),
    (6101.06, 713.1),
    (7000, 713.1),
))
def teste_inss(salario, inss):
    assert calculo_inss(salario) == inss

@pytest.mark.parametrize("salario, irpf", (
    (1000, 0),
    (2826.65, 69.20),
    (5000 , 505.64)
))
def test_irpf(salario, irpf):
    assert calculo_irpf(salario) == irpf

@pytest.mark.parametrize("salario_bruto, salario_liquido", (
    (1000, 925),
    (900, 832.5),
    (950, 878.75),
    (1046, 967.53),
    # acima de 1903.98
    (2000, 1835.67),
    (2089.60, 1916.22),
    (8000.60, 6152.80)
))
def teste_salario(salario_bruto, salario_liquido):
    assert salario(salario_bruto) == salario_liquido