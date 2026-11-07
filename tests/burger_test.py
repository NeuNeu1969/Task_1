from unittest.mock import Mock

import pytest

from data import BURGER_PRICE_CASES


class TestBurger:

    def test_set_buns_sets_bun(self, burger, mock_bun):
        # Установка булочки
        burger.set_buns(mock_bun)

        # Проверка булочки в бургере
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self, burger, mock_sauce):
        # Добавление ингредиента
        burger.add_ingredient(mock_sauce)

        # Проверка списка ингредиентов
        assert burger.ingredients == [mock_sauce]

    def test_remove_ingredient_removes_from_list(self, burger, mock_sauce, mock_filling):
        # Два ингредиента, удаление первого
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)

        # Проверка, остался только второй
        assert burger.ingredients == [mock_filling]

    def test_move_ingredient_changes_order(self, burger, mock_sauce, mock_filling):
        # Два ингредиента, перемещение второго наверх
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)

        # Проверка нового порядка
        assert burger.ingredients == [mock_filling, mock_sauce]

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", BURGER_PRICE_CASES)
    def test_get_price_returns_sum(self, burger, bun_price, ingredient_prices, expected_price):
        # Мок булочки с ценой
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        # Моки ингредиентов с ценами
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        # Проверка цены: две булочки и ингредиенты
        assert burger.get_price() == expected_price

    def test_get_receipt_returns_receipt(self, burger, mock_bun, mock_sauce, mock_filling):
        # Бургер с булочкой, соусом и начинкой
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 400"
        )

        # Проверка чека
        assert burger.get_receipt() == expected_receipt
