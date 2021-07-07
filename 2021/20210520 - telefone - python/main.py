# Mantenha o seu cursor aqui quando não estiver pilotando: |

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

# código sob teste:
def palavra(texto):
    resposta = ''

    for letra in texto:
        resposta += teclado(letra)

    return resposta

def teclado(texto):
    if texto in '01-':
        return texto

    dicionario = [
        'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 
        'PQRS', 'TUV', 'WXYZ'
    ]

    for indice, letras in enumerate(dicionario):
        if texto in letras:
            return str(indice + 2)

# testes:
def test_muitas_letras():
    assert palavra('1-HOME-SWEET-HOME') == '1-4663-79338-4663'

def test_tres_letras():
    assert palavra('AAA') == '222'

def test_duas_letras():
    assert palavra('AA') == '22'

@pytest.mark.parametrize('letra', '01-')
def test_retorna_letra(letra):
    assert teclado(letra) == letra

@pytest.mark.parametrize('letra', 'WXYZ')
def test_vira_9(letra):
    assert teclado(letra) == '9'

@pytest.mark.parametrize('letra', 'TUV')
def test_vira_8(letra):
    assert teclado(letra) == '8'

@pytest.mark.parametrize('letra', 'PQRS')
def test_vira_7(letra):
    assert teclado(letra) == '7'

@pytest.mark.parametrize('letra', 'MNO')
def test_vira_6(letra):
    assert teclado(letra) == '6'

@pytest.mark.parametrize('letra', 'JKL')
def test_vira_5(letra):
    assert teclado(letra) == '5'

@pytest.mark.parametrize('letra', 'GHI')
def test_vira_4(letra):
    assert teclado(letra) == '4'

@pytest.mark.parametrize('letra', 'DEF')
def test_vira_3(letra):
    assert teclado(letra) == '3'

@pytest.mark.parametrize('letra', 'ABC')
def test_vira_2(letra):
    assert teclado(letra) == '2'


# Letras  ->  Número 
# ABC    ->  2 
# DEF    ->  3 
# GHI    ->  4 
# JKL    ->  5 
# MNO    ->  6 
# PQRS    ->  7 
# TUV    ->  8 
# WXYZ   ->  9 