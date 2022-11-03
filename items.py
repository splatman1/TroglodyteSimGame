class Items:
    def __init__(self, item, collectable=True, readable=True, message=None, location=None):
        self.location = location
        self.item = item
        self.message = message
        self.is_collectable = collectable
        self.is_readable = readable

    def pick_up_item(self, location):
        if self.is_collectable:
            self.location = location
            return self.item
        if not self.is_collectable:
            print("object cannot be collected")

    def interpret_message(self):
        if self.is_readable:
            return self.message
        if not self.is_readable:
            print("object can't be interpreted")

    def detect_items(self, t):
