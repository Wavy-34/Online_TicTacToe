from dataclasses import dataclass

from online_tictactoe.game.game_status import GameStatus
from online_tictactoe.game.winner_type import WinnerType


@dataclass
class GameState:
    status: GameStatus
    winner: WinnerType