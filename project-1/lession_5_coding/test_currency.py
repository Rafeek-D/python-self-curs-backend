from .currency_prog  import Currency_converter

def test_conversion():
    converter = Currency_converter()
    assert converter.conversion("EUR","USD",100)== 90.0




