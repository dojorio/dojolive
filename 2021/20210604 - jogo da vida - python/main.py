import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

#     Qualquer célula viva com menos que duas células vivas vizinhas morre, por baixa população;
#     Qualquer célula viva com mais que três células vivas vizinhas morre, por alta população;
#     Qualquer célula viva com duas ou três células vivas vizinhas permanece viva para a próxima geração;
#     Qualquer célula morta com exatamente três células vivas vizinhas se transforma em uma célula viva;

def jogo_da_vida(situacao):
    conta = 0
    for linha in situacao:
        for celula in linha:
            conta += celula
            
    celula_do_meio = situacao[1][1]
    return conta == 3 or (conta == 4 and celula_do_meio)

def test_celula_canto_norte_recussita_com_3_vizinhas():
    situacao = (
        (1, 1, 0),
        (1, 0, 0),
        (0, 0, 0)
    )
    assert jogo_da_vida(situacao)

def test_celula_canto_sudeste_recussita_com_3_vizinhas():
    situacao = (
        (1, 1, 0),
        (1, 0, 0),
        (0, 0, 0)
    )
    assert jogo_da_vida(situacao)

def test_celula_canto_noroeste_recussita_com_3_vizinhas():
    situacao = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1)
    )
    assert jogo_da_vida(situacao)

def test_celula_nao_recussita_com_5_vizinhas():
    situacao = (
        (1, 1, 1),
        (1, 0, 1),
        (0, 0, 0)
    )
    assert not jogo_da_vida(situacao)

def test_celula_nao_recussita_com_4_vizinhas():
    situacao = (
        (1, 1, 1),
        (0, 0, 1),
        (0, 0, 0)
    )
    assert not jogo_da_vida(situacao)

def test_celula_recussita_com_3_vizinhas():
    situacao = (
        (1, 1, 1),
        (0, 0, 0),
        (0, 0, 0)
    )
    assert jogo_da_vida(situacao)

def test_celular_morre_com_quatro_vizinhas():
    situacao = (
        (1, 1, 1),
        (0, 1, 0),
        (0, 0, 1)
    )
    assert not jogo_da_vida(situacao)

def test_celula_morre_com_uma_adjacente():
    situacao = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 0)
    )
    assert not jogo_da_vida(situacao)

def test_celula_permanece_viva_com_3_adjacentes():
    situacao = (
        (0, 1, 0),
        (0, 1, 0),
        (0, 1, 1)
    )
    assert jogo_da_vida(situacao)

def test_celula_permanece_viva():
    situacao = (
        (1, 1, 0),
        (0, 1, 0),
        (0, 0, 0)
    )
    assert jogo_da_vida(situacao)

def test_celula_sozinha_morre():
    situacao = (
        (0, 0, 0),
        (0, 1, 0),
        (0, 0, 0)
    )
    assert not jogo_da_vida(situacao)