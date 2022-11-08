from person import Person
from room import Room
from items import Items
from troglodyte import Troglodyte
from dragon import Dragon
"""Rooms"""
starting_room = Room("Starting_Room")
lake_room = Room("Lake Room")
floyds_room = Room("Floyd's Room")
wilsons_room = Room("Wilson's Room")
gollums_room = Room("Gollum's Room")
outside = Room("Outside")
weapons_room = Room("Weapon's Room")
dragons_room = Room("Dragon's_Room")
skeletons_room = Room("Skeleton's Room")
frodo_room = Room("Frodo's Room")
"""Characters"""
wilson_volleyball = Person(wilsons_room, "Hi young Troglodyte, what are you doing here?....\n"
                                         "Never mind, I dont really care.\n"
                                         " Ever since I lost my best friend to sea life has been miserable.\n "
                                         "I hope his marriage is more stable than his raft. \n"
                                         "anyway here is a fishing rod. I don't have arms so I sort of \n"
                                         "stare at it wishing for the sweet release of death.")

floyd_collins = Person(floyds_room)
gollum = Person(gollums_room)
troglodyte = Troglodyte(starting_room)
dragon = Dragon(dragons_room)
"""Items"""
the_one_ring = Items("The One Ring", gollum)
knife = Items("Knife", skeletons_room)
fish = Items("Fish", lake_room)
fishing_rod = Items("Fishing Rod", wilsons_room)
note = Items("note", frodo_room)
key = Items("Key", starting_room)
id = Items("ID", starting_room)
shopping_list = Items("Shopping List", starting_room)
floyds_note = Items("Floyd's Note", floyds_room)
skeleton = Items("Skeleton", skeletons_room)
map = Items("Map", wilsons_room)
"""Setup locations"""
starting_room.find_directions(wilsons_room)
skeletons_room.find_directions(floyds_room)
weapons_room.find_directions(gollums_room)
floyds_room.find_directions(lake_room, wilsons_room, skeletons_room)
wilsons_room.find_directions(dragons_room, gollums_room, starting_room, floyds_room)
gollums_room.find_directions(frodo_room, None, weapons_room, wilsons_room)
lake_room.find_directions(None, None, floyds_room)
dragons_room.find_directions(outside, None, wilsons_room)
frodo_room.find_directions(None, None, gollums_room, None)
"""Game"""
troglodyte.print_slow(troglodyte.starting_message)
print("\n")
troglodyte.print_slow("You find yourself in a cave. You have no idea who you are\n"
                      "and no idea how you got here.")
starting_room
