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
wilson_volleyball = Person()
floyd_collins = Person()
gollum = Person()
troglodyte = Troglodyte()
dragon = Dragon()
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
troglodyte.died()

