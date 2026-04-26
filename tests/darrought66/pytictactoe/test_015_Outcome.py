from darrought66.pytictactoe.Outcome import Outcome


def test_from_str_01():
    assert Outcome.from_str("___") == Outcome.NONE
    return


def test_from_str_02():
    assert Outcome.from_str("WTL") == Outcome.ANY
    return


def test_union_01():
    assert Outcome.NONE.union(Outcome.WIN).union(Outcome.TIE).union(Outcome.LOSE) == Outcome.ANY
    return


def test_union_02():
    assert Outcome.TIE_OR_BETTER.union(Outcome.TIE_OR_WORSE) == Outcome.ANY
    return


def test_union_03():
    assert Outcome.TIE_OR_WORSE.union(Outcome.TIE_OR_BETTER) == Outcome.ANY
    return


def test_reverse_01():
    assert Outcome.WIN.reverse() == Outcome.LOSE
    return


def test_reverse_02():
    assert Outcome.LOSE.reverse() == Outcome.WIN
    return


def test_reverse_03():
    assert Outcome.ANY.reverse() == Outcome.ANY
    return


def test_reverse_04():
    assert Outcome.NONE.reverse() == Outcome.NONE
    return


def test_is_better_01():
    assert Outcome.is_better(Outcome.NONE, Outcome.LOSE)
    return


def test_is_better_02():
    assert Outcome.is_better(Outcome.LOSE, Outcome.TIE)
    return


def test_is_better_03():
    assert Outcome.is_better(Outcome.TIE, Outcome.WIN)
    return
