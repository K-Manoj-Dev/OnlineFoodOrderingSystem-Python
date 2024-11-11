from .FoodManager import FoodManager
from Models.Cart import Cart
from Models import FoodManager




class MainMenu:

    __Options = {1: "Show Restaurant", 2: "Show Food", 3: "Search Restaurant", 4: "Search FoodItem", 5: "Logout"}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurants(self):
        for i, res in enumerate(self.__FoodManager.Restaurants, 1):
            res.DisplayItem(i)
        
        choice = self.get_valid_choice("Please Select the Restaurant: ", len(self.__FoodManager.Restaurants))
        res = self.__FoodManager.Restaurants[choice - 1]
        self.ShowFoodMenus(res.FoodMenus)

    def ShowFoodItems(self, foodItems=None):
        if foodItems is not None:
            for i, foodItem in enumerate(foodItems, 1):
                foodItem.DisplayItem(i)
            
            choices = self.get_valid_choices("Please Choose your Food Items (e.g., 1,2): ", len(foodItems))
            cart = Cart(foodItems, choices)
            cart.ProcessOrder(foodItems)
        else:
            print("No food items available.")

    def SearchRestaurant(self):
        resName = input("Enter Restaurant Name: ")
        res = self.__FoodManager.FindRestaurant(resName)

        if res is not None:
            print("Restaurant Found....")
            print(f"Name: {res.Name}, Rating: {res.Rating}")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"No Restaurant found with the name '{resName}'")

    def SearchFoodItem(self):
        itemName = input("Enter Food Item Name to Search: ")
        foundItems = []
        
        for res in self.__FoodManager.Restaurants:
            for menu in res.FoodMenus:
                for foodItem in menu.FoodItems:
                    if itemName.lower() in foodItem.Name.lower():
                        foundItems.append(foodItem)

        if foundItems:
            print(f"Food items found for '{itemName}':")
            self.ShowFoodItems(foundItems)
        else:
            print(f"No food items found with the name '{itemName}'")

    def ShowFoodMenus(self, menus):
        print("List of Menus Available:")
        for i, menu in enumerate(menus, 1):
            menu.DisplayItem(i)
        
        choice = self.get_valid_choice("Please Choose a Menu: ", len(menus))
        fooditems = menus[choice - 1].FoodItems
        self.ShowFoodItems(fooditems)

    def Start(self):
        while True:
            for option in MainMenu.__Options:
                print(f"{option}. {MainMenu.__Options[option]}", end="  ")
            print()

            try:
                choice = int(input("Please Enter Your Choice: "))
                if choice in MainMenu.__Options:
                    method_name = MainMenu.__Options[choice].replace(" ", "")
                    getattr(self, method_name)()
                else:
                    raise KeyError
            except (ValueError, KeyError):
                print("Invalid Input. Please Enter a Valid Choice.")

    def get_valid_choice(self, prompt, max_value):
        """Helper method to ensure valid input within a given range."""
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= max_value:
                    return choice
                else:
                    print(f"Please select a valid option between 1 and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_valid_choices(self, prompt, max_value):
        """Helper method to ensure multiple valid choices."""
        while True:
            try:
                choices = list(map(int, input(prompt).split(',')))
                if all(1 <= choice <= max_value for choice in choices):
                    return choices
                else:
                    print(f"Please select valid options between 1 and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a comma-separated list of numbers.")
