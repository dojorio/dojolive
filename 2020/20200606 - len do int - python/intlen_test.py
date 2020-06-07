# como vejo o len de um int ?
# sem converter pra str

import pytest
import math

class Integer(int):
    def __len__(self):
        length = 1
        integer = self
        while integer >= 10:
            integer = integer / 10
            length += 1
        return length

    def __len__2(self):
        '''numero de digitos de um numero inteiro'''
        n = abs(self)
        if n > 0 and n <= 999999999999997:
            return int(math.log10(n)) + 1
        elif n == 0:
            return 1
        else:
            counter = 15
            while n >= 10**counter:
                counter = counter + 1
            return counter



def calc_length(integer):
    return len(Integer(integer))

@pytest.mark.parametrize(
    "inteiro,esperado",
    (
        (1, 1),
        (10, 2),
        (11, 2),
        (100, 3),
        (0, 1),
        (199, 3),
        (1999, 4),
        (1_000_000_000_000_000, 16),
        (999_999_999_999_999, 15),
    ),
)
def test_len(inteiro, esperado):
    assert calc_length(inteiro) == esperado

pytest.main([__file__, "-v"])