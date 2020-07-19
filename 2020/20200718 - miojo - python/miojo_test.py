import pytest
from math import gcd
pytest.main([__file__, '-v', '-p', 'no:warnings'])

def preparo(ampulheta_1, ampulheta_2):
    if gcd(ampulheta_1,ampulheta_2) not in (1,3):
        return None

    tempo1 = 0
    tempo2 = 0
    while True:
        if tempo1 <= tempo2:
            tempo1 += ampulheta_1
        
        if tempo1 % ampulheta_2 == 3:
            return tempo1

        if tempo2 <= tempo1:
            tempo2 += ampulheta_2

        if tempo2 % ampulheta_1 == 3:
            return tempo2    

@pytest.mark.parametrize('amp1, amp2, tempo', (
    (4, 7, 7),
    (5, 8, 8),
    (8, 5, 8),
    (34, 37, 37),
    (5, 7, 10),
    (7, 11, 14),
    (8, 13, 16),
    (17, 5, 20),
    (5, 17, 20),
    (5, 27, 30),
    (4, 8, None),
    (18,24,None),
    (6,9,9)
))
def test_miojo(amp1, amp2, tempo):
    assert preparo(amp1, amp2) == tempo

# 0  -> 5 17
# 5  -> 5
# 10 -> 5
# 15 -> 5
# 17 -> 17
# 20 -> 20

# I -> 5 17
# II -> 5 17 -> 10 34
# III -> 5 17 -> 15 51
# IV -> 5 17 -> 20 68

# 0 > 5 & 9 
# 5 > 5 & 4
# 9 > 1 & 9
# 10> 5 & 8
# 15> 5 & 3
# 18> - & -
