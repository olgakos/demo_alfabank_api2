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
@title("Display exchange rates of the National Bank of the Republic of Belarus")
def test_display_bank_all_exchange_rates_rb():
    response = alfabank().get(f'/public/nationalRates',
                              params={'currencyCode': '840, 978'}
                              )
    assert response.status_code == 200
    assert len(response.json()['rates']) != 0
    assert S(exchange_rates_belarus) == response.json()
    # первый вложенный список
    assert response.json()["rates"][0]["date"] == now_time
    #assert response.json()['rates'][0]['rate'] == 2.6376 #dinamic! For example: Expected:2.6376  Actual:2.6728
    assert response.json()['rates'][0]['iso'] == "EUR"
    assert response.json()['rates'][0]['code'] == 978
    assert response.json()['rates'][0]['name'] == "евро"
    # второй вложенный список
    assert response.json()["rates"][1]["date"] == now_time
    #assert response.json()['rates'][1]['rate'] == 2.5022 #dinamic! For example: Expected:2.5022 Actual:2.5061
    assert response.json()['rates'][1]['iso'] == "USD"
    assert response.json()['rates'][1]['code'] == 840
    assert response.json()['rates'][1]['name'] == "доллар США"