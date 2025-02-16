from online_tictactoe.schemas.board import from_state
from online_tictactoe.game.game import create_random_game
from online_tictactoe.game.player import Player
from online_tictactoe.schemas.cell_state import CellState


def main():
    player1 = Player("Player1's name")
    player2 = Player("Player2's name")
    board = from_state(3, CellState.EMPTY)
    game = create_random_game(player1, player2, board)
    game.start()
    print(f"{player1.score = }, {player2.score = }")


if __name__ == "__main__":
    main()
