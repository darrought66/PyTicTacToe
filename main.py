import math
import pickle
from player import Player
from status import Status
from status import TreeStatus
from evaluation import evaluate

# play area is a 3 by 3 grid.
# useful to have a list of all ordinates in play area.
locations = []
for col in range(3):
    for row in range(3):
        locations.append((col, row))


# a 3 by 3 play area plus all associated state. this class is used as a node
# in a tree of possible game states.
class Grid:
    # used for debugging
    class_count = 0  # number of classes instantiated
    ordinal = 0  # serves as name, index and key

    # create an empty grid
    def __init__(self):

        self.ordinal = Grid.class_count
        Grid.class_count += 1

        self.spots = {}
        for location in locations:
            self.spots[location] = Player.OPEN

        # tree is a doubly linked structure
        self.parent = None
        self.children = []

        # the status of this state. in other words does this state represent a WIN or TIE?
        self.status = Status.UNDECIDED

        # the status of this sub tree. for example can player WIN regardless of what the
        # opponent chooses. this is relative to the current player.
        self.tree_status = TreeStatus.NONE

        # the move that was made to get from the parent state to this state.
        self.current_player = Player.OPEN
        self.current_location = None

        return

    # create a child grid with spots data copied plus one additional play.
    def create_child(self, location, player):

        child = Grid()
        for location0 in locations:
            child.spots[location0] = self.spots[location0]

        child.parent = self
        self.children.append(child)

        child.spots[location] = player

        child.current_location = location
        child.current_player = player

        evaluate(child)

        return child

    # return a list of open locations.
    def open_locations(self):

        open_locations = []
        for location in locations:
            if self.spots[location] == Player.OPEN:
                open_locations.append(location)

        return open_locations

    # string representation
    def __str__(self):

        s = "(" + str(self.status) + " " + str(self.tree_status) + " " + str(self.current_location)  + " " + str(self.current_player) + ") "
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
    for child in parent.children:
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
        if child.tree_status == TreeStatus.NONE:
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


# assign tree status values
def assign_tree_status(grid):

    if grid.tree_status == TreeStatus.NONE:
        for child in grid.children:

            if child.tree_status == TreeStatus.NONE:
                assign_tree_status(child)

            grid.tree_status = grid.tree_status.union(child.tree_status)

        grid.tree_status = grid.tree_status.reverse()

    return grid.tree_status


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    TreeStatus.define_singletons()

    # tree can be clipped to 526,906 by halting when a WIN or TIE state is reached
    root_grid = Grid()
    grow_tree(root_grid, Player.X, 0)
    assign_tree_status(root_grid)

    print("the tree has " + str(Grid.class_count) + " nodes\n")
    print_tree(root_grid)
