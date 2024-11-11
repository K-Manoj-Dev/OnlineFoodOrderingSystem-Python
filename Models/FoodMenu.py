from AbstractItem import AbstractItem
from FoodItem import FoodItem

class FoodMenu(AbstractItem):

    def __init__(self, name):
        super().__init__(name)
        self.__FoodItems = []  # Private attribute to store FoodItems

    @property
    def FoodItems(self):
        return self.__FoodItems  # Getter to access FoodItems

    @FoodItems.setter
    def FoodItems(self, items):
        for item in items:
            if not isinstance(item, FoodItem):
                print("Invalid FoodItem...")
                return
        self.__FoodItems = items  # Setter to assign only valid FoodItems

    def DisplayItem(self, start):
        print(f"{start} => {self.Name}")
        for i, item in enumerate(self.__FoodItems, 1):
            print(f"   {i}. {item.Name} - Rating: {item.Rating} - Price: {item.Price}")
