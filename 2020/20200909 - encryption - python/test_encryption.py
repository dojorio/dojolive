# Mantenha o seu cursor aqui quando não estiver pilotando: |
#https://www.urionlinejudge.com.br/judge/en/problems/view/1024

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])


def transforma(letra, valor, regra=True):
    if regra:
        return chr(ord(letra) + valor)
    return letra


def desloca_1(texto):
    return ''.join(
        transforma(letra, 3, letra.isalpha())
        for letra in texto
    )


def inverte(texto):
    return texto[::-1]


def desloca_2(texto):
    metade = len(texto) // 2

    novo_texto = texto[:metade]
    for letra in texto[metade:]:
        novo_texto += transforma(letra, -1)

    return novo_texto


def criptografar(texto):
    return desloca_2(inverte(desloca_1(texto)))


@pytest.mark.parametrize("params, expected", (
    ('abc', 'aab'),
    ('abcd1', 'abbc0'),
    ('abcd', 'abbc')

))
def test_desloca_2(params, expected):
    assert desloca_2(params) == expected


@pytest.mark.parametrize("params, expected", (
    ('abc', 'cba'),
    ('abcd1', '1dcba')
))
def test_inverte(params, expected):
    assert inverte(params) == expected


@pytest.mark.parametrize("params, expected", (
    ('abc', 'def'),
    ('abcd1', 'defg1'),
))
def test_desloca_1(params, expected):
    assert desloca_1(params) == expected


@pytest.mark.parametrize("params, expected", (
    ('a', 'c'),
    ('y', '{'),
    ('b', 'd'),
    ('#', '"'),
    ('@', '?'),
    ('2', '1'),
    ('A', 'C'),
    ('ab', 'ec'),
    ('cd', 'ge'),
    ('abc', 'fdc'),
    ('Texto #3', '3# rvzgV'),
    ('vv.xwfxo.fd', 'gi.r{hyz-xx'),

))
def test_criptografar(params, expected):
    assert criptografar(params) == expected
