from dataclasses import dataclass

from online_tictactoe.schemas.game_status import GameStatus
from online_tictactoe.schemas.winner_type import WinnerType


@dataclass
class GameState:
    status: GameStatus
    winner: WinnerType
