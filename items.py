class Items:
    """The items is a basic class which holds information like is_collectable.
    Alot of what is held inside this class became redundant however I hope to return to this
    game and improve on it more. Potentially as a top down py game."""
    def __init__(self, item, collectable=True, readable=True, message=None, location=None, item_required=None):
        self.location = location
        self.item = item
        self.message = message
        self.is_collectable = collectable
        self.is_readable = readable
        self.requires_item = item_required


    def interpret_message(self):
        """This function is used to interpret a message within an item"""
        if self.is_readable:
            return self.message
        if not self.is_readable:
            print("object can't be interpreted")

    def detect_items(self, troglodyte_location):
        """This is an older function that isn't used however I believe it helps show my thought
        process for earlier designs/builds of this project."""
        if troglodyte_location == self.location:
            print(self.item)
