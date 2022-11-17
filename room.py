class Room:
    def __init__(self, room_name, north=None, east=None, south=None, west=None, characters = None,
                 item1=None, item2=None, item3=None, explored=False, troglodyte_character=None):
        self.explored = explored
        self.room_name = room_name
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.characters = characters
        self.troglodyte_character = troglodyte_character

    def find_directions(self, north_room=None, east_room=None, south_room=None, west_room=None):
        self.north = north_room
        self.east = east_room
        self.south = south_room
        self.west = west_room

    def move_character(self):
        north = ''
        east = ''
        south = ''
        west = ''
        if self.north != None:
            north = " North"
        if self.east != None:
            east = " East"
        if self.south != None:
            south = " South"
        if self.west != None:
            west = " West"
        direction_options = (f"I can move{north} {east} {south} {west}")
        print(direction_options)
        choose_direction = input("Where should I go: ").lower()
        if choose_direction not in direction_options.lower():
            print("I can't enter a room without a door")
        if choose_direction in direction_options.lower():
            if choose_direction == north.lower():
                self.north.troglodyte_character = self.troglodyte_character
                return self.north
            if choose_direction == east.lower():
                self.east.troglodyte_character = self.troglodyte_character
            if choose_direction == south.lower():
                self.south.troglodyte_character = self.troglodyte_character
            if choose_direction == west.lower():
                self.west.troglodyte_character = self.troglodyte_character
            self.troglodyte_character = None
            return self.north


    def search_room(self):
        item1 = None
        item2 = None
        item3 = None

        if self.item1 != None:
            item1 = self.item1.item
        if self.item2 != None:
            item2 = self.item2.item
        if self.item3 != None:
            item3 = self.item3.item
        if self.characters != None:
            print(f"A wild {str(self.characters.name)} appeared")

        print(f"I see a {item1}, {item2}, {item3} and I'm in a place called {self.room_name} weird name...")

        if self.characters.name == "dragon":
            self.characters.search_for_player(self.troglodyte_character)
        self.explored = True









