import pytest

from praktikum.bun import Bun
from data import BUN_CASES


class TestBun:

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_get_name_returns_name(self, name, price):
        # Булочка с названием и ценой
        bun = Bun(name, price)

        # Проверка названия
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_get_price_returns_price(self, name, price):
        bun = Bun(name, price)

        # Проверка цены
        assert bun.get_price() == price
        
