class Room:
    """The Class handles any character movements as well as any tracking required."""
    def __init__(self, room_name, north=None, east=None, south=None, west=None, characters = None,
                 item1=None, item2=None, item3=None, explored='', troglodyte_character=None):
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
        self.troglodyte_location = None
        self.room_requirement = None

    def find_directions(self, north_room=None, east_room=None, south_room=None, west_room=None):
        """This takes in the parameters north, east, south and west set_up in main and allocates
        what directions the character can move for each room."""
        self.north = north_room
        self.east = east_room
        self.south = south_room
        self.west = west_room

    def move_character(self, backpack):
        """This class is where most of my effort went.
        When the player enters option 5 they will be told which directions they can go.
        For instance, in the starting room the player will be told they can only go north.

        The troglodyte(Main Character) is setup using the current Room class which can be referenced due to
        the use of instances rather than multiple different classes.

        If the player chooses to go a direction where there is no door they will be met with
        a message that says I can't enter a room without a door.

        If the player chooses a valid option a message appears with you walk (player direction)

        It will then print you find yourself in (self.player_location)

        The move character function also checks if the character has entered the dragon room. If they
        enter the dragons_room without the required item it is already too late as any movement will get you killed.
        When you enter the dragon room, a function is called in the dragon class called search_for_player which checks
        if the player is viewable. If the player is viewable the player will be killed and will be met with a
        death screen. If the player has the_one_ring, then they will be able to get past the dragon and win.

        """
        self.troglodyte_location = Room
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
            print(f"You walk {choose_direction}\n")

            if self.room_name == "Dragon's_Room":
                self.characters.search_for_player(self.troglodyte_character, backpack)

            if choose_direction.lower() in north.lower():
                self.north.troglodyte_character = self.troglodyte_character
                self.troglodyte_location = self.north

            if choose_direction in east.lower():
                self.east.troglodyte_character = self.troglodyte_character
                self.troglodyte_location = self.east

            if choose_direction in south.lower():
                self.south.troglodyte_character = self.troglodyte_character
                self.troglodyte_location = self.south

            if choose_direction in west.lower():
                self.west.troglodyte_character = self.troglodyte_character
                self.troglodyte_location = self.west
            print(f"You find yourself in {self.troglodyte_location.room_name}")
            self.explored=self.room_name

    def remove_items(self):
        """This function removes all items within the room and is only called
        by the backpack class."""
        self.item1 = None
        self.item2 = None
        self.item3 = None

    def get_current_location(self):
        return self.troglodyte_location

    def search_room(self):
        """The search_room function looks for any items that may be in the room aswell as any characters that
        may be in the room.
        After this it prints "A wild {self.characters.name} appeared"
         as well as I see a {self.item1}{self.item2}{self.item3} which are set to empty strings by default.
          If there is nothing in the room it prints I see absolutely nothing using a weird technique I thought of."""
        item1 = 'bsolutely Nothing'
        item2 = ''
        item3 = ''

        if self.item1 is not None:
            item1 = " " + self.item1.item
        if self.item2 is not None:
            item2 = ", " + self.item2.item
        if self.item3 is not None:
            item3 = ", " + self.item3.item
        if self.characters is not None:
            print(f"A wild {str(self.characters.name)} appeared")
        print(f"I see a{item1}{item2}{item3} and I'm in a place called {self.room_name} weird name...")

    def pick_up_item(self, backpack):
        """Pick_up_item checks to see if there is a room requirement such as a fishing_rod and
        then checks what items are in the room and if they are pickable. If the item has no requirement
        and is pickable it is then retured as a list to the backpack class which adds them using the add function.
        If the room has an item requirement, it will print "I need a {self.room_requirement.item} to collect
        items in here. I better look around and find it." """
        if self.room_requirement is not None:
            print(f"I need a {self.room_requirement.item} to collect items in here.\n"
                  f"I better look around and find it.")
            backpack.sort()
            returned_item = backpack.in_backpack(self.room_requirement.item)
            if returned_item is not None:
                if returned_item == self.room_requirement.item:
                    items = []
                    items.append(self.item1)
                    self.item1 = None
                    self.room_requirement = None
                    return items
            return []

        if self.room_requirement is None:
            items = [self.item1, self.item2, self.item3]
            items_available = []
            for i in items:
                if i is not None:
                    if i.is_collectable:
                        items_available.append(i)
            return items_available










