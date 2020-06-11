"""
Restringindo apenas para elementos mais conhecidos e para os quais a química
de ensino médio funciona relativamente bem:

Objetivo: testar se a combinação dos elementos é possível.

Metais alcalinos combinam com apenas um halogênio (NaCl) ou
com um calcogênio, precisando então de dois metais alcalinos do mesmo elemento (Na2O).

Metais alcalinos terrosos combinam com dois halogênios (MgCl2) ou
um calcogênio (MgO).

Calcogênios e halogênios não se combinam para formar sais.
"""

import pytest


class Elemento:
    ELETRONS_VALENCIA = None

    def __add__(self, other):
        if self.ELETRONS_VALENCIA not in (1, 2):
            return False
        return (self.ELETRONS_VALENCIA + other.ELETRONS_VALENCIA) % 8 == 0

    def __mul__(self, other):
        elemento = Elemento()
        elemento.ELETRONS_VALENCIA = self.ELETRONS_VALENCIA * other
        return elemento

    def __repr__(self):
        return f'{self.__class__.__name__}(e:{self.ELETRONS_VALENCIA})'


class Calcogenio(Elemento):
    ELETRONS_VALENCIA = 6


class Alcalino(Elemento):
    ELETRONS_VALENCIA = 1


class AlcalinoTerroso(Elemento):
    ELETRONS_VALENCIA = 2


class Halogenio(Elemento):
    ELETRONS_VALENCIA = 7


elementos_e_tipos = {
    Calcogenio: ['O', 'S'],
    Alcalino: ['Li', 'Na', 'K'],
    AlcalinoTerroso: ['Mg', 'Ca', 'Ba'],
    Halogenio: ['F', 'Cl', 'Br', 'I'],
}

# locals().update(
#     {
#         elemento: type(elemento, (tipo,), {})
#         for tipo, elementos in elementos_e_tipos.items()
#         for elemento in elementos
#     }
# )
for tipo, elementos in elementos_e_tipos.items():
    for elemento in elementos:
        locals()[elemento] = type(elemento, (tipo,), {})


@pytest.mark.parametrize(
    "primeiro, segundo, expected", (
            (Na(), Cl(), True),  # ALCALINO + HALOGENIO
            (Na(), O(), False),  # ALCALINO + CALCOGENIO
            (O(), S(), False),  # CALCOGENIO + CALCOGENIO
            (S(), O(), False),  # CALCOGENIO + CALCOGENIO
            (Na(), K(), False),  # ALCALINO + ALCALINO
            (Na(), Mg(), False),  # ALCALINO + TERROSO
            (Cl(), Na(), False),  # HALOGENIO + ALCALINO
            (Mg(), O(), True),  # TERROSO + CALCOGENIO
    )
)
def test_com_dois_elementos(primeiro, segundo, expected):
    assert primeiro + segundo is expected


def test_tres_elementos():
    assert Mg() + Cl() * 2 is True
    assert Na() * 2 + O() is True
    assert Ca() + F() * 2 is True


pytest.main([__file__, '-v'])
