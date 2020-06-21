# https://pt.wikipedia.org/wiki/Blackjack

import pytest

pytest.main([__file__, '-v'])

valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipes = ['♠', '♥', '♦', '♣']

def pontuacao_de(mao):
    # mao = mao.copy()
    if mao == ['A', 'A']:
        return 12

    tem_a = ('A' in mao)
    if tem_a:
        mao.remove('A')
        tem_a = True
    print(mao)
    
    total = 0
    for carta in mao:        
        if carta in 'JQK':
            carta = 10
        total += int(carta)
    
    if tem_a:
        if total <= 10:
            total += 11
        else:
            total += 1
    
    return total if total <= 21 else 0


def blackjack(mao1, mao2):
    if pontuacao_de(mao1) > pontuacao_de(mao2):
        return "mao1"
    else:
        return "mao2"


@pytest.mark.parametrize(
    "mao, expected", (
        (['10', '9'], 19),
        (['J', '5'], 15),
        (['J', 'K'], 20),
        (['J', 'K', 'Q'], 0),
        (['2', 'A'], 13),
        (['10', 'A'], 21),
        (['J', 'A'], 21),
        (['A', 'A'], 12),
        (['A', '5', 'J'], 16),
    ))
def test_pontuacao_de(mao, expected):
    assert pontuacao_de(mao) == expected


def test_bug():
    assert pontuacao_de(['2', 'A']) == 13

def test_bug2():
    assert pontuacao_de(['10', 'A']) == 21

def test_bug3():
    assert pontuacao_de(['A', '5', 'J']) == 16

def test_2():
    assert blackjack(['2'], ['3']) == 'mao2'
    assert blackjack(['10'], ['9']) == 'mao1'
    assert blackjack(['10'], ['9', '2']) == 'mao2'
    assert blackjack(['10', '9'], ['3', '5']) == 'mao1'
    

