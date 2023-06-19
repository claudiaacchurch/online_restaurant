from lib.order import Order
from lib.restaurant import Restaurant
from unittest import mock
from unittest.mock import Mock, MagicMock
import pytest

# Order.add_to_order() adds dish to receipt
def test_add_to_order_dish_to_receipt():
    order = Order()
    dishes = [{'Chicken korma': 9.78}, {'Pasta alfredo': 9.60}]
    order.add_to_order("Pasta alfredo", dishes)
    result = order.receipt
    assert result == [{'Pasta alfredo': 9.60}]

# Order.add_to_order() raises error if Mock dish does not exist
def test_add_to_order_raises_error():
    order = Order()
    dishes = [{'Chicken korma': 9.78}, {'Pasta alfredo': 9.60}]
    with pytest.raises(Exception) as e:
        order.add_to_order("Pasta carbonara", dishes)
    assert str(e.value) == "Dish does not exist"

# Order.make_order() returns itemised receipt and grand total
def test_make_order_returns_itemised_receipt_and_total():
    order = Order()
    dishes = [{'Chicken korma': 9.78}, {'Pasta alfredo': 9.60}]
    order.add_to_order("Chicken korma", dishes)
    order.add_to_order("Pasta alfredo", dishes)
    result = order.make_order("+447984641632", "+14066128776", order)
    assert result == "Chicken korma: £9.78\nPasta alfredo: £9.60\nTotal: £19.38"

# Order.send_text() uses a Mock API to send a confirmation text

# patches send_order_confirmation in the Order class. Required othersie method can't use return_value 
@mock.patch('lib.order.Order.send_order_confirmation')
def test_order_send_text_mock(send_order_confirmation_mock):
    order = Order()
    expected_sid = 'SM87105da94bff44b999e4e6eb90d8eb6a'

    # create new mock object of the twilio api and set its sid
    mock_return = Mock()
    mock_return.sid = expected_sid

    send_order_confirmation_mock.return_value = mock_return

    to = "<your-personal-number>"
    from_ = "<your-twilio-number>"

    result = order.send_order_confirmation(to, from_)

    assert send_order_confirmation_mock.called
    assert result.sid == expected_sid