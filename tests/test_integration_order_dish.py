from lib.order import Order
from lib.dish import Dish
from lib.restaurant import Restaurant
import pytest

# Order.add_to_order() adds dish to receipt
def test_add_to_order_adds_dish_to_receipt():
    order = Order()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    dish3 = Dish("Pasta bolognese", 8.00)
    dish4 = Dish("Pasta carbonara", 8.60)
    restaurant = Restaurant()
    restaurant.add(dish1)
    restaurant.add(dish2)
    restaurant.add(dish3)
    restaurant.add(dish4)
    order.add_to_order("Chicken korma", restaurant.dishes)
    assert order.receipt == [{'Chicken korma': 9.78}]

# Order.add_to_order() raises error if Dish does not exist
def test_add_to_order_raises_error():
    order = Order()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    restaurant = Restaurant()
    restaurant.add(dish1)
    restaurant.add(dish2)
    with pytest.raises(Exception) as e:
        order.add_to_order("Pasta alfredo", restaurant.dishes)
    assert str(e.value) == "Dish does not exist"

# Order.remove_order() removes order from receipt
def test_remove_order_removes_item_from_receipt():
    order = Order()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    restaurant = Restaurant()
    restaurant.add(dish1)
    restaurant.add(dish2)
    order.add_to_order("Margarita pizza", restaurant.dishes)
    order.add_to_order("Chicken korma", restaurant.dishes)
    order.remove_order("Margarita pizza")
    assert order.receipt == [{'Chicken korma': 9.78}]

# Order.remove_order() raises error if Dish not in receipt
def test_remove_order_raises_error_if_dish_not_in_order():
    order = Order()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    restaurant = Restaurant()
    restaurant.add(dish1)
    restaurant.add(dish2)
    order.add_to_order("Margarita pizza", restaurant.dishes)
    order.add_to_order("Chicken korma", restaurant.dishes)
    with pytest.raises(Exception) as e:
        order.remove_order("Pasta alfredo")
    assert str(e.value) == "Item is not in order"

# Order.remove_order() raises error if receipt is empty
def test_remove_order_raises_error_if_order_is_empty():
    order = Order()
    with pytest.raises(Exception) as e:
        order.remove_order("Pasta alfredo")
    assert str(e.value) == "Item is not in order"

# Order.maker_order() returns itemised receipt and grand total
def test_make_order_returns_itemised_receipt_and_grand_total():
    order = Order()
    dish1 = Dish("Margarita pizza", 10.99)
    dish2 = Dish("Chicken korma", 9.78)
    dish3 = Dish("Pasta bolognese", 8.00)
    dish4 = Dish("Pasta carbonara", 8.60)
    restaurant = Restaurant()
    restaurant.add(dish1)
    restaurant.add(dish2)
    restaurant.add(dish3)
    restaurant.add(dish4)
    order.add_to_order("Margarita pizza", restaurant.dishes)
    order.add_to_order("Chicken korma", restaurant.dishes)
    order.add_to_order("Pasta bolognese", restaurant.dishes)
    order.add_to_order("Pasta carbonara", restaurant.dishes)
    result = order.make_order("+447984641632", "+14066128776", order)
    assert result == "Margarita pizza: £10.99\nChicken korma: £9.78\nPasta bolognese: £8.00\nPasta carbonara: £8.60\nTotal: £37.37"
