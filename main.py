import sys

from grid import Grid, grow_tree, assign_outcome, display_grid
from player import Player
from status import Outcome
from status import Status

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Outcome.define_singletons()

    grid = Grid()
    grow_tree(grid, Player.X, 0)
    assign_outcome(grid)

    for _ in range(9):
        display_grid(grid)
        ch = input("enter your choice: ")
        ch = int(ch)
        location = (ch % 3, ch // 3)
        print(location)
        grid = grid.children[location]
        if grid.status != Status.UNDECIDED:
            display_grid(grid)
            sys.exit(grid.status)
