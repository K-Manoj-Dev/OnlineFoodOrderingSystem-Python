from Models.AbstractItem import AbstractItem


class FoodItem(AbstractItem):
    
    def __init__(self, name, rating, price, description):
        super().__init__(name, rating)
        self.Price = self.validate_price(price)
        self.Description = description

    def validate_price(self, price):
        """Ensure the price is a positive value."""
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        return price

    def DisplayItem(self, start):
        print(f"{start} => Name: {self.Name}, Price: {self.Price}, Rating: {self.Rating}, Description: {self.Description}")

    def __str__(self):
        return f"{self.Name} - {self.Rating} stars, {self.Price} INR"
