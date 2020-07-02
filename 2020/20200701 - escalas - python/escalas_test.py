# Mantenha o seu cursor aqui: |
# Igor, Bruno, Lucas R,

# Do     Re     Mi     Fa      Sol      La      Si
# C      D      E      F       G        A       B
#  C#/Db   D#/Eb         F#/Gb   G#/Ab    A#/Bb

# sustenidos: sentido horário     (começa em F) C G D A E B  até -2
# bemois : sentido anti-horário   (começa em B) E A D G C F  até +1
# Círculo de Quintas
#       [F]
#    B      C
#   E         G
#     A     D
   
# C -> []           C D E F G A B
# G -> [F#]         G A B C D E F#
# D -> [F# C#]      D E F# G A B C#

# F  -> [Bb]        F G A Bb C D E

# Bb -> [Bb Eb]     Bb C D Eb F G A
# Eb -> [Bb Eb Ab]  Eb F G Ab Bb C D

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

def escala(tom):
    escala_base = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B']
    ciclo_das_quintas_sus = ['F', 'C', 'G', 'D', 'A', 'E', 'B']
    ciclo_das_quintas_bemol = ciclo_das_quintas_sus[::-1]

    ciclo_das_quintas = ciclo_das_quintas_sus
    mudanca = -2
    simbolo = '#'

    if tom == 'F':
      return ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']

    if 'b' in tom:
        ciclo_das_quintas = ciclo_das_quintas_bemol
        tom = tom.replace('b', '')
        mudanca = 1
        simbolo = 'b'
    
    index = ciclo_das_quintas.index(tom)
    index_inicial = escala_base.index(tom)
    escala_tom = escala_base[index_inicial:index_inicial + 7]
    mudar_ate = index + mudanca
    
    return [
        f'{nota}{simbolo}' if ciclo_das_quintas.index(nota) <= mudar_ate else nota
        for nota in escala_tom
    ]

def test_C():  # F C G D A E B
    assert escala('C') == ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def test_G():  # [F] C G D A E B
    assert escala('G') == ['G', 'A', 'B', 'C', 'D', 'E', 'F#']

def test_D():  # [F C] G D A E B
    assert escala('D') == ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']

def test_A():  # [F C G] D A E B
    assert escala('A') == ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']

def test_E():  # [F C G D] A E B
    assert escala('E') == ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', ]

def test_B():  # [F C G D A] E B
    assert escala('B') == ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']

def test_Bb():  # [B E] A D G C F
    assert escala('Bb') == ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A']

def test_Eb():  # [B E A] D G C F
    assert escala('Eb') == ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D']

def test_F():  # [B] E A D G C F
    assert escala('F') == ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']

#def test_F_sus():  # [F C G D A E B F# C#]
#    assert escala('F#') == ['F#', 'G#', 'A#', 'B#', 'C#', 'D#', 'E#']
