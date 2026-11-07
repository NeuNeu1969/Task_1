from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Булочки: название и цена
BUN_CASES = [
    ("black bun", 100),
    ("white bun", 200.5),
    ("", 0),
]

# Ингредиенты: тип, название и цена
INGREDIENT_CASES = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 150.5),
]

# Булочки в базе данных
DATABASE_BUN_NAMES = ["black bun", "white bun", "red bun"]

# Ингредиенты в базе данных
DATABASE_INGREDIENT_NAMES = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]

# Цена бургера: цена булочки, цены ингредиентов, итог
BURGER_PRICE_CASES = [
    (100, [], 200),
    (100, [50], 250),
    (200, [100, 300], 800),
]
