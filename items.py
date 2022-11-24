class Items:
    def __init__(self, item, collectable=True, readable=True, message=None, location=None, item_required=None):
        self.location = location
        self.item = item
        self.message = message
        self.is_collectable = collectable
        self.is_readable = readable
        self.requires_item = item_required


    def interpret_message(self):
        if self.is_readable:
            return self.message
        if not self.is_readable:
            print("object can't be interpreted")

    def detect_items(self, troglodyte_location):
        if troglodyte_location == self.location:
            print(self.item)
