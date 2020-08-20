 
# Mantenha o seu cursor aqui quando não estiver pilotando >>>> |
# http://dojopuzzles.com/problemas/exibe/partida-de-tenis/

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

# estados = [ 0 , 15, 30, 40 , 'venceu']
# estados-deuce = [ 'deuce' , 'vantagem' ,  'venceu'] 
# jogador1 = 0
# jogador2 = 0
# placar = [jogador1, jogador2]

def calculadora(ponto):   
    if ponto == 30:
        return 40  
    if ponto == 40:
        return "game"
    if  ponto == "vantagem":
        return  "game"
    return ponto + 15

def placar(sacador, receptor, sacador_acertou):
    deuce = sacador == receptor == 40
    if sacador == "vantagem" and not sacador_acertou:
        return (40, 40)

    if receptor == "vantagem" and sacador_acertou:
        return (40, 40)
        
    if deuce:
        if sacador_acertou:
            sacador = 'vantagem'
        else:
            receptor = 'vantagem'
        return (sacador, receptor)    

    if sacador_acertou:
        return (calculadora(sacador), receptor)
    return (sacador, calculadora(receptor))

def test_zero():
    assert calculadora(0) == 15

def test_quinze():
    assert calculadora(15) == 30

def test_trinta():
    assert calculadora(30) == 40

def test_calculadora_venceu():
    assert calculadora(40) == "game"

# @pytest.mark.parametrize(
def teste_placar_0_0_true():
    assert placar(0, 0, True) == (15, 0)

def teste_placar_15_0_true():
    assert placar(15, 0, True) == (30, 0)
    
def teste_placar_30_0_false():
    assert placar(30, 0, False) == (30, 15)
    
def teste_placar_30_15_false():
    assert placar(30, 15, False) == (30, 30)

def teste_placar_30_30_true():
    assert placar(30, 30, True) == (40, 30)

def teste_placar_40_30_true():
    assert placar(40, 30, True) == ("game", 30)

def teste_placar_40_30_false():
    assert placar(40, 30, False) == (40, 40)

def teste_placar_40_40_false():
    assert placar(40, 40, False) == (40, "vantagem")

def teste_placar_40_40_true():
    assert placar(40, 40, True) == ("vantagem", 40)

def teste_placar_vantagem_40_true():
    assert placar('vantagem', 40, True) == ("game", 40)

def teste_placar_vantagem_40_False():
    assert placar('vantagem', 40, False) == (40, 40)

def teste_placar_40_vantagem_False():
    assert placar(40, 'vantagem', False) == (40, "game")

def teste_placar_40_vantagem_True():
    assert placar(40, 'vantagem', True) == (40, 40)
