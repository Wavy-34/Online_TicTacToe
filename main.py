from online_tictactoe.board.board import create_board
from online_tictactoe.game.game import create_random_game
from online_tictactoe.game.player import Player


def main():
    player1 = Player("Player1's name")
    player2 = Player("Player2's name")
    board = create_board(3)
    game = create_random_game(player1, player2, board)
    game.start()
    print(f"{player1.score = }, {player2.score = }")

if __name__ == "__main__":
    main()
