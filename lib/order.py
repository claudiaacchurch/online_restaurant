import os
from datetime import datetime, timedelta
from twilio.rest import Client
import dotenv

class Order():
    def __init__(self):
        self.receipt = []
        self.total = 0

    def add_to_order(self, dish, all_dishes):
        for dish_item in all_dishes:
            if dish in dish_item:
                self.receipt.append(dish_item)
        if len(self.receipt) < 1:
            raise Exception("Dish does not exist")
        return self.receipt
    
    def remove_order(self, dish):
        dish_to_remove = None
        for dish_item in self.receipt:
            if dish in dish_item:
                dish_to_remove = dish_item
                break
        if dish_to_remove is None:
            raise Exception("Item is not in order")
        self.receipt.remove(dish_to_remove)
        return self.receipt
    
    def make_order(self, to_number, from_number, text_sender):
        itemised_receipt = ""
        for order_item in self.receipt:
            for name,price in order_item.items():
                    itemised_receipt += f"{name}: £{price:.2f}\n"
                    self.total += price
        text_sender.send_order_confirmation(to_number, from_number)
        return f"{itemised_receipt}Total: £{self.total:.2f}"
    

    def send_order_confirmation(self, to_number, from_number):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        delivery_time = (datetime.now() + timedelta(minutes = 45)).strftime('%H:%M')
        message_body = f"Thank you! Your order was placed and will be delivered by {delivery_time}"

        #sends text
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )

        #unique to each message
        return message.sid