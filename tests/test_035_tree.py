import pytest

from darrought66.pytictactoe.GameState import GameState
from darrought66.pytictactoe.Outcome import Outcome
from darrought66.pytictactoe.Player import Player
from darrought66.pytictactoe.Status import Status
from darrought66.pytictactoe.construct_state_tree import grow_tree, assign_outcome


def test_tree():

    GameState.class_count = 0
    root_gs0 = GameState()
    grow_tree(root_gs0, Player.X, 0)
    assign_outcome(root_gs0)
    inspect(root_gs0)

    return

def inspect(gs):

    assert gs.ordinal is not None and 0 <= gs.ordinal <= 526905
    assert gs.play_area is not None

    if gs.ordinal != 0:
        assert gs.status is not None
        assert gs.minimax is not None and gs.minimax != Outcome.NONE
        assert gs.lookahead is not None and gs.lookahead != Outcome.NONE
        assert gs.parent is not None
        assert gs.children is not None
        assert gs.current_player is not None and gs.current_player != Player.OPEN
        assert gs.current_location is not None and 0 <= gs.current_location <= 8

    if gs.status != Status.UNDECIDED:
        assert len(gs.children) == 0

    else:
        assert len(gs.children) > 0

    return