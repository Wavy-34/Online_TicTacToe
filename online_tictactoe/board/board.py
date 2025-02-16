from online_tictactoe.board.cell import Cell
from online_tictactoe.board.cell_state import CellState

class Board:

    def __init__(self, size: int, grid: list[list[Cell]]) -> None:
        self.board = grid
        self.size = size
        
    def get_cell_state(self, X: int, Y: int) -> CellState:
        return self.board[Y][X].state

    def set_cell_state(self, X: int, Y: int, state: CellState) -> None:
        self.board[Y][X].state = state

    def show_board(self) -> None:
        j = 0
        for row in self.board:
            j += 1
            i = 0
            for cell in row:
                i += 1
                if cell.state == CellState.EMPTY:
                    print(" ", end="")
                elif cell.state == CellState.PLAYER1:
                    print("O", end="")
                elif cell.state == CellState.PLAYER2:
                    print("X", end="")
                if not i == 3:
                    print("|", end="")
            print("")
            if not j == 3:
                print("─────")

def create_board(size, pattern: CellState | list[list[CellState]] = CellState.EMPTY) -> Board:
    if isinstance(pattern, CellState):
        grid = [[Cell(pattern) for i in range(size)] for j in range(size)]
    elif isinstance(pattern, list[list[CellState]]):
        print("Not implemented yet. Defaulting to empty Board")
        grid = [[Cell(CellState.EMPTY) for i in range(size)] for j in range(size)]
    board = Board(3, grid)
    return board

    