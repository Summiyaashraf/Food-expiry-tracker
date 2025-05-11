from datetime import datetime, timedelta

class ExpiryManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_expired(self):
        today = datetime.today()
        return [item for item in self.items if item.expiry_date < today]

    def get_soon_expiring(self, days=3):
        today = datetime.today()
        return [item for item in self.items if 0 <= (item.expiry_date - today).days <= days]

    def get_all_items(self):
        return sorted(self.items, key=lambda x: x.expiry_date)
