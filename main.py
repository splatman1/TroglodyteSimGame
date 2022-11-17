from person import Person
from room import Room
from items import Items
from troglodyte import Troglodyte
from dragon import Dragon
from backpack import BackPack
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
wilson_volleyball = Person
floyd_collins = Person
gollum = Person
troglodyte = Troglodyte()
dragon = Dragon
"""Items"""
the_one_ring = Items("The One Ring")
knife = Items("Knife")
fish = Items("Fish")
fishing_rod = Items("Fishing Rod")
note = Items("note")
key = Items("Key")
id = Items("ID")
shopping_list = Items("Shopping List")
floyds_note = Items("Floyd's Note")
skeleton = Items("Skeleton")
map = Items("Map")
"""Backpack"""
backpack = BackPack(None)
"""Setup directions"""
starting_room.find_directions(wilsons_room)
skeletons_room.find_directions(floyds_room)
weapons_room.find_directions(gollums_room)
floyds_room.find_directions(lake_room, wilsons_room, skeletons_room)
wilsons_room.find_directions(dragons_room, gollums_room, starting_room, floyds_room)
gollums_room.find_directions(frodo_room, None, weapons_room, wilsons_room)
lake_room.find_directions(None, None, floyds_room)
dragons_room.find_directions(outside, None, wilsons_room)
frodo_room.find_directions(None, None, gollums_room, None)
"""Setup Character Locations"""
starting_room.troglodyte_character = troglodyte
wilsons_room.characters = wilson_volleyball
gollums_room.characters = gollum
floyds_room.characters = floyd_collins
dragons_room.characters = dragon
"""Setup Item Locations"""
starting_room.item1 = key
starting_room.item2 = id
starting_room.item3 = shopping_list
skeletons_room.item1 = skeleton
weapons_room.item1 = knife
gollum.item1 = the_one_ring
lake_room.item1 = fish
frodo_room.item1 = note
wilson_volleyball.item = fishing_rod
gollum.item = the_one_ring
"""Game options"""


"""Game Start"""
starting_room.troglodyte_character.print_slow(troglodyte.starting_message)


