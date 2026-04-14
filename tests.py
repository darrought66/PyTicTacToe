from evaluation import evaluate
from player import Player
from main import Grid


# unit test for the evaluate method
def test_evaluate():
    test_cases = test_case_01()
    for tc in test_cases:
        status = evaluate(tc)
        print(str(status) + " " + str(tc.status))

    return


# generates test cases for testing evaluate method.
def test_case_01():
    test_cases = [Grid(), Grid(), Grid(), Grid(), Grid(), Grid(), Grid(), Grid()]

    ndx = 0
    test_cases[ndx].spots[(0, 0)] = Player.X
    test_cases[ndx].spots[(1, 1)] = Player.X
    test_cases[ndx].spots[(2, 2)] = Player.X

    ndx = 1
    test_cases[ndx].spots[(2, 0)] = Player.O
    test_cases[ndx].spots[(1, 1)] = Player.O
    test_cases[ndx].spots[(0, 2)] = Player.O

    ndx = 2
    test_cases[ndx].spots[(0, 0)] = Player.X
    test_cases[ndx].spots[(0, 1)] = Player.X
    test_cases[ndx].spots[(0, 2)] = Player.X

    ndx = 3
    test_cases[ndx].spots[(1, 0)] = Player.O
    test_cases[ndx].spots[(1, 1)] = Player.O
    test_cases[ndx].spots[(1, 2)] = Player.O

    ndx = 4
    test_cases[ndx].spots[(2, 0)] = Player.X
    test_cases[ndx].spots[(2, 1)] = Player.X
    test_cases[ndx].spots[(2, 2)] = Player.X

    ndx = 5
    test_cases[ndx].spots[(0, 0)] = Player.O
    test_cases[ndx].spots[(1, 0)] = Player.O
    test_cases[ndx].spots[(2, 0)] = Player.O

    ndx = 6
    test_cases[ndx].spots[(0, 1)] = Player.X
    test_cases[ndx].spots[(1, 1)] = Player.X
    test_cases[ndx].spots[(2, 1)] = Player.X

    ndx = 7
    test_cases[ndx].spots[(0, 2)] = Player.O
    test_cases[ndx].spots[(1, 2)] = Player.O
    test_cases[ndx].spots[(2, 2)] = Player.O

    return test_cases
