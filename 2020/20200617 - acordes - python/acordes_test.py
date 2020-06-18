# Dó Dó# Ré Ré# Mi Fá Fá# Sol Sol# Lá Lá# Si Dó
# Um acorde maior é formado pela nota que dá seu nome + 2 tons + 1 tom e meio
# Um acorde menor é formado pela nota que dá seu nome + 1 tom e meio + 2 tons

import pytest

NOTAS = "Do Do# Re Re# Mi Fa Fa# Sol Sol# La La# Si".split(" ")

def acorde(tom):
    menor = tom.endswith('m')
    if menor:
        tom = tom[:-1]
    
    if tom.endswith('b'):
        tom = NOTAS[NOTAS.index(tom[:-1]) - 1]
    
    indice = NOTAS.index(tom)
    terca_menor = NOTAS[(indice + 3) % 12]
    terca_maior = NOTAS[(indice + 4) % 12]
    quinta_justa = NOTAS[(indice + 7) % 12]
    terca = terca_menor if menor else terca_maior
    return [tom, terca, quinta_justa]

@pytest.mark.parametrize(
    "tom, notas",
    (
        ("Do", ["Do", "Mi", "Sol"]),
        ("Re", ["Re", "Fa#", "La"]),
        ("Mi", ["Mi", "Sol#", "Si"]),
        ("La", ["La", "Do#", "Mi"]),
        ("Si", ["Si", "Re#", "Fa#"]),
        ("Do#", ["Do#","Fa", "Sol#"]),
        ("Dom", ["Do", "Re#", "Sol"]),
        ("Reb", ["Reb", "Fa", "Lab"]),
        ("Lab", ["Sol#", "Do" , "Re#"]),
        ("Labm", ["Sol#", "Si" , "Re#"]),
    )
)
def test_acorde(tom, notas):
    assert acorde(tom) == notas

pytest.main([__file__, '-v'])
