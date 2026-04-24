import math

from src.darrought66.tic_tac_toe.evaluation import evaluate
from . import Player, GameState


# unit test for the evaluate method
def test_evaluate():
    test_cases = test_case_01()
    for tc in test_cases:
        status = evaluate(tc)
        print(str(status) + " " + str(tc.status))

    return


# generates test cases for testing evaluate method.
def test_case_01():
    test_cases = [GameState(), GameState(), GameState(), GameState(), GameState(), GameState(), GameState(), GameState()]

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


# calculates the size of the tree if every spot is used. in most games a win is
# reached while there are still open spots. we are ignoring that fact here. we
# want to know the maximal boundry. 986410 is full size.
def calc_full_tree_size():
    sum0 = 1
    for n in range(9):
        sum0 = sum0 + math.factorial(9) / math.factorial(n)
    print("a full tree has " + str(sum0) + " nodes\n")

    return
