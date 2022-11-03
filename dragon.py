class Dragon:
    def __init__(self, player_viewable=True):
        self.quote = "Dragon go brrr"
        self.player_viewable = player_viewable

    def search_for_player(self, player):
        if self.player_viewable:
            return self.quote and self.kill_player(player)
        if not self.player_viewable:
            return None

    def kill_player(self, player):
        player.is_alive = True



