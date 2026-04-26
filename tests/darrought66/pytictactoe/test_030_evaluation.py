import pytest

from darrought66.pytictactoe.GameState import GameState
from darrought66.pytictactoe.evaluation import *


@pytest.fixture
def gs_tie():
    gs = GameState.GameState()
    gs.spots[loc(0, 0)] = Player.X
    gs.spots[loc(0, 1)] = Player.O
    gs.spots[loc(0, 2)] = Player.O
    gs.spots[loc(1, 0)] = Player.O
    gs.spots[loc(1, 1)] = Player.X
    gs.spots[loc(1, 2)] = Player.X
    gs.spots[loc(2, 0)] = Player.O
    gs.spots[loc(2, 1)] = Player.X
    gs.spots[loc(2, 2)] = Player.O
    return gs


@pytest.fixture
def all_combos():
    gs = []

    ndx = 0
    gs.append(GameState.GameState())
    gs[ndx].spots[loc(0, 0)] = Player.X
    gs[ndx].spots[loc(0, 1)] = Player.X
    gs[ndx].spots[loc(0, 2)] = Player.X

    ndx = 1
    gs.append(GameState.GameState())
    gs[ndx].spots[loc(1, 0)] = Player.O
    gs[ndx].spots[loc(1, 1)] = Player.O
    gs[ndx].spots[loc(1, 2)] = Player.O

    ndx = 2
    gs.append(GameState.GameState())
    gs[ndx].spots[loc(2, 0)] = Player.X
    gs[ndx].spots[loc(2, 1)] = Player.X
    gs[ndx].spots[loc(2, 2)] = Player.X

    ndx = 3
    gs.append(GameState.GameState())
    gs[ndx].spots[loc(0, 0)] = Player.O
    gs[ndx].spots[loc(1, 0)] = Player.O
    gs[ndx].spots[loc(2, 0)] = Player.O

    ndx = 4
    gs.append(GameState.GameState())
    gs[ndx].spots[loc(0, 1)] = Player.X
    gs[ndx].spots[loc(1, 1)] = Player.X
    gs[ndx].spots[loc(2, 1)] = Player.X

    ndx = 5
    gs.append(GameState.GameState())
    gs[ndx].spots[loc(0, 2)] = Player.O
    gs[ndx].spots[loc(1, 2)] = Player.O
    gs[ndx].spots[loc(2, 2)] = Player.O

    ndx = 6
    gs.append(GameState.GameState())
    gs[ndx].spots[loc(0, 0)] = Player.X
    gs[ndx].spots[loc(1, 1)] = Player.X
    gs[ndx].spots[loc(2, 2)] = Player.X

    ndx = 7
    gs.append(GameState.GameState())
    gs[ndx].spots[loc(0, 2)] = Player.O
    gs[ndx].spots[loc(1, 1)] = Player.O
    gs[ndx].spots[loc(2, 0)] = Player.O

    return gs


def test_pot(all_combos):
    # X holds (0, 0) in combo 0
    assert pot(all_combos[0], loc(0, 0), Player.X) == Player.X
    assert pot(all_combos[0], loc(0, 0), Player.O) == Player.X
    # O holds (1, 1) in combo 1
    assert pot(all_combos[1], loc(1, 1), Player.X) == Player.O
    assert pot(all_combos[1], loc(1, 1), Player.O) == Player.O
    # (1, 0) is open in combo 0
    assert pot(all_combos[0], loc(1, 0), Player.X) == Player.X
    assert pot(all_combos[0], loc(1, 0), Player.O) == Player.O
    return


def eval_tie(gs_tie):
    assert eval_tie(gs_tie) == True
    return


def test_eval_row_col_diagonal(all_combos):
    assert eval_row(all_combos[0], 0, Player.X) == True
    assert eval_row(all_combos[1], 1, Player.O) == True
    assert eval_row(all_combos[2], 2, Player.X) == True
    assert eval_col(all_combos[3], 0, Player.O) == True
    assert eval_col(all_combos[4], 1, Player.X) == True
    assert eval_col(all_combos[5], 2, Player.O) == True
    assert eval_diagonal(all_combos[6], Player.X) == True
    assert eval_diagonal(all_combos[7], Player.O) == True

    # reverse player should be false
    assert eval_row(all_combos[0], 0, Player.O) == False
    assert eval_row(all_combos[1], 1, Player.X) == False
    assert eval_row(all_combos[2], 2, Player.O) == False
    assert eval_col(all_combos[3], 0, Player.X) == False
    assert eval_col(all_combos[4], 1, Player.O) == False
    assert eval_col(all_combos[5], 2, Player.X) == False
    assert eval_diagonal(all_combos[6], Player.O) == False
    assert eval_diagonal(all_combos[7], Player.X) == False

    return


def test_eval(all_combos):
    assert evaluate(all_combos[0]) == True
    assert all_combos[0].status == Status.X_WON
    assert all_combos[0].outcome == Outcome.WIN
    assert all_combos[0].range == Outcome.WIN

    assert evaluate(all_combos[1]) == True
    assert all_combos[1].status == Status.O_WON
    assert all_combos[1].outcome == Outcome.WIN
    assert all_combos[1].range == Outcome.WIN

    assert evaluate(all_combos[2]) == True
    assert all_combos[2].status == Status.X_WON
    assert all_combos[2].outcome == Outcome.WIN
    assert all_combos[2].range == Outcome.WIN

    assert evaluate(all_combos[3]) == True
    assert all_combos[3].status == Status.O_WON
    assert all_combos[3].outcome == Outcome.WIN
    assert all_combos[3].range == Outcome.WIN

    assert evaluate(all_combos[4]) == True
    assert all_combos[4].status == Status.X_WON
    assert all_combos[4].outcome == Outcome.WIN
    assert all_combos[4].range == Outcome.WIN

    assert evaluate(all_combos[5]) == True
    assert all_combos[5].status == Status.O_WON
    assert all_combos[5].outcome == Outcome.WIN
    assert all_combos[5].range == Outcome.WIN

    assert evaluate(all_combos[6]) == True
    assert all_combos[6].status == Status.X_WON
    assert all_combos[6].outcome == Outcome.WIN
    assert all_combos[6].range == Outcome.WIN

    assert evaluate(all_combos[7]) == True
    assert all_combos[7].status == Status.O_WON
    assert all_combos[7].outcome == Outcome.WIN
    assert all_combos[7].range == Outcome.WIN

    return
