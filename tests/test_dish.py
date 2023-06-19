from lib.dish import Dish
import pytest

# Dish() raises an error if Dish.name is not str
def test_raises_error_if_dish_name_not_str():
    with pytest.raises(Exception) as e:
        Dish(97, 9.99)
    assert str(e.value) == "name should be a string"

# Dish() raises an error if Dish.price is not float
def test_raises_error_if_dish_price_not_float():
    with pytest.raises(Exception) as e:
        Dish("Chicken korma", "9.99")
    assert str(e.value) == "price should be a float"

