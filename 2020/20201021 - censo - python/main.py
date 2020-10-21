# Mantenha o seu cursor aqui quando não estiver pilotando: |

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])


def ano_mais_denso(pessoas):
    maior_ano = max([pessoa['obito'] for pessoa in pessoas])
    anos = [0 for x in range(maior_ano + 1)]

    for pessoa in pessoas:
        for ano in range(pessoa['nascimento'], pessoa['obito'] + 1):
            anos[ano] += 1

    anos = list(reversed(anos))
    maior_valor = max(anos)
    return maior_ano - anos.index(maior_valor)


def test_caso_pra_quebrar():
    pessoas = [
        {"nascimento": 3000, "obito": 3010 },
        {"nascimento": 2990, "obito": 3005 },
    ]
    assert ano_mais_denso(pessoas) == 3005


def test_outro_com_tres_pessoas_sem_intercessao():
    pessoas = [
        {"nascimento": 1909, "obito": 1920 },
        {"nascimento": 1928, "obito": 1964 },
        {"nascimento": 1957, "obito": 1994 },
    ]
    assert ano_mais_denso(pessoas) == 1964


def test_outro_com_tres_pessoas():
    pessoas = [
        {"nascimento": 1929, "obito": 1957 },
        {"nascimento": 1928, "obito": 1964 },
        {"nascimento": 1957, "obito": 1994 },
    ]
    assert ano_mais_denso(pessoas) == 1957


def test_exemplo_com_tres_pessoas():
    pessoas = [
        {"nascimento": 1903, "obito": 1957 },
        {"nascimento": 1928, "obito": 1964 },
        {"nascimento": 1957, "obito": 1994 },
    ]
    assert ano_mais_denso(pessoas) == 1957


def test_com_duas_pessoas_com_intersecao():
    pessoas = [
        {"nascimento": 1903, "obito": 1957 },
        {"nascimento": 1928, "obito": 1964 },
    ]
    assert ano_mais_denso(pessoas) == 1957


def test_com_duas_pessoas_em_periodos_diferentes():
    pessoas = [
        {'nascimento': 1990, 'obito': 2089},
        {'nascimento': 1920, 'obito': 1980},
    ]
    assert ano_mais_denso(pessoas) == 2089


def test_com_duas_pessoas_reversed():
    pessoas = [
        {'nascimento': 1990, 'obito': 2089},
        {'nascimento': 1970, 'obito': 1990},
    ]
    assert ano_mais_denso(pessoas) == 1990


def test_com_duas_pessoas():
    pessoas = [
        {'nascimento': 1970, 'obito': 1990},
        {'nascimento': 1990, 'obito': 2089},
    ]
    assert ano_mais_denso(pessoas) == 1990


def test_com_uma_pessoa_anos_diferentes():
    pessoas = [{'nascimento': 1970, 'obito': 1990}]
    assert ano_mais_denso(pessoas) == 1990


def test_com_outra_pessoa():
    pessoas = [{'nascimento': 1970, 'obito': 1970}]
    assert ano_mais_denso(pessoas) == 1970


def test_com_uma_pessoa():
    pessoas = [{'nascimento': 1980, 'obito': 1980}]
    assert ano_mais_denso(pessoas) == 1980
