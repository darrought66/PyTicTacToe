import math
import pickle

from evaluation import evaluate
from player import Player
from status import Outcome
from status import Status


# a 3 by 3 play area plus all associated state. this class is used as a node
# in a tree of possible game states.
class Grid:
    # used for debugging
    class_count = 0  # number of classes instantiated
    ordinal = 0  # serves as name, index and key

    # play area is a 3 by 3 grid.
    # useful to have a list of all ordinates in play area.
    locations = []
    for col0 in range(3):
        for row0 in range(3):
            locations.append((col0, row0))

    # create an empty grid
    def __init__(self):

        self.ordinal = Grid.class_count
        Grid.class_count += 1

        self.spots = {}
        for location in self.locations:
            self.spots[location] = Player.OPEN

        # tree is a doubly linked structure
        self.parent = None
        self.children = {}

        # the status of this state. in other words does this state represent a WIN or TIE?
        self.status = Status.UNDECIDED

        # the status of this subtree. for example can player WIN regardless of what the
        # opponent chooses. this is relative to the current player.
        self.outcome = Outcome.NONE

        # the move that was made to get from the parent state to this state.
        self.current_player = Player.OPEN
        self.current_location = None

        return

    # create a child grid with spots data copied plus one additional play.
    def create_child(self, location, player):

        child = Grid()
        for location0 in self.locations:
            child.spots[location0] = self.spots[location0]

        child.parent = self
        self.children[location] = child

        child.spots[location] = player

        child.current_location = location
        child.current_player = player

        evaluate(child)

        return child

    # return a list of open locations.
    def open_locations(self):

        open_locations = []
        for location in self.locations:
            if self.spots[location] == Player.OPEN:
                open_locations.append(location)

        return open_locations

    # string representation
    def __str__(self):

        s = "(" + str(self.status) + " " + str(self.outcome) + " " + str(self.current_location) + " " + str(
            self.current_player) + ") "
        for row in range(3):
            s = s + " ["
            for col in range(3):
                if col == 0:
                    s = s + str(self.spots[(row, col)])
                else:
                    s = s + " " + str(self.spots[(row, col)])
            s = s + "]"
        return s


# prints a tree of game states
def print_tree(root_tree):
    print(str(root_tree) + "\n")  # print root grid
    print_tree0(root_tree, 1)  # print tree
    return


# prints tree of provided grid
def print_tree0(parent, depth):
    for child in parent.children.values():
        print(("\t" * depth) + str(child) + "\n")
        print_tree0(child, depth + 1)

    return


# creates a tree of game states.
def grow_tree(grid, player, depth):
    if depth > 10:
        raise RuntimeError("depth exceeded 10")

    open_locations = grid.open_locations()

    if len(open_locations) == 0:
        return

    for location in open_locations:
        child = grid.create_child(location, player)
        if child.outcome == Outcome.NONE:
            grow_tree(child, player.opposite(), depth + 1)

    return


# serialize entire game tree to a file
def pickle_game_tree(root_grid):
    with open("tic_tac_toe_game_tree.pkl", "wb") as file:
        pickle.dump(root_grid, file)
    return


# restore entire game tree from a file
def restore_game_tree():
    with open("tic_tac_toe_game_tree.pkl", "rb") as file:
        root_grid = pickle.load(file)
    return root_grid


# calculates the size of the tree if every spot is used. in most games a win is
# reached while there are still open spots. we are ignoring that fact here. we
# want to know the maximal boundry. 986410 is full size.
def calc_full_tree_size():
    sum0 = 1
    for n in range(9):
        sum0 = sum0 + math.factorial(9) / math.factorial(n)
    print("a full tree has " + str(sum0) + " nodes\n")

    return


# assign outcome values
def assign_outcome(grid):
    # if the grid outcome has not been calculated then calculate it
    if grid.outcome == Outcome.NONE:

        # calculate the outcome for each child that has not been calculated by recursive call
        for child in grid.children.values():
            if child.outcome == Outcome.NONE:
                assign_outcome(child)

            # a grids outcome is the union of its children outcomes.
            grid.outcome = grid.outcome.union(child.outcome)

        # the grids outcome and the children outcomes are for opposite players.
        grid.outcome = grid.outcome.reverse()

    return grid.outcome


# draws a grid on a text console for simple play and debugging.
def display_grid(grid):
    for row in range(3):
        for col in range(3):
            location = (col, row)
            if grid.spots[location] == Player.OPEN:
                print(str(3 * row + col), end="")
            else:
                print(grid.spots[location], end="")
        print("")

    return
