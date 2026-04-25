from darrought66.tic_tac_toe import GameState
from darrought66.tic_tac_toe.Outcome import Outcome
from darrought66.tic_tac_toe.Player import Player
from darrought66.tic_tac_toe.Status import Status
from darrought66.tic_tac_toe.location import loc


# called during GameState construction to assign outcome, range and status for terminal game states. now status only
# has a value for terminal states. outcome and range for non-terminal states are assigned later, after the tree has
# been fully assembled.

# tests if any row, column or diagonal has been taken by either player. if so, then declares a WIN. then tests if any
# row, column or diagonal could still be taken. if not then declares a tie. in either case returns true. otherwise
# returns false
def evaluate(gs: GameState.GameState) -> bool:
    # evaluate diagonals for a win
    if eval_diagonal(gs, Player.X):
        gs.status = Status.X_WON
        gs.outcome = Outcome.WIN
        gs.range = Outcome.WIN
        return True
    if eval_diagonal(gs, Player.O):
        gs.status = Status.O_WON
        gs.outcome = Outcome.WIN
        gs.range = Outcome.WIN
        return True

    # each iteration checks one row and one column.
    for ndx in range(3):
        if eval_col(gs, ndx, Player.X) or eval_row(gs, ndx, Player.X):
            gs.status = Status.X_WON
            gs.outcome = Outcome.WIN
            gs.range = Outcome.WIN
            return True
        if eval_col(gs, ndx, Player.O) or eval_row(gs, ndx, Player.O):
            gs.status = Status.O_WON
            gs.outcome = Outcome.WIN
            gs.range = Outcome.WIN
            return True

    # evaluate_tie assumes that no one has won yet.
    if evaluate_tie(gs):
        gs.status = Status.TIE
        gs.outcome = Outcome.TIE
        gs.range = Outcome.TIE

    return False


# tests if either diagonal has been taken by a player.
def eval_diagonal(gs: GameState.GameState, player: Player) -> bool:
    if gs.spots[loc(0, 0)] == gs.spots[loc(1, 1)] \
            == gs.spots[loc(2, 2)] == player:
        return True
    if gs.spots[loc(2, 0)] == gs.spots[loc(1, 1)] \
            == gs.spots[loc(0, 2)] == player:
        return True
    return False


# tests if a column has been taken by a player.
def eval_col(gs: GameState.GameState, col: int, player: Player) -> bool:
    if gs.spots[loc(0, col)] == gs.spots[loc(1, col)] \
            == gs.spots[loc(2, col)] == player:
        return True
    return False


# tests if a row has been taken by a player.
def eval_row(gs: GameState.GameState, row: int, player: Player) -> bool:
    if gs.spots[loc(row, 0)] == gs.spots[loc(row, 1)] \
            == gs.spots[loc(row, 2)] == player:
        return True
    return False


# tests if no row, column or diagonal can be taken by either player. assumes that no one has won yet. returns true if
# there is a tie.
def evaluate_tie(gs: GameState.GameState) -> bool:
    # if either diagonal can be taken by either player then it is not a tie.
    if eval_diagonal_tie(gs, Player.X) or eval_diagonal_tie(gs, Player.O):
        return False

    # if any row or column can be taken by either player then it is not a tie.
    for ndx in range(3):
        if eval_col_tie(gs, ndx, Player.X) or eval_row_tie(gs, ndx, Player.X):
            return False
        if eval_col_tie(gs, ndx, Player.O) or eval_row_tie(gs, ndx, Player.O):
            return False

    return True


# tests if either diagonals can be taken by a player. returns true if a win is possible, which means that the game is
# not tied yet.
def eval_diagonal_tie(gs: GameState.GameState, player: Player) -> bool:
    if pot(gs, loc(0, 0), player) \
            == pot(gs, loc(1, 1), player) \
            == pot(gs, loc(2, 2), player) == player:
        return True

    if pot(gs, loc(2, 0), player) \
            == pot(gs, loc(1, 1), player) \
            == pot(gs, loc(0, 2), player) == player:
        return True

    # there might still be a tie
    return False


# tests if a column can be taken by a player. returns true if a win is possible, which means that the game is not tied
# yet.
def eval_col_tie(gs: GameState.GameState, col: int, player: Player) -> bool:
    if pot(gs, loc(col, 0), player) \
            == pot(gs, loc(col, 1), player) \
            == pot(gs, loc(col, 2), player) == player:
        return True

    # there might still be a tie
    return False


# tests if a row be taken by a player. returns true if a win is possible,
# which means that the game is not tied yet.
def eval_row_tie(gs: GameState.GameState, row: int, player: Player) -> bool:
    if pot(gs, loc(0, row), player) \
            == pot(gs, loc(1, row), player) \
            == pot(gs, loc(2, row), player) == player:
        return True

    # there might still be a tie
    return False


# returns opposite player if that player is holding the spot. otherwise returns current player. "pot" is "potentially".
def pot(gs: GameState.GameState, location: int, player: Player) -> Player:
    return player.opposite() if gs.spots[location] == player.opposite() else player
