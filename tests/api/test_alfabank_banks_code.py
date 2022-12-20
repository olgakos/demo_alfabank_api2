import os

import requests
from schemas.alfabank import *
from pytest_voluptuous import S
from alfabank.utils.sessions import alfabank
from allure import tag, title

@tag('API')
@title("Display Bank codes")
def test_display_bank_codes():
    type_code = os.getenv('TYPE_CODE')
    bic_name = os.getenv('BIC_NAME_BANK')

    params = f"type={type_code}&search={bic_name}"

    response = alfabank().get(
        f'/public/banks',
        params=params
    )
    assert response.status_code == 200
    assert S(code_banks) == response.json()
    assert response.json()["banks"][0]["bic"] == bic_name