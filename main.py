import time
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
wilson_volleyball = Person("Wilson the volleyball", " What are you doing here?...\n"
                                                    " Never mind I don't really care. Ever since I lost\n"
                                                    " my main man Forrest Gump to the cruel mistress to the sea\n"
                                                    " life has been so miserable. Anyway here have a fishing rod.")
floyd_collins = Person("floyd collins", "Hi, my name is Floyd Collins. Ive been stuck under this rock for \n"
                                        "a long time and I don't want to get laughed at by my brother.\n"
                                        "The lake is north of here, but help a man out and end my suffering.")
gollum = Person("gollum", "Misery misery! Hobbits won’t kill us, nice hobbits. My precious. \n"
                          "Oh it's you Baggins. My precious means everything to me, but I\n"
                          "would be happy to trade my precious for a fish. ")
troglodyte = Troglodyte()
dragon = Dragon("dragon")
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
troglodyte_location = starting_room
troglodyte.print_slow(troglodyte.starting_message)
"""Game setup"""
while True:
    character_options = troglodyte.character_options()
    if character_options == 1:
        troglodyte_location.search_room()
    if character_options == 2:
        character_choice = input("What character do you want to talk to? ")
        troglodyte.ask_character_question(character_choice)
    if character_options == 3:
        pass
    if character_options == 4:
        pass
    if character_options == 5:
        troglodyte_location = troglodyte_location.move_character()

