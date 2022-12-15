import requests
from schemas.alfabank import *
from pytest_voluptuous import S
from alfabank.utils.sessions import alfabank
from allure import tag, title

@tag('API')
@title("Display Bank's Code")
def test_display_bank_all_exchange_rates_banks():
    #response = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/banks?type=by&search=ALFABY2X')
    response = alfabank().get(f'/public/banks?type=by&search=ALFABY2X')
    '''
    ??
    response = alfabank().get(f'/public/banks',
                              params={'type': 'by&search=ALFABY2X'}
                              )
    '''
    assert response.status_code == 200
    assert len(response.json()['banks']) != 0
    assert S(exchange_rates_banks) == response.json()
    assert response.json()['totalRowCount'] == 1
    assert response.json()["banks"][0]["bic"] == "ALFABY2X"
    assert response.json()['banks'][0]['name'] == "ЗАО 'АЛЬФА-БАНК', Г.МИНСК, РБ"
    assert response.json()['banks'][0]['address'] == ""