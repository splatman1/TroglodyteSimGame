class Dragon:
    def __init__(self, name, player_viewable=True):
        self.quote = "Dragon go brrr"
        self.player_viewable = player_viewable
        self.name = name

    def search_for_player(self, player, backpack):
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
        player.died()



