# problema: http://dojopuzzles.com/problemas/exibe/ocr-bancario/

"""
Cada entrada possui 4 linhas, e cada linha possui 27 caracteres.
As 3 primeiras linhas contém o número da conta, utilizando pipes e underscores,
e a quarta linha é vazia. Cada número de conta possui nove dígitos (entre 0 e 9). 
"""
# >>>>>>> cursor aqui:
import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])
from textwrap import dedent

lista_digitos = [dedent("""
                          _
                         | |
                         |_|"""),
                dedent("""

                           |
                           |"""),
                dedent("""
                         _
                         _|
                        |_ """),
                '', '', '', '', '',
                dedent("""
                           _ 
                          |_|
                          |_|""")]

def ocr(digito):
    return lista_digitos.index(digito)

def test_8():
    assert ocr(dedent("""
                          _ 
                         |_|
                         |_|""")) == 8

def test_0():
    assert ocr(dedent("""
                          _
                         | |
                         |_|""")) == 0

def test_1():
    assert ocr(dedent("""

                          |
                          |""")) == 1

def test_2():
    assert ocr(dedent("""
                         _
                         _|
                        |_ """)) == 2

def test_11():
    assert ocr(dedent("""
                             
                            |   |
                            |   |""")) == 11