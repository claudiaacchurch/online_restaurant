from lib.restaurant import Restaurant
from unittest.mock import Mock

# Restaurant.add() adds a Mock dish to self.dishes
def test_restaurant_mock_add_adds_dish_to_dishes():
    restaurant = Restaurant()
    dish1 = Mock()
    dish2 = Mock()
    dish1.name = "Chicken korma"
    dish1.price = 9.78
    dish2.name = "Pasta alfredo"
    dish2.price = 9.60
    restaurant.add(dish1)
    restaurant.add(dish2)
    result = restaurant.dishes
    assert result == [{'Chicken korma': 9.78}, {'Pasta alfredo': 9.60}]

# Restaurant.view_formatted_menu() returns list of formatted Mock dish items
def test_restaurant_mock_returns_formatted_menu():
    restaurant = Restaurant()
    dish1 = Mock()
    dish2 = Mock()
    dish1.name = "Chicken korma"
    dish1.price = 9.78
    dish2.name = "Pasta alfredo"
    dish2.price = 9.60
    restaurant.add(dish1)
    restaurant.add(dish2)
    result = restaurant.view_formatted_menu()
    assert result == "Chicken korma: £9.78\nPasta alfredo: £9.60"

# Restaurant.search() returns Mock dish item that matches parameter
def test_restaurant_mock_search_returns_search_results():
    restaurant = Restaurant()
    dish1 = Mock()
    dish2 = Mock()
    dish1.name = "Chicken korma"
    dish1.price = 9.78
    dish2.name = "Pasta alfredo"
    dish2.price = 9.60
    restaurant.add(dish1)
    restaurant.add(dish2)
    result = restaurant.search("pasta")
    assert result == "Pasta alfredo: £9.60"