import pytest

from datetime import datetime, timedelta


def prazo_de_expiracao(data_de_criacao):
    if data_de_criacao.hour < 8:
        data_de_criacao = data_de_criacao.replace(hour=8, minute=0, second=0, microsecond=0)

    if data_de_criacao.weekday() in (5, 6):
        data_de_criacao = data_de_criacao + timedelta(days=7 - data_de_criacao.weekday())

    distancia_ate_17 = data_de_criacao.replace(hour=17, minute=0, second=0, microsecond=0) - data_de_criacao
    if timedelta(hours=0) < distancia_ate_17 < timedelta(hours=1):
        return data_de_criacao + timedelta(hours=16)

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
        ((2020, 5, 30, 7), (2020, 6, 1, 9)),
        ((2020, 5, 27, 7, 30, 1), (2020, 5, 27, 9)),
        ((2020, 5, 27, 16, 30), (2020, 5, 28, 8, 30)),
        ((2020, 5, 27, 16, 1), (2020, 5, 28, 8, 1)),
    ]
)
def test_prazo_de_expiracao(data_de_criacao, data_de_expiracao):
    assert prazo_de_expiracao(datetime(*data_de_criacao)) == datetime(*data_de_expiracao)
