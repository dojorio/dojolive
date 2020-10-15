# Mantenha o seu cursor aqui quando não estiver pilotando: |
# Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
# Saída: [100-105], [110-111], [113-115], [150]

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

# [100, 200, 201, 202, 300, 301]
def intervalo(lista_numeros):
    resultado = []
    numero_anterior = None

    for numero in lista_numeros:
        if resultado and numero == numero_anterior + 1:
            if len(resultado[-1]) == 1:
                resultado[-1].append(numero)
            else:
                resultado[-1][-1] = numero
        else:
            resultado.append([numero])
        numero_anterior = numero  # 301
    return resultado  # [[100], [200, 202], [300, 301]]



@pytest.mark.parametrize("lista_de_entrada, resultado", (
    ([], []),
    ([100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150], [[100,105], [110,111], [113,115], [150]]),
    ([100, 101, 102], [[100, 102]]),
    (
        [100, 200, 201, 202, 300, 301],
        [[100], [200, 202], [300, 301]]
    ),
    ([100, 200, 300, 301], [[100], [200], [300, 301]]),
    ([100, 200, 300], [[100], [200], [300]]), # três números não consecutivos
    ([100, 101, 150], [[100, 101], [150]]),   # três números
    ([100, 200], [[100], [200]]),             # dois não consecutivos
    ([120, 150], [[120], [150]]),             # outros dois não consecutivos  
    ([150, 151], [[150, 151]]),               # dois números consecutivos
    ([150], [[150]]),                         # um número
))
def test_intervalo(lista_de_entrada, resultado):
    assert intervalo(lista_de_entrada) == resultado
