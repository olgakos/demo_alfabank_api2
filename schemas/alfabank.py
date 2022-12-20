from voluptuous import Schema, Any, ALLOW_EXTRA, PREVENT_EXTRA

exchange_rates = Schema(
    {
        "rates": [
            {
                "sellRate": Any(int, float),
                "sellIso": str,
                "sellCode": int,
                "buyRate": Any(int, float),
                "buyIso": str,
                "buyCode": int,
                "quantity": int,
                "name": Any(str, None),
                "date": str
            }
        ]
    }
)


#2
'''
Шаблон:
RESPONSE
{
  "rates": [
    {
      "rate": 0,
      "iso": "string",
      "code": 0,
      "quantity": 0,
      "date": "06.08.2019",
      "name": "string"
    }
  ]
}
'''
exchange_rates_belarus = Schema(
    {
        "rates": [
            {
                "rate": float,
                "iso": str,
                "code": int,
                "quantity": int,
                "date": str,
                "name": str

            }
        ]
    }
,
    #required=True,
    #extra=PREVENT_EXTRA
)

#3
'''
RESPONSE
{
  "totalRowCount": 0,
  "banks": [
    {
      "bic": "string",
      "name": "string",
      "address": "string"
    }
  ]
}
'''
'''
exchange_rates_banks = Schema(
    {
        "totalRowCount": int,
        "banks": [
            {
                "bic": str,
                "name": str,
                "address": str,
            }
        ]
    }
)
'''


code_banks = Schema(
    {
        "totalRowCount": int,
        "banks": [
            {
                "bic": str,
                "name": str,
                "address": str
            }
        ]
    }
)