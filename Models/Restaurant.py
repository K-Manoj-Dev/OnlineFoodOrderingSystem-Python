from AbstractItem import AbstractItem
from FoodMenu import FoodMenu

class Restaurant(AbstractItem):

    def __init__(self, name, rating, location, offer):
        super().__init__(name, rating)
        self.Location = location
        self.Offer = offer
        self.__FoodMenus = []  # Private attribute to store FoodMenus

    @property
    def FoodMenus(self):
        return self.__FoodMenus  # Return the correct private attribute

    @FoodMenus.setter
    def FoodMenus(self, items):
        for item in items:
            if not isinstance(item, FoodMenu):
                print("Invalid FoodMenu...")
                return
        self.__FoodMenus = items  # Set the private attribute with valid items

    def DisplayItem(self, start):
        print(f">> {start} => {self.Name} => Rating : {self.Rating}")
