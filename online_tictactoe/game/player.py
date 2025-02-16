from dataclasses import dataclass

from online_tictactoe.game.player_place import PlayerPlace


@dataclass
class Player:
    name: str
    score: int = 0
    player_place: PlayerPlace | None = None

    def set_player_place(self, player_place: PlayerPlace):
        self.player_place = player_place