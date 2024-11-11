from Models.FoodItem import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurant import Restaurant


class FoodManager:
    def __init__(self):
        self.Restaurants = self.__PrepareRestaurants()

    def __PrepareFoodItems(self):
        item1 = FoodItem("VegBiriyani", 4, 150, "***")
        item2 = FoodItem("ChickenBiriyani", 4.2, 200, "***")
        item3 = FoodItem("Parota", 4.1, 60, "***")
        item4 = FoodItem("Dosa", 4.5, 50, "***")
        item5 = FoodItem("Noodles", 3.8, 100, "***")
        return [item1, item2, item3, item4, item5]

    def __PrepareFoodMenus(self):
        food_items = self.__PrepareFoodItems()
        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [food_items[0], food_items[3]]  # Veg items
        menu2 = FoodMenu("Non-Veg")
        menu2.FoodItems = [food_items[1], food_items[2]]  # Non-veg items
        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [food_items[4]]  # Chinese item
        return [menu1, menu2, menu3]

    def __PrepareRestaurants(self):
        food_menus = self.__PrepareFoodMenus()

        res1 = Restaurant("A2B", 5, "Chennai", 10)
        res1.FoodMenus = [food_menus[0]]  # Veg menu
        res2 = Restaurant("Muniyandi Vilas", 4.9, "Bengaluru", 20)
        res2.FoodMenus = [food_menus[0], food_menus[1]]  # Veg and Non-Veg menus
        res3 = Restaurant("KFC", 4.8, "Coimbatore", 15)
        res3.FoodMenus = [food_menus[1], food_menus[2]]  # Non-Veg and Chinese menus
        return [res1, res2, res3]

    def FindRestaurant(self, name):
        for res in self.Restaurants:
            if res.Name.lower() == name.lower():
                return res
        print(f"No restaurant found with the name '{name}'.")
        return None
