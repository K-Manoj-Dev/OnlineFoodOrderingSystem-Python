class Cart:

    def __init__(self, items, choices):
        self.Choices = choices
        self.FoodItems = self.__AddtoCart(items)
        
    def __AddtoCart(self, items):
        foodDic = {}
        for choice in self.Choices:
            if choice > len(items) or choice <= 0:
                raise KeyError("Invalid choice number")
            if choice in foodDic:
                foodDic[choice] += 1
            else:
                foodDic[choice] = 1
        return foodDic
    
    def ProcessOrder(self, fooditems):
        total = 0
        for item in self.FoodItems:
            price = self.FoodItems[item] * fooditems[item-1].Price
            total += price
            print(f"{fooditems[item-1].Name} x {self.FoodItems[item]} = {price}")
        print(f"Total: {total}")

        self.ProcessPayment(total)

    def ProcessPayment(self, amount):
        print("\n--- Payment Options ---")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. UPI")
        print("4. Cash on Delivery")

        payment_choice = self.get_payment_choice()

        # Simulate a simple confirmation process
        confirmation = input("Confirm payment? (yes/no): ")
        if confirmation.lower() == "yes":
            print(f"Payment of {amount} successful using option {payment_choice}. Thank you for your order!")
        else:
            print("Payment canceled. Please choose a payment method again.")
            self.ProcessPayment(amount)

    def get_payment_choice(self):
        """Handles the user input for payment options."""
        while True:
            try:
                choice = int(input("Choose a payment method (1-4): "))
                if choice not in [1, 2, 3, 4]:
                    raise ValueError("Invalid payment choice, please choose between 1 and 4.")
                return choice
            except ValueError as e:
                print(e)
