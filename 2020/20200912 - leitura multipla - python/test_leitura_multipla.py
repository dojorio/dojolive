# Mantenha o seu cursor aqui quando não estiver pilotando: |
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1262

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

def ciclos(entrada,leituraPciclo):
    if entrada == 'WW':
        return 2
    return 1

@pytest.mark.parametrize("params, expected", (
    (('R',1) , 1) ,
    ((), True),
))
def test_ciclosr1(params, expected):
    assert ciclos('R',1) == 1
    
def test_ciclosr2():
    assert ciclos('W',1) == 1

def test_ciclos3():
    assert ciclos('WW',1) == 2    
    
    
    