from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    # Пустой бургер
    return Burger()


@pytest.fixture
def mock_bun():
    # Мок булочки
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_sauce():
    # Мок соуса
    sauce = Mock()
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 50
    return sauce


@pytest.fixture
def mock_filling():
    # Мок начинки
    filling = Mock()
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 150
    return filling
