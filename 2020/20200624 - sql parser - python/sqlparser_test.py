# Dado uma estrutura de dados onde uma tabela é uma lista de dicionários,
# crie um interpretador de SQL que seja capaz de executar "selects" nesses dados.
# pessoa = [{"nome": "Fulano", "idade": 15}, {"nome": "Ciclano", "idade": 50}]
# 
# Exemplo
# SELECT * FROM pessoa;
# nome    | idade
# Fulano  |  15
# Ciclano |  50

import pytest
pytest.main([__file__, '-v'])


dados = {
    "pessoa": [
        {"id": 0, "nome": "Fulano", "idade": "15", "email": "fulano@gmail.com"},
        {"id": 1, "nome": "Berrondo", "idade": "57", "email": "cl.berrondo@gmail.com"},
        {"id": 2, "nome": "Chico", "idade": "28", "email": "chico.quimica@ifrj.gov.br"},
        {"id": 3, "nome": "Mari", "idade": "24", "email": "mari@gmail.com"},
        {"id": 4, "nome": "Guido", "idade": "50", "email": "guido.van@python.org"},
    ]
}


def selecao(tabela, condicao):
    campo, valor = condicao.split('=')
    return [
        pessoa for pessoa in tabela
        if str(pessoa[campo]) == valor.replace("'", "")
    ]

def projecao(tabela, campos):
    if '*' in campos:
        return tabela
    return [
        {campo: pessoa[campo] for campo in campos}
        for pessoa in tabela
    ]


def executa(query):
    query = query.replace("select ", "").replace(" ", "").replace(";", "")
    campos, resto = query.split("from")  # "id,nome", "pessoawhereid=1"
    fragmentos = resto.split("where")
    condicao = None
    
    if len(fragmentos) > 1:
        tabela, condicao = fragmentos
    else:
        tabela = fragmentos[0]

    temporario = dados[tabela]
    campos = campos.split(",")
    if condicao:
        temporario = selecao(temporario, condicao)
    return projecao(temporario, campos)

def test_selecionar_tudo():
    assert executa("select * from pessoa;") == dados["pessoa"]

def test_selecionar_id():
    assert executa("select id from pessoa;") == [
        {"id": pessoa["id"]} for pessoa in dados["pessoa"]
    ]

def test_selecionar_nome():
    assert executa("select nome from pessoa;") == [
        {"nome": pessoa["nome"]} for pessoa in dados["pessoa"]
    ]

def test_selecionar_idade():
    assert executa("select idade from pessoa;") == [
        {"idade": pessoa["idade"]} for pessoa in dados["pessoa"]
    ]

def test_selecionar_email():
    assert executa("select email from pessoa;") == [
        {"email": pessoa["email"]} for pessoa in dados["pessoa"]
    ]

def test_selecionar_id_e_nome():
    assert executa("select id, nome from pessoa;") == [
        {"id": pessoa["id"], "nome": pessoa["nome"]}
        for pessoa in dados["pessoa"]
    ]

def test_selecionar_tudo_e_nome():
    assert executa("select *, nome from pessoa;") == [
        {"id": pessoa["id"], "nome": pessoa["nome"], "idade": pessoa["idade"], "email": pessoa["email"]}
        for pessoa in dados["pessoa"]
    ]

def test_selecionar_id_igual_a_1():
    assert executa("select id from pessoa where id = 1;") == [
        {"id": 1}
    ]

def test_selecionar_id_igual_a_2():
    assert executa("select id from pessoa where id = 2;") == [
        {"id": 2}
    ]

def test_selecionar_tudo_com_id_igual_a_2():
    assert executa("select * from pessoa where id = 2;") == [
        {"id": 2, "nome": "Chico", "idade": "28", "email": "chico.quimica@ifrj.gov.br"},
    ]

def test_selecionar_tudo_com_email():
    assert executa("select * from pessoa where email = 'chico.quimica@ifrj.gov.br';") == [
        {"id": 2, "nome": "Chico", "idade": "28", "email": "chico.quimica@ifrj.gov.br"},
    ]
