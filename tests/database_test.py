from unittest.mock import patch

import pytest

from praktikum.database import Database
from data import DATABASE_BUN_NAMES, DATABASE_INGREDIENT_NAMES


class TestDatabase:

    @pytest.mark.parametrize("name", DATABASE_BUN_NAMES)
    def test_available_buns_contains_bun(self, name):
        # Список булочек из базы
        buns = Database().available_buns()

        # Проверка наличия булочки
        assert name in [bun.get_name() for bun in buns]

    @pytest.mark.parametrize("name", DATABASE_INGREDIENT_NAMES)
    def test_available_ingredients_contains_ingredient(self, name):
        # Список ингредиентов из базы
        ingredients = Database().available_ingredients()

        # Проверка наличия ингредиента
        assert name in [ingredient.get_name() for ingredient in ingredients]

    def test_available_buns_returns_three_buns(self):
        assert len(Database().available_buns()) == 3

    @patch("praktikum.database.Bun")
    def test_database_creates_buns_with_bun_class(self, mock_bun_class):
        # Подмена класса Bun моком
        Database()

        # Проверка, база создала три булочки через Bun
        assert mock_bun_class.call_count == 3
