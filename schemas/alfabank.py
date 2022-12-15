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