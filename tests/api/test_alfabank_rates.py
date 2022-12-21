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
@title("Display Bank exchange rates ")
def test_display_bank_all_exchange_rates():
    response = alfabank().get(f'/public/rates')
    with step('Check status code'):
        assert response.status_code == 200
    with step('Check response'):
        assert S(exchange_rates) == response.json()
    with step('Check time'):
        assert response.json()["rates"][0]["date"] == now_time
    with step('Check status code'):
        assert response.status_code == 200
    with step('Check !=0'):
        assert len(response.json()['rates']) != 0
    '''
    with step('Check First data'):
        assert response.json()['rates'][0]['buyCode'] == 933
        assert response.json()['rates'][0]['buyIso'] == 'BYN'
        assert response.json()['rates'][0]['sellIso'] == 'EUR'
        assert response.json()['rates'][0]['name'] == 'евро'
    with step('Check Second data'):
        assert response.json()['rates'][1]['buyCode'] == 643
        assert response.json()['rates'][1]['buyIso'] == 'RUB'
        assert response.json()['rates'][1]['sellIso'] == 'EUR'
        assert response.json()['rates'][1]['name'] == None
    '''
    with step('Check First data'):
        assert response.json()['rates'][0]['buyCode'] == 643
        assert response.json()['rates'][0]['buyIso'] == 'RUB'
        assert response.json()['rates'][0]['sellIso'] == 'EUR'
        assert response.json()['rates'][0]['name'] == None
    with step('Check Second data'):
        assert response.json()['rates'][1]['buyCode'] == 643
        assert response.json()['rates'][1]['buyIso'] == 'RUB'
        assert response.json()['rates'][1]['sellIso'] == 'USD'
        assert response.json()['rates'][1]['name'] == None