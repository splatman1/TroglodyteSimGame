from troglodyte import Troglodyte
class Dragon:
    def __init__(self, name, player_viewable=True):
        self.quote = "Dragon go brrr"
        self.player_viewable = player_viewable
        self.name = name

    def search_for_player(self, player):
        if self.player_viewable:
            print(self.quote)
            self.kill_player(player)
            print("YOU DIED")

    def kill_player(self, player):
        player.died()



