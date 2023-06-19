class Restaurant():
    def __init__(self):
        self.dishes = []
        self.menu = ""
    
    def add(self, dish):
        dish_dictionary = {}
        dish_dictionary[dish.name] = dish.price
        self.dishes.append(dish_dictionary)
    
    def view_formatted_menu(self):
        for dish in self.dishes:
            for name,price in dish.items():
                if dish == self.dishes[-1]:
                    self.menu += f"{name}: £{price:.2f}"
                else:
                    self.menu += f"{name}: £{price:.2f}\n"
        return self.menu
    
    def search(self, search_q):
        search_results = []
        split_menu = self.view_formatted_menu().split("\n")
        for item in split_menu:
            if search_q.lower() in item.lower():
                search_results.append(item)
        if len(search_results) < 1:
            raise Exception(f"Sorry, there is no {search_q} on the menu!")
        return "\n".join(search_results)