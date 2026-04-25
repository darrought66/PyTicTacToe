from darrought66.tic_tac_toe.Player import Player


def test_from_str_01():
    assert Player.from_str("X") == Player.X
    return


def test_from_str_02():
    assert Player.from_str("O") == Player.O
    return


def test_from_str_03():
    assert Player.from_str("-") == Player.OPEN
    return


def test_opposite_01():
    assert Player.X.opposite() == Player.O
    return


def test_opposite_02():
    assert Player.O.opposite() == Player.X
    return
