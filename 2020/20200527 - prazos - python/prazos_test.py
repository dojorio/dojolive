def prazo_de_expiracao(data_de_criacao):
    return '2020-05-28 09:00'

def test_prazo_de_expiracao():
    assert prazo_de_expiracao('2020-05-27 17:00') == '2020-05-28 09:00'
    assert prazo_de_expiracao('2020-05-26 17:00') == '2020-05-27 09:00'