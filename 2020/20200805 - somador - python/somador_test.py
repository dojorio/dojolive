import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

def somador(a, b):
    if b > 9:
        raise ValueError
    
    if a > 9:
        a0 = int(str(a)[-1])  # a unidade em a...
        a1 = int(str(a)[0])   # a dezena em a...       
        unidade_somada, dezena_somada = somador(a0, b)
        dezena, _ = somador(dezena_somada, a1)
        return unidade_somada, dezena
   
    paus = ''
    for pauzinho in range(a):
        paus = f'{paus}|'
    for pauzinho in range(b):
        paus = f'{paus}|'

    return len(paus)%10, len(paus)//10

@pytest.mark.parametrize("a, b, resultado", (
    (1, 1, (2, 0)),
    (0, 0, (0, 0)),
    (8, 1, (9, 0)),
    (7, 1, (8, 0)),
    (9, 1, (0, 1)),
    (9, 2, (1, 1)),
    (10, 1, (1, 1)),
    (18, 2, (0, 2)),
    (28, 3, (1, 3)),
    (3, 28, (1, 3)),
))
def test_somador(a, b, resultado):
    assert somador(a, b) == resultado


# somador(10) somador()

# s|s
# 1|0
# 0|1
# 1|1

# 2|1|0 
# 1|0|_
# s|s|s
# 0|5|0
# 0|5|0
# 1|0|0