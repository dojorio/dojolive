# problema cheque por extenso

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

unidades = {
        0: 'zero',
        1: 'um', 
        2: 'dois',
        3: 'três',
        4: 'quatro',
        5: 'cinco', 
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove',
        10:'dez',
        11:'onze',
        12:'doze',
        13:'treze',
        14:'quatroze',
        15:'quinze',
        20: 'vinte',
        30: 'trinta',
        100: 'cem',
        200: 'duzentos',
    }

def mod(valor, div=10):
    resto = valor % div
    return (valor-resto, resto)

def por_extenso(valor):
    try:
        return unidades[valor]
    except KeyError:
        valor, resto = mod(valor)
        return unidades[valor] + ' e ' + unidades[resto]

@pytest.mark.parametrize('valor, extenso', (
    (0, 'zero'),
    (1, 'um'),
    (2, 'dois'),
    (3, 'três'),
    (4, 'quatro'),
    (5, 'cinco'),
    (6, 'seis'),
    (7, 'sete'),
    (8, 'oito'),
    (9, 'nove'),
    (10,'dez' ),
    (11,'onze'),
    (12,'doze'),
    (13,'treze'),
    (14,'quatroze'),
    (15,'quinze'),
    # ...
    (20,'vinte'),
    (21,'vinte e um'),
    (22,'vinte e dois'),
    (30,'trinta'),
    (31,'trinta e um'),
    (100,'cem'),
   # (121,'cento e vinte um'),
    (200,'duzentos'),
    (221,'duzentos e vinte um'),
))
def test_por_extenso(valor, extenso):
    assert por_extenso(valor) == extenso

@pytest.mark.parametrize('valor, valor_resto', (
    (21, (20, 1)),
))
def test_mod(valor, valor_resto):
    assert mod(valor) == valor_resto
