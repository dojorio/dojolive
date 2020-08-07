
import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

# aqui esta o codigo sob teste:

#          chave, valor'
#          key, value
valores = {
        0.0: '',
        50.0: 'cinquenta',
        1.0: 'um',
        2.0: 'dois',
        3.0: 'três',
        4.0: 'quatro',
        5.0: 'cinco',
        6.0: 'seis',
        7.0: 'sete',
        8.0: 'oito',
        9.0: 'nove',
        10.0: 'dez',
        11.0: 'onze',
        # 1.50: 'um e cinquenta',
        }

def por_extenso(valor):
    valor = str(valor)
    inteiro, centavos = valor.split('.')
    inteiro = valores[float(inteiro)]
    centavos = float(centavos)*10
    moeda = ' reais'
    if inteiro == 'um':
        moeda = ' real'
    if centavos:
        return inteiro + moeda + ' e ' + valores[centavos] + ' centavos'
    
    return inteiro + moeda


# aqui estao os testes:
@pytest.mark.parametrize('valor, extenso', (
    (0.50, 'cinquenta centavos'),
    (1.0, 'um real'),
    (2.0, 'dois reais'),
    (3.0, 'três reais'),
    (4.0, 'quatro reais'),
    (5.0, 'cinco reais'),
    (6.0, 'seis reais'), 
    (7.0, 'sete reais'),
    (8.0, 'oito reais'),
    (9.0, 'nove reais'),
    (10.0, 'dez reais'),
    (11.0, 'onze reais'),
    (1.50, 'um real e cinquenta centavos')
))

def test_por_extenso(valor, extenso):
    assert por_extenso(valor) == extenso
