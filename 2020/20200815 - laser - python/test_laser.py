# Mantenha o seu cursor aqui quando não estiver pilotando: |

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

def laser(largura, pontos):
    quantos_x = len(set(px for px, _ in pontos))
    quantos_y = len(set(py for _, py in pontos))

    return 1 if len(pontos) == 1 else quantos_x + quantos_y


def test_1():
    largura = 10
    pontos = ((0, 0),)
    quantidade_de_disparos_que_mata_ponto = laser(largura, pontos)
    assert 1 == quantidade_de_disparos_que_mata_ponto

def test_2_alinhados():
    largura = 10
    pontos = ((0, 0), (0, 1))
    quantidade_de_disparos_que_mata_ponto = laser(largura, pontos)
    assert 3 == quantidade_de_disparos_que_mata_ponto

def test_3_alinhados():
    largura = 1
    pontos = ((0, 0), (0, 2), (0, 4))
    quantidade_de_disparos_que_mata_ponto = laser(largura, pontos)
    assert 4 == quantidade_de_disparos_que_mata_ponto

def test_4_pontos_paralelogramo():
    largura = 1
    pontos = (           (2, 6),
                         (2, 4),
  
              (0, 2),
              (0, 0),)
    quantidade_de_disparos_que_mata_ponto = laser(largura, pontos)
    assert 6 == quantidade_de_disparos_que_mata_ponto

def test_4_pontos_quadrado():
    largura = 1
    pontos = ((0, 2), (2, 2),
              (0, 0), (2, 0))
    quantidade_de_disparos_que_mata_ponto = laser(largura, pontos)
    assert 4 == quantidade_de_disparos_que_mata_ponto

def test_2_pontos_e_laser_largura_2():
    largura = 2
    pontos = ((0, 2), (2, 4))
    quantidade_de_disparos_que_mata_ponto = laser(largura, pontos)
    assert 3 == quantidade_de_disparos_que_mata_ponto    

def _test_4_pontos_quadrado_lado_2_e_laser_largura_2():
    largura = 2
    pontos = ((0, 2), (2, 2),
              (0, 0), (2, 0))
    quantidade_de_disparos_que_mata_ponto = laser(largura, pontos)
    assert 5 == quantidade_de_disparos_que_mata_ponto    