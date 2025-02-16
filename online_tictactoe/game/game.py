from dataclasses import dataclass
from random import choice
from online_tictactoe.board.board import Board
from online_tictactoe.board.cell_state import CellState
from online_tictactoe.game.error import NoWinnersFound, WinnerTypeNotImplemented
from online_tictactoe.game.game_status import GameStatus
from online_tictactoe.game.player import Player
from online_tictactoe.game.player_place import PlayerPlace
from online_tictactoe.game.winner_type import WinnerType

cell_to_xy_pos: dict[int, tuple[int, int]] = {
    0: (0,0),
    1: (1,0),
    2: (2,0),
    3: (0,1),
    4: (1,1),
    5: (2,1),
    6: (0,2),
    7: (1,2),
    8: (2,2)
}

@dataclass
class Game:
    turn: Player
    player1: Player
    player2: Player
    board: Board
    
    def show_board(self):
        self.board.show_board()

    def play_on_cell(self, player: Player, cell_posx: int, cell_posy) -> bool:
        if self.board.get_cell_state(cell_posx, cell_posy) == CellState.EMPTY:
            if player.player_place == PlayerPlace.PLAYER1:
                self.board.set_cell_state(cell_posx, cell_posy, CellState.PLAYER1)
            else:
                self.board.set_cell_state(cell_posx, cell_posy, CellState.PLAYER2)
            print(self.board.get_cell_state(cell_posx, cell_posy))
            return True
        else:
            print("Cell already full")
            return False
        
    def start(self):
        print(self.board.get_cell_state(0,0))
        self.show_board()
        self.take_turn(self.turn)

    def take_turn(self, player: Player):
        cell = int(input(f"{player.name} Which cell do you want to play in (0 is the top left 3 the middle left and 8 the bottom right):"))
        cell_posx, cell_posy = cell_to_xy_pos[cell]

        if self.play_on_cell(player, cell_posx, cell_posy):
            if player == self.player1:
                self.turn = self.player2
            else:
                self.turn = self.player1
        self.show_board()

        if not self.status == GameStatus.OVER:
            self.take_turn(self.turn)
        else:
            print(f"{self.winner.name} won !")
            self.winner.score += 1


    @property
    def winner(self) -> Player:
        if not self.is_over:
            raise NoWinnersFound(f"Calling .winner attr when game is not over")

        if self.winner_type == WinnerType.PLAYER1:
            if self.player1.player_place == PlayerPlace.PLAYER1:
                return self.player1
            else:
                return self.player2
        elif self.winner_type == WinnerType.PLAYER2:
            if self.player1.player_place == PlayerPlace.PLAYER2:
                return self.player1
            else:
                return self.player2
        else:
            raise WinnerTypeNotImplemented(f"Winner type {self.winner_type} not implemented")    

    @property
    def winner_type(self) -> WinnerType:
        for i in range(len(self.board.board)):
            if self.board.get_cell_state(i,0) == self.board.get_cell_state(i,1) == self.board.get_cell_state(i,2) != CellState.EMPTY:
                return WinnerType.PLAYER1 if self.board.get_cell_state(i,0) == CellState.PLAYER1 else WinnerType.PLAYER2
            
        for i in range(len(self.board.board)):
            if self.board.get_cell_state(0,i) == self.board.get_cell_state(1,i) == self.board.get_cell_state(2,i) != CellState.EMPTY:
                return WinnerType.PLAYER1 if self.board.get_cell_state(0,i) == CellState.PLAYER1 else WinnerType.PLAYER2
                
        if self.board.get_cell_state(0,0) == self.board.get_cell_state(1,1) == self.board.get_cell_state(2,2) != CellState.EMPTY:
            return WinnerType.PLAYER1 if self.board.get_cell_state(0,0) == CellState.PLAYER1 else WinnerType.PLAYER2
        
        if self.board.get_cell_state(0,2) == self.board.get_cell_state(1,1) == self.board.get_cell_state(2,0) != CellState.EMPTY:
            return WinnerType.PLAYER1 if self.board.get_cell_state(0,2) == CellState.PLAYER1 else WinnerType.PLAYER2
        return WinnerType.DRAW

    @property
    def is_board_full(self) -> bool:
        return all(cell.state != CellState.EMPTY for row in self.board.board for cell in row)

    @property
    def status(self) -> GameStatus:
        if self.winner_type != WinnerType.DRAW or self.is_board_full:
            return GameStatus.OVER
        return GameStatus.ONGOING
    
    @property
    def is_over(self) -> bool:
        return self.status == GameStatus.OVER


def create_random_game(player1: Player, player2: Player, board: Board) -> Game:
    turn = choice((player1,player2))
    if turn == player1:
        player1.set_player_place(PlayerPlace.PLAYER1)
        player2.set_player_place(PlayerPlace.PLAYER2)
    else:
        player1.set_player_place(PlayerPlace.PLAYER2)
        player2.set_player_place(PlayerPlace.PLAYER1)
    game = Game(turn, player1, player2, board)
    return game