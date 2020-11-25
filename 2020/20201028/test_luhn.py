# Mantenha o seu cursor aqui quando não estiver pilotando: |

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])


def valida_numero(cartao):
    cartao = cartao.replace(' ', '')
    
    numeros = [(int(digito) * 2) % 9 for digito in cartao[::2]]
    numeros.extend([int(digito) for digito in cartao[1::2]])
    soma = sum(numeros)
    return soma % 10 == 0
    
    numeros = []
    for index, digito in enumerate(cartao):
        if index % 2 == 0:
            numeros.append((int(digito) * 2) % 9)
        else:
            numeros.append(int(digito))

    soma = sum(numeros)
    return soma % 10 == 0


def test_exemplo():
    assert valida_numero('4539 1488 0343 6467') is True


def test_dobrando_passando_de_nove():
    assert valida_numero('5900 0000 0000 0000') is True


def test_dobrando_de_novo():
    assert valida_numero('3400 0000 0000 0000') is True


def test_dobrando():
    assert valida_numero('2600 0000 0000 0000') is True

def test_com_mais_digitos_sem_dobrar():
    assert valida_numero('0902 0901 0901 0900') is True

def test_0901():
    assert valida_numero('0000 0000 0000 0901') is True


def test_0801():
    assert valida_numero('0000 0000 0000 0801') is False


def test_0000():
    assert valida_numero('0000 0000 0000 0000') is True


def test_final_0802():
    assert valida_numero('0000 0000 0000 0802') is True
