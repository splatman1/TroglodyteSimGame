import time
from person import Person
from room import Room
from items import Items
from troglodyte import Troglodyte
from dragon import Dragon
from backpack import BackPack
"""This is where I use my room class to setup different instances of rooms.
It takes in the name of the room and other optional requirements"""

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
"""This is my the instance of my backpack class"""
backpack = BackPack()
"""This is where I setup the instances of my characters. They take in a quote as well as the name of the character."""
wilson_volleyball = Person("Wilson the volleyball", " What are you doing here?...\n"
                                                    " Never mind I don't really care. Ever since I lost\n"
                                                    " my main man Forrest Gump to the cruel mistress to the sea\n"
                                                    " life has been so miserable. Anyway here have a fishing rod.")
floyd_collins = Person("floyd collins", "Hi, my name is Floyd Collins. Ive been stuck under this rock for \n"
                                        "a long time and I don't want to get laughed at by my brother.\n"
                                        "The lake is north of here, but help a man out and end my suffering.")
gollum = Person("gollum", "Misery misery! Hobbits won’t kill us, nice hobbits. My precioussssssssss. \n"
                          "Oh it's you Baggins. My precious means everything to me, but I\n"
                          "would be happy to trade my precious for a fish. It will also let you get through \n"
                          "the dragons room. ")

"""This is my main character which has it's own class called Troglodyte"""
troglodyte = Troglodyte(backpack)
"""This is the dragon or the final boss. You can't get past him unless you have the one ring which makes you 
invisible."""
dragon = Dragon("dragon")

"""This is where I initialise all of my items
It takes a name and can optionally take a is pickable option/"""
the_one_ring = Items("The One Ring")
knife = Items("Knife")
fish = Items("Fish")
fishing_rod = Items("Fishing Rod")
note = Items("note")
key = Items("Key")
id = Items("ID")
shopping_list = Items("Shopping List")
floyds_note = Items("Floyd's Note")
skeleton = Items("Skeleton", False)
map = Items("Map")
"""This is how I setup the Directions for each room such as if you can go North, East, South or West.
The parameters are north_room, east_room, south_room and west_room."""
starting_room.find_directions(wilsons_room)
skeletons_room.find_directions(floyds_room)
weapons_room.find_directions(gollums_room)
floyds_room.find_directions(lake_room, wilsons_room, skeletons_room)
wilsons_room.find_directions(dragons_room, gollums_room, starting_room, floyds_room)
gollums_room.find_directions(frodo_room, None, weapons_room, wilsons_room)
lake_room.find_directions(None, None, floyds_room)
dragons_room.find_directions(outside, None, wilsons_room)
frodo_room.find_directions(None, None, gollums_room, None)
"""This is where I setup each room or each characters requirements to unlock or interact sort of like a key.
In this game gollum wants a fish, the lake room requires a fishing rod and the dragon room requires a key."""
gollum.item_wanted = True
gollum.item_name_wanted = fish
lake_room.room_requirement = fishing_rod
dragons_room.room_requirement = key
"""This is where I setup my characters locations.
The parameter is an instance of a  character class."""
starting_room.troglodyte_character = troglodyte
wilsons_room.characters = wilson_volleyball
gollums_room.characters = gollum
floyds_room.characters = floyd_collins
dragons_room.characters = dragon
"""This is where I setup my item locations.
The parameter is an instance of an item class"""
starting_room.item1 = key
starting_room.item2 = id
starting_room.item3 = shopping_list
skeletons_room.item1 = skeleton
weapons_room.item1 = knife
lake_room.item1 = fish
frodo_room.item1 = note
wilson_volleyball.item = fishing_rod
gollum.tradable_item = the_one_ring
"""This is the first message the player will see and is the introduction to the story."""
troglodyte.print_slow("Welcome You are playing --Troglodyte Sim-- the video game.\n\n"
                      ""
                      "Since ancient times man has always taken an interest in caves.\n"
                      "Be it for shelter, paintings, tragedies or mysteries caves have touched every part of History.\n"
                      "The way I look at it, this game isn't a game, but a love letter to all things cave.\n"
                      ""
                      "The player will be given 5 options when they first begin. These will include\n"
                      "Search room\n"
                      "talk to characters\n"
                      "check backpack\n"
                      "pick up items \n"
                      "and move character\n"
                      "For move character you must enter North East South or West or the first letter if\n"
                      "you wish to be lazy... Totally get it if you want to though.\n\n"
                      "The aim of this game is to get outside, however this requires the player to collect a few items\n"
                      "You must first get a Fishing Rod, then a Fish and then The One Ring to get past the dragon.\n"
                      "Good luck to you player and may your journey be safe and plentiful\n")
time.sleep(3)

troglodyte.print_slow(troglodyte.starting_message)
"""This sets up the character location and the starting message."""
troglodyte_location = starting_room
starter_message = "\nYou find yourself in " + (troglodyte_location.room_name.replace("_", " "))+"\n"
Troglodyte.print_slow(troglodyte, starter_message)
while True:
    """This prints the characters location each time they enter an option."""
    character_options = troglodyte.character_options()
    """The player is given 5 options for everywhere they go. 
    These options are: 
    search_room, ask_character_question, show_items_in_bag, collect_items and move_character"""

    if character_options == 1:
        troglodyte_location.search_room()

    if character_options == 2:
        if troglodyte_location.characters != None:
            troglodyte_location.troglodyte_character.ask_character_question(troglodyte_location.characters.name)
            troglodyte_location.characters.talk_to_character(troglodyte_location.characters,
                                                             troglodyte_location.troglodyte_character.backpack)
        if troglodyte_location.characters == None:
            print("No characters are in your area!")

    if character_options == 3:
        troglodyte_location.troglodyte_character.backpack.list()
    if character_options == 4:
        items = troglodyte_location.pick_up_item(troglodyte_location.troglodyte_character.backpack)
        troglodyte_location.troglodyte_character.backpack.add(troglodyte_location, items)
    if character_options == 5:
        troglodyte_location.move_character(troglodyte_location.troglodyte_character.backpack)
        troglodyte_location = troglodyte_location.get_current_location()
        """This is a map, it prints the locations the player has been to."""

    print(f"[{lake_room.explored}], [{dragons_room.explored}], [{frodo_room.explored}]\n"
          f"[{floyds_room.explored}], [{wilsons_room.explored}], [{gollums_room.explored}]\n"
          f"[{skeletons_room.explored}], [{starting_room.explored}], [{weapons_room.explored}]\n"
          f"This is your map")

