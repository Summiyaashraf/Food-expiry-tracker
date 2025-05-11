import json
import os
from food_item import FoodItem

def save_to_file(filename, items):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        json.dump([item.to_dict() for item in items], f, indent=4)

def load_from_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [FoodItem.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
