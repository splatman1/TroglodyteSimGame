class Room:
    def __init__(self, room_name, north=None, east=None, south=None, west=None):
        self.room_name = room_name
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def find_directions(self, north_room=None, east_room=None, south_room=None, west_room=None):
        self.north = north_room
        self.east = east_room
        self.south = south_room
        self.west = west_room
