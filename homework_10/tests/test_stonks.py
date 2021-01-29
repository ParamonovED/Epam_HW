import json
import os

from homework_10.stonks import check_exchange, make_output


def test_check_exchange_type():
    """
    site will return value from today or last day when recording was wrote
    """
    assert isinstance(check_exchange(), float)


def test_mock_check_exchange(requests_mock):
    mock_page = '<?xml version="1.0" encoding="windows-1251"?>\
             <html> \
             <Valute ID="R01235"> \
             <CharCode>USD</CharCode> \
             <Value>66,6666</Value> \
             </Valute> \
             </html>'
    requests_mock.get("http://www.cbr.ru/scripts/XML_daily.asp", text=mock_page)
    assert check_exchange() == 66.6666


def test_make_output(tmp_path):
    data = {
        "0": {
            "growth": 99,
            "code": "growth_p_e",
            "price": 10,
            "P/E": 1,
            "potential profit": 10,
        },
        "1": {
            "growth": 1,
            "code": "price_profit",
            "price": 99,
            "P/E": 10,
            "potential profit": 99,
        },
    }
    os.chdir(tmp_path)
    make_output(data)
    with open("price.json", "r") as f:
        price = json.loads(f.read())
    with open("p_div_e.json", "r") as f:
        p_div_e = json.loads(f.read())
    with open("growth.json", "r") as f:
        growth = json.loads(f.read())
    with open("potential profit.json", "r") as f:
        potential_profit = json.loads(f.read())

    assert (
        price
        == potential_profit
        == {
            "1": {
                "growth": 1,
                "code": "price_profit",
                "price": 99,
                "P/E": 10,
                "potential profit": 99,
            },
            "0": {
                "growth": 99,
                "code": "growth_p_e",
                "price": 10,
                "P/E": 1,
                "potential profit": 10,
            },
        }
    )
    assert p_div_e == growth == data
