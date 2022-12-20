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
@title("Display Bank exchange rates (EASY)")
def test_display_bank_all_exchange_rates0():
    response = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
    assert response.status_code == 200
    assert S(exchange_rates) == response.json()
    assert response.json()["rates"][0]["date"] == now_time

@tag('API')
@title("Display Bank exchange rates ")
def test_display_bank_all_exchange_rates():
    response = alfabank().get(f'/public/rates')
    assert response.status_code == 200
    assert S(exchange_rates) == response.json()
    assert response.json()["rates"][0]["date"] == now_time
    assert response.status_code == 200
    assert len(response.json()['rates']) != 0
    #первый вложенный список
    assert response.json()['rates'][0]['buyCode'] == 933
    assert response.json()['rates'][0]['buyIso'] == 'BYN'
    assert response.json()['rates'][0]['sellIso'] == 'EUR'
    assert response.json()['rates'][0]['name'] == 'евро'
    #второй вложенный список
    assert response.json()['rates'][1]['buyCode'] == 643
    assert response.json()['rates'][1]['buyIso'] == 'RUB'
    assert response.json()['rates'][1]['sellIso'] == 'EUR'
    assert response.json()['rates'][1]['name'] == None