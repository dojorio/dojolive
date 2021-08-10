# Mantenha o seu cursor aqui quando não estiver pilotando: |

# Participantes:
# *Lucas
# *Rodrigo
# *Orlando Saraiva Jr
# *Daniel Souza
# *Allan Patrick
# Cláudio Berrondo
# Marcos Lima
# Geovane Carvalho
# Bruno Osório
# John
# Celestino

# E um número triste? Como sabemos que um número não será feliz?

import pytest

pytest.main([__file__, '-v', '-p', 'no:warnings'])


# 2 => "4" => 16 => 37 => 58 => 89 => 145 => 42 => 20 => "4"
def is_happy(n, visited_numbers = None):
    if visited_numbers is None:
        visited_numbers = []

    result = sum(int(x)**2 for x in str(n))

    if result == 1:
        return True
    
    # print(visited_numbers)

    if result in visited_numbers:
        return False
    
    visited_numbers.append(result)
    
    return is_happy(result, visited_numbers)


rows = 40
cols = 100
for row in range(rows):
    line = ''
    for col in range(cols):
        val = row * cols + col
        line += '#' if is_happy(val) else ' '
    print(line)


def test_2111():
  assert is_happy(2111) is True


def test_ten():
    assert is_happy(10) is True


def test_one():
    assert is_happy(1) is True


def test_two():
    assert is_happy(2) is False


def test_seven():
    assert is_happy(7) is True


def test_nine():
    assert is_happy(9) is False

def test_49():
    assert is_happy(49) is True

