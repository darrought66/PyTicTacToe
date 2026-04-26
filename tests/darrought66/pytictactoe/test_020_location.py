from darrought66.pytictactoe.location import loc, col, row


def test_loc_01():
    assert loc(0, 0) == 0
    return


def test_loc_02():
    assert loc(0, 2) == 2
    return


def test_loc_03():
    assert loc(2, 0) == 6
    return


def test_loc_04():
    assert loc(2, 2) == 8
    return


def test_col_01():
    assert col(0) == 0
    return


def test_col_02():
    assert col(2) == 2
    return


def test_col_03():
    assert col(6) == 0
    return


def test_col_04():
    assert col(8) == 2
    return


def test_row_01():
    assert row(0) == 0
    return


def test_row_02():
    assert row(2) == 0
    return


def test_row_03():
    assert row(6) == 2
    return


def test_row_04():
    assert row(8) == 2
    return
