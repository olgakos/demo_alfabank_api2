import requests
from allure_commons._allure import step

from schemas.alfabank import *
from pytest_voluptuous import S
from alfabank.utils.sessions import alfabank
from allure import tag, title

import datetime as DT


now = DT.datetime.now(DT.timezone.utc).astimezone()
time_format = "%d.%m.%Y"
now_time = f"{now:{time_format}}"


@tag('API')
@title("Display exchange rates of the National Bank of the Republic of Belarus")
def test_display_rb():
    response = alfabank().get(f'/public/nationalRates',
                              params={'currencyCode': '840, 978'}
                             )
    with step('Check status code'):
        assert response.status_code == 200
    with step('Check !=0'):
        assert len(response.json()['rates']) != 0
    with step('Check response'):
        assert S(exchange_rates_belarus) == response.json()
    # первый вложенный список
    with step('Check time'):
        assert response.json()["rates"][0]["date"] == now_time
        assert response.json()['rates'][0]['iso'] == "EUR"
        assert response.json()['rates'][0]['code'] == 978
        assert response.json()['rates'][0]['name'] == "евро"
    # второй вложенный список
        assert response.json()["rates"][1]["date"] == now_time
        assert response.json()['rates'][1]['iso'] == "USD"
        assert response.json()['rates'][1]['code'] == 840
        assert response.json()['rates'][1]['name'] == "доллар США"
