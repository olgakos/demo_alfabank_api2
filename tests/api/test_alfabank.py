import requests
from schemas.alfabank import *
from pytest_voluptuous import S
from alfabank.utils.sessions import alfabank
from allure import tag, title
import datetime as DT


now = DT.datetime.now(DT.timezone.utc).astimezone()
time_format = "%d.%m.%Y"
now_time = f"{now:{time_format}}"


@tag('API')
@title("Display Bank exchange rates")
def test_display_bank_all_exchange_rates():
    response = alfabank().get(f'/public/rates')
    assert response.status_code == 200
    assert S(exchange_rates) == response.json()
    assert response.json()["rates"][0]["date"] == now_time
