from player import Player
from status import TreeStatus
from status import Status


# tests if any row, column or diagonal has been taken by either player. if so,
# then declares a WIN. then tests if any row, column or diagonal could still be
# taken. if not then declares a tie. in either case returns true. otherwise
# returns false
def evaluate(grid):
    if eval_diagonal(grid, Player.X):
        grid.status = Player.X
        grid.tree_status = TreeStatus.WIN
        return True

    if eval_diagonal(grid, Player.O):
        grid.status = Status.O_WON
        grid.tree_status = TreeStatus.WIN
        return True

    # each iteration checks one row and one column.
    for ndx in range(3):
        if eval_col(grid, ndx, Player.X) or eval_row(grid, ndx, Player.X):
            grid.status = Player.X
            grid.tree_status = TreeStatus.WIN
            return True
        if eval_col(grid, ndx, Player.O) or eval_row(grid, ndx, Player.O):
            grid.status = Status.O_WON
            grid.tree_status = TreeStatus.WIN
            return True

    # evaluate_tie assumes that no one has won yet.
    if evaluate_tie(grid):
        grid.status = Status.TIE
        grid.tree_status = TreeStatus.TIE

    return False


# tests if either diagonal has been taken by a player.
def eval_diagonal(grid, player):
    if grid.spots[(0, 0)] == grid.spots[(1, 1)] == grid.spots[(2, 2)] == player:
        return True
    if grid.spots[(2, 0)] == grid.spots[(1, 1)] == grid.spots[(0, 2)] == player:
        return True
    return False


# tests if a column has been taken by a player.
def eval_col(grid, ndx, player):
    if grid.spots[(ndx, 0)] == grid.spots[(ndx, 1)] == grid.spots[(ndx, 2)] == player:
        return True
    return False


# tests if a row has been taken by a player.
def eval_row(grid, ndx, player):
    if grid.spots[(0, ndx)] == grid.spots[(1, ndx)] == grid.spots[(2, ndx)] == player:
        return True
    return False


# tests if no row, column or diagonal can be taken by either player. assumes
# that no one has won yet. returns true if there is a tie.
def evaluate_tie(grid):
    # if either diagonal can be taken by either player then its not a tie.
    if eval_diagonal_tie(grid, Player.X) or eval_diagonal_tie(grid, Player.O):
        return False

    # if any row or column can be taken by either player then its not a tie.
    for ndx in range(3):
        if eval_col_tie(grid, ndx, Player.X) or eval_row_tie(grid, ndx, Player.X):
            return False
        if eval_col_tie(grid, ndx, Player.O) or eval_row_tie(grid, ndx, Player.O):
            return False

    return True


# tests if either diagonals can be taken by a player. returns true if a win is
# possible, which means that the game is not tied yet.
def eval_diagonal_tie(grid, player):
    if pot(grid, (0, 0), player) == pot(grid, (1, 1), player) == pot(grid, (2, 2), player) == player:
        return True

    if pot(grid, (2, 0), player) == pot(grid, (1, 1), player) == pot(grid, (0, 2), player) == player:
        return True

    # there might still be a tie
    return False


# tests if a column can be taken by a player. returns true if a win is possible,
# which means that the game is not tied yet.
def eval_col_tie(grid, ndx, player):
    if pot(grid, (ndx, 0), player) == pot(grid, (ndx, 1), player) == pot(grid, (ndx, 2), player) == player:
        return True

    # there might still be a tie
    return False


# tests if a row be taken by a player. returns true if a win is possible,
# which means that the game is not tied yet.
def eval_row_tie(grid, ndx, player):
    if pot(grid, (0, ndx), player) == pot(grid, (1, ndx), player) == pot(grid, (2, ndx), player) == player:
        return True

    # there might still be a tie
    return False


# returns player if the location has been claimed by player or is still unclaimed.
# otherwise returns open.
def pot(grid, location, player):
    t = grid.spots[location] == player or grid.spots[location] == Player.OPEN
    return player if t else Player.OPEN
