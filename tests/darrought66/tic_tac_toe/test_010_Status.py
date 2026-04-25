from darrought66.tic_tac_toe.Status import Status


def test_from_str_01():
    assert Status.from_str("???") == Status.UNDECIDED
    return


def test_from_str_02():
    assert Status.from_str("X WINS") == Status.X_WON
    return


def test_from_str_03():
    assert Status.from_str("O WINS") == Status.O_WON
    return


def test_from_str_04():
    assert Status.from_str("TIE") == Status.TIE
    return
