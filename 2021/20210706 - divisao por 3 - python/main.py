# Mantenha o seu cursor aqui quando não estiver pilotando: |
from random import randint
from time import time

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

"dada uma sequencia de inteiros não negativos, mudando apenas uma posição de cada vez, quantas combinações divisíveis por 3 são produzidas"

def f51(seq):
    seq_int = [int(digito) for digito in seq]
    soma = sum(seq_int)

    len_seq = len(seq)
    total = 3 * len_seq
    for i, _ in enumerate(seq):
        if (soma - seq_int[i]) % 3 == 0:
            total += 1
            
    if soma % 3 == 0:
        total -= (len_seq - 1)
    
    return total


def f5(seq):
    seq_int = [int(digito) for digito in seq]
    soma = sum(seq_int)

    total = 3 * len(seq)
    for i, _ in enumerate(seq):
        if (soma - seq_int[i]) % 3 == 0:
            total += 1
            
    if soma % 3 == 0:
        total -= (len(seq) - 1)
    
    return total

def f4(seq):
    soma = sum([int(digito) for digito in seq])

    total = 3 * len(seq)
    for digito in seq:
        if (soma - int(digito)) % 3 == 0:
            total += 1
            
    if soma % 3 == 0:
        total -= (len(seq) - 1)
    
    return total

def f3(seq):
    seq = str(seq)
    resultado = 0
    posicao = 0
    while posicao < len(seq):
        numero = seq[:posicao] + '0' + seq[posicao+1:]

        n = int(numero)
        resultado += 4 if n % 3 == 0 else 3
        posicao += 1

    correcao = (posicao-1) if int(seq) % 3 == 0 else 0

    return resultado - correcao

def f(seq):
    resultado = 0
    for posicao, _ in enumerate(seq):
        lseq = list(seq)
        
        lseq[posicao] = '0'
        n = int(''.join(lseq))
        resultado += 4 if n % 3 == 0 else 3
    
    correcao = posicao if int(seq) % 3 == 0 else 0

    return resultado - correcao


def f2(seq):
    divisiveis = set()
    for posicao, _ in enumerate(seq):
        lseq = list(seq)
        
        for digito in range(10):
            lseq[posicao] = str(digito)
            n = int(''.join(lseq))
            if n % 3 == 0:
                divisiveis.add(n)
    
    return len(divisiveis)

def test_grande():
    assert f4('0'*1_000_000) == 3000001

def test_rand():
    for x in range(1000):
        seq = str(randint(0, 10000))
        expected = f4(seq)
        assert f(seq) == expected


def test_timing():
    numero = '0' * 1000000
    start = time()
    f5(numero)
    t1 = time() - start

    start = time()
    f51(numero)
    t2 = time() - start

    assert t1 == t2
    

# def test_grande():
#     assert f('0'*100) == 11 

def test_789():
    assert f('789') == f2('789')

def test_345():
    assert f('345') == f2('345')

def test_123():
    assert f('123') == f2('123')

def test_12():
    assert f('12') == 5

def test_0081():
    assert f('0081') == 11 

def test_vinte_e_tres():
    assert f('23') == 7 

def test_dois_digitos():
    assert f('00') == 7

def test_um_digito():
    assert f('0') == 4


# assert f('23') == 7
# assert f('0081') == 11

"""23:
20
21x
22
23
24x
25
26
27x
28
29

03x
13
23
33x
43
53
63x
73
83
93x
"""

"""
12

02
12x
22
32
42x
52
62
72x
82
92

10
11
12x
13
14
15x
16
17
18x
19
"""

""" exemplo do f4:
247 (soma 13)

digito 2
047 = 11
147 = 12x
247 = 13
347 = 14
447 = 15x
547 = 16
647 = 17
747 = 18x
847 = 19
947 = 20

digito 4
207 = 9x
217 = 10
227 = 11
237 = 12x
247 = 13
257 = 14
267 = 15x
277 = 16
287 = 17
297 = 18x

digito 7
240 = 6x
241 = 7
242 = 8
243 = 9x
244 = 10
245 = 11
246 = 12x
247 = 13
248 = 14
249 = 15x

13 - 2 = 11 (soma 3)
13 - 4 = 9 (soma 4)
13 - 7 = 6 (soma 4)
total = 11
"""

"""
1234 -> soma = 10

digito 1
0234 = 9x
1234 = 10
2234 = 11
3234 = 12x
4234 = 13
5234 = 14
6234 = 15x
7234 = 16
8234 = 17
9234 = 18x

digito 2
1034 = 8
1134 = 9x
1234 = 10
1334 = 11
1434 = 12x
1534 = 13
1634 = 14
1734 = 15
1834 = 16x
1934 = 17

digito 3
1204 = 7
1214 = 8
1224 = 9x
1234 = 10
1244 = 11
1254 = 12x
1264 = 13
1274 = 14
1284 = 15x
1294 = 16

digito 4
1230 = 6x
1231 = 7
1232 = 8
1233 = 9x
1234 = 10
1235 = 11
1236 = 12x
1237 = 13
1238 = 14
1239 = 15x
"""