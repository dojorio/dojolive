import pytest

from datetime import datetime, timedelta


def prazo_de_expiracao(data_de_criacao):
    if data_de_criacao.hour < 8:
        data_de_criacao = data_de_criacao.replace(hour=8)
    if data_de_criacao.hour < 17:
        return data_de_criacao + timedelta(hours=1)
    return datetime(2020, 5, data_de_criacao.day + 1, 9)


@pytest.mark.parametrize(
    "data_de_criacao,data_de_expiracao",
    [
        ((2020, 5, 27, 17), (2020, 5, 28, 9)),
        ((2020, 5, 26, 17), (2020, 5, 27, 9)),
        ((2020, 5, 28, 20), (2020, 5, 29, 9)),
        ((2020, 5, 27, 15), (2020, 5, 27, 16)),
        ((2020, 5, 27, 8), (2020, 5, 27, 9)),
        ((2020, 5, 27, 7), (2020, 5, 27, 9)),
    ]
)
def test_prazo_de_expiracao(data_de_criacao, data_de_expiracao):
    assert prazo_de_expiracao(datetime(*data_de_criacao)) == datetime(*data_de_expiracao)
