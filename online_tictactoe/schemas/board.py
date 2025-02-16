from online_tictactoe.schemas.cell_state import CellState


class Board:

    def __init__(self, grid: list[list[CellState]]) -> None:
        self.board = grid

    def get_cell_state(self, X: int, Y: int) -> CellState:
        return self.board[Y][X]

    def set_cell_state(self, X: int, Y: int, state: CellState) -> None:
        self.board[Y][X] = state

    def show_board(self) -> None:
        j = 0
        for row in self.board:
            j += 1
            i = 0
            for cell_state in row:
                i += 1
                if cell_state is CellState.EMPTY:
                    print(" ", end="")
                elif cell_state is CellState.PLAYER1:
                    print("O", end="")
                elif cell_state is CellState.PLAYER2:
                    print("X", end="")
                if not i == 3:
                    print("|", end="")
            print("")
            if not j == 3:
                print("─────")


def from_state(size: int, cell_state: CellState) -> Board:
    grid = grid = [[cell_state for _ in range(size)] for _ in range(size)]
    return Board(grid)


def from_pattern(pattern: list[list[CellState]]) -> Board:
    return Board(pattern)
