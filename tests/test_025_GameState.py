import pytest

from darrought66.pytictactoe.GameState import GameState
from darrought66.pytictactoe.Player import Player
from darrought66.pytictactoe.location import loc


@pytest.fixture
def root_gs():
    root_gs = GameState()
    return root_gs


@pytest.fixture
def child(root_gs):
    root_gs.create_child(loc(1, 1), Player.X)
    child = root_gs.get_child_by_location(loc(1, 1))
    assert child is not None
    return child


def test_game_state_01(root_gs, child):
    assert child.current_player == Player.X
    return


def test_game_state_02(root_gs, child):
    assert child.current_location == loc(1, 1)
    return


def test_game_state_03(root_gs, child):
    assert child.parent == root_gs
    return


def test_game_state_04(root_gs, child):
    assert child.play_area[loc(1, 1)] == Player.X
    return


def test_game_state_05(root_gs, child):
    assert len(root_gs.open_locations()) == 9
    assert len(child.open_locations()) == 8
    return


def test_game_state_06(root_gs, child):
    assert str(child) == "(??? ___ ___ 4 X)  [- - -] [- X -] [- - -]"
    return
