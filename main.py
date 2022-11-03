from person import Person
from room import Room
from items import Items
from troglodyte import Troglodyte
from dragon import Dragon
"""Rooms"""
lake_room = Room("Lake Room")
floyds_room = Room("Floyd's Room")
wilsons_room = Room("Wilson's Room")
gollums_room = Room("Gollum's Room")
Outside = Room("Outside")
weapons_room = Room("Weapon's Room")
starting_room = Room("Starting_Room")
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
"""Game"""


