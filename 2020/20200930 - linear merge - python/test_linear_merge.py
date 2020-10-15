# Mantenha o seu cursor aqui quando não estiver pilotando: |

"""
12. linear_merge
Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.
A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


def linear_merge(list1, list2):
    resultado = []
    indice1 = 0
    indice2 = 0
    while len(resultado) != len(list1) + len(list2):
        try:
            valor_1 = list1[indice1]
        except IndexError:
            resultado.extend(list2[indice2:])
            break
        
        try:
            valor_2 = list2[indice2]
        except IndexError:
            resultado.extend(list1[indice1:])
            break

        if valor_1 <= valor_2:
            resultado.append(valor_1)
            indice1 +=  1
        else:
            resultado.append(valor_2)
            indice2 += 1

    return resultado



if __name__ == '__main__':
    test(linear_merge, (['a'], ['b']), ['a', 'b'])
    test(linear_merge, (['a'], ['a']), ['a', 'a'])
    test(linear_merge, (['a', 'b'], ['a']), ['a', 'a', 'b'])
    test(linear_merge, (['a', 'b'], ['a', 'a']), ['a', 'a', 'a','b'])

    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])

