from online_tictactoe.board.cell_state import CellState


class Cell:
    def __init__(self, state: CellState) -> None:
        self.state: CellState = state