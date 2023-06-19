from lib.dish import Dish
from lib.restaurant import Restaurant
import pytest

# Restaurant.add() adds Dish item to self.dishes
def test_restaurant_add_adds_dish():
    restaurant = Restaurant()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    restaurant.add(dish1)
    restaurant.add(dish2)
    result = restaurant.dishes
    assert result == [{"Margarita pizza": 10.99}, {"Chicken korma": 9.78}]

# Restaurant.view_formatted_menu() returns list of all dishes with prices (keeping 00)
def test_restaurant_all_returns_dishes():
    restaurant = Restaurant()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    dish3 = Dish("Pasta bolognese", 8.00)
    restaurant.add(dish1)
    restaurant.add(dish2)
    restaurant.add(dish3)
    result = restaurant.view_formatted_menu()
    assert result == "Margarita pizza: £10.99\nChicken korma: £9.78\nPasta bolognese: £8.00"

# Restaurant.search() returns Dish object
def test_restaurant_search_returns_dish():
    restaurant = Restaurant()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    dish3 = Dish("Pasta bolognese", 8.00)
    restaurant.add(dish1)
    restaurant.add(dish2)
    restaurant.add(dish3)
    result = restaurant.search("Chicken")
    assert result == "Chicken korma: £9.78"

# Restaurant.search() returns formatted dishes in a list
def test_restaurant_search_returns_dishes():
    restaurant = Restaurant()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    dish3 = Dish("Pasta bolognese", 8.00)
    dish4 = Dish("Pasta carbonara", 8.60)
    restaurant.add(dish1)
    restaurant.add(dish2)
    restaurant.add(dish3)
    restaurant.add(dish4)
    result = restaurant.search("pasta")
    assert result == "Pasta bolognese: £8.00\nPasta carbonara: £8.60"

# Restaurant.search() raises error if Dish object does not exist
def test_restaurant_rasies_error_if_no_dish():
    restaurant = Restaurant()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    restaurant.add(dish1)
    restaurant.add(dish2)
    with pytest.raises(Exception) as e:
        restaurant.search("beef")
    assert str(e.value) == "Sorry, there is no beef on the menu!"
