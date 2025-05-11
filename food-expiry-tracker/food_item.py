from datetime import datetime

class FoodItem:
    def __init__(self, name, quantity, expiry_date, category):
        self.name = name
        self.quantity = quantity
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")
        self.category = category

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "expiry_date": self.expiry_date.strftime("%Y-%m-%d"),
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        return FoodItem(
            data["name"],
            data["quantity"],
            data["expiry_date"],
            data["category"]
        )
