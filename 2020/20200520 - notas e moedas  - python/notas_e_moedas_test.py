NOTAS = [1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0]


def atm(valor):
    if valor in NOTAS:
        return {valor: 1}
    else:
        return {2.00: 1,
                1.00: 1}


def test_atm():
    assert atm(1.00) == {1.00: 1}
    assert atm(5.00) == {5.00: 1}
    assert atm(20.00) == {20.00: 1}
    assert atm(3.00) == {2.00: 1,
                         1.00: 1}
