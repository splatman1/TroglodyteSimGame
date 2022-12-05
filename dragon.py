class Dragon:
    """This is my dragon class.
    This is a rather basic class however it does what is required of it and allowed me to
    work more in depth with instances and interacting with them."""
    def __init__(self, name, player_viewable=True):
        self.quote = "Dragon go brrr"
        self.player_viewable = player_viewable
        self.name = name

    def search_for_player(self, player, backpack):
        """The search_for_player function looks for the player in the dragons_room.
        It does this by detecting if the player is viewable.
        This class checks if the player is viewable by checking the players backpack for the_one_ring.
        If the players backpack does not contain the_one_ring they will be eliminated using the {self.kill_player}
        function which takes the instance of the troglodute and uses the inbuilt self.died function which prints a
        message to let the player know they lost aswell as ends the game with quit()"""
        result = backpack.in_backpack("the_one_ring")
        if result != "the_one_ring":
            player.player_viewable = False
        if player.player_viewable:
            print(self.quote)
            self.kill_player(player)
            quit()

        if player.player_viewable == False:
            print("Congratulations you escaped the cave!")
            quit()


    def kill_player(self, player):
        """kill_player is a @staticmethod that uses the troglodyte instance from main and
        calls the self.died method. """
        player.died()



