import requests
from src import app
from src.controllers.controller import format_price_clp

def test_get_productos_success():
    with app.test_client() as client:
        rv = client.get('/api/get_productos')
        assert rv.status_code == 200


def test_exchange_rate_success():
    with app.test_client() as client:
        amount_clp = 1000 # Cambiar esto por un valor real
        rv = client.get(f'/api/exchange_rate?amount_clp={amount_clp}')
        assert rv.status_code == 200


def test_format_price_clp():
    # Prueba con un precio bajo
    assert format_price_clp(100) == '$100'
    
    # Prueba con un precio exactamente 1 millón
    assert format_price_clp(1000000) == '$1.000.000'