import pytest

from darrought66.pytictactoe.GameState import GameState as GameStateClass
from darrought66.pytictactoe.evaluation import *


@pytest.fixture
def gs_tie():
    gs = GameStateClass()
    gs.play_area[loc(0, 0)] = Player.X
    gs.play_area[loc(0, 1)] = Player.O
    gs.play_area[loc(0, 2)] = Player.O
    gs.play_area[loc(1, 0)] = Player.O
    gs.play_area[loc(1, 1)] = Player.X
    gs.play_area[loc(1, 2)] = Player.X
    gs.play_area[loc(2, 0)] = Player.O
    gs.play_area[loc(2, 1)] = Player.X
    gs.play_area[loc(2, 2)] = Player.O
    return gs


@pytest.fixture
def all_combos():
    gs = []

    ndx = 0
    # pycharm insists on GameState.GameState(), even though it flags it as an error.
    # otherwise is reports "TypeError: 'module' object is not callable"
    # work around is to rename the class GameStateClass
    gs.append(GameStateClass())
    gs[ndx].play_area[loc(0, 0)] = Player.X
    gs[ndx].play_area[loc(0, 1)] = Player.X
    gs[ndx].play_area[loc(0, 2)] = Player.X

    ndx = 1
    gs.append(GameStateClass())
    gs[ndx].play_area[loc(1, 0)] = Player.O
    gs[ndx].play_area[loc(1, 1)] = Player.O
    gs[ndx].play_area[loc(1, 2)] = Player.O

    ndx = 2
    gs.append(GameStateClass())
    gs[ndx].play_area[loc(2, 0)] = Player.X
    gs[ndx].play_area[loc(2, 1)] = Player.X
    gs[ndx].play_area[loc(2, 2)] = Player.X

    ndx = 3
    gs.append(GameStateClass())
    gs[ndx].play_area[loc(0, 0)] = Player.O
    gs[ndx].play_area[loc(1, 0)] = Player.O
    gs[ndx].play_area[loc(2, 0)] = Player.O

    ndx = 4
    gs.append(GameStateClass())
    gs[ndx].play_area[loc(0, 1)] = Player.X
    gs[ndx].play_area[loc(1, 1)] = Player.X
    gs[ndx].play_area[loc(2, 1)] = Player.X

    ndx = 5
    gs.append(GameStateClass())
    gs[ndx].play_area[loc(0, 2)] = Player.O
    gs[ndx].play_area[loc(1, 2)] = Player.O
    gs[ndx].play_area[loc(2, 2)] = Player.O

    ndx = 6
    gs.append(GameStateClass())
    gs[ndx].play_area[loc(0, 0)] = Player.X
    gs[ndx].play_area[loc(1, 1)] = Player.X
    gs[ndx].play_area[loc(2, 2)] = Player.X

    ndx = 7
    gs.append(GameStateClass())
    gs[ndx].play_area[loc(0, 2)] = Player.O
    gs[ndx].play_area[loc(1, 1)] = Player.O
    gs[ndx].play_area[loc(2, 0)] = Player.O

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
    assert all_combos[0].minimax == Outcome.WIN
    assert all_combos[0].lookahead == Outcome.WIN

    assert evaluate(all_combos[1]) == True
    assert all_combos[1].status == Status.O_WON
    assert all_combos[1].minimax == Outcome.WIN
    assert all_combos[1].lookahead == Outcome.WIN

    assert evaluate(all_combos[2]) == True
    assert all_combos[2].status == Status.X_WON
    assert all_combos[2].minimax == Outcome.WIN
    assert all_combos[2].lookahead == Outcome.WIN

    assert evaluate(all_combos[3]) == True
    assert all_combos[3].status == Status.O_WON
    assert all_combos[3].minimax == Outcome.WIN
    assert all_combos[3].lookahead == Outcome.WIN

    assert evaluate(all_combos[4]) == True
    assert all_combos[4].status == Status.X_WON
    assert all_combos[4].minimax == Outcome.WIN
    assert all_combos[4].lookahead == Outcome.WIN

    assert evaluate(all_combos[5]) == True
    assert all_combos[5].status == Status.O_WON
    assert all_combos[5].minimax == Outcome.WIN
    assert all_combos[5].lookahead == Outcome.WIN

    assert evaluate(all_combos[6]) == True
    assert all_combos[6].status == Status.X_WON
    assert all_combos[6].minimax == Outcome.WIN
    assert all_combos[6].lookahead == Outcome.WIN

    assert evaluate(all_combos[7]) == True
    assert all_combos[7].status == Status.O_WON
    assert all_combos[7].minimax == Outcome.WIN
    assert all_combos[7].lookahead == Outcome.WIN

    return
