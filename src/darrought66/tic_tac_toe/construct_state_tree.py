from darrought66.tic_tac_toe.GameState import GameState
from darrought66.tic_tac_toe.Outcome import Outcome
from darrought66.tic_tac_toe.Player import Player
from darrought66.tic_tac_toe.Status import Status
from darrought66.tic_tac_toe.debug_test_util import print_tree


# these methods construct the solution space, which is a doubly linked tree of GameState objects.

# creates a tree of game states.
def grow_tree(gs: GameState, player: Player, depth: int):
    # guard clause, depth = 0 is empty game. there are 9 spots in the game. therefore should never go deeper than 9.
    if depth > 9:
        raise RuntimeError("depth exceeded 10")

    open_locations = gs.open_locations()

    if len(open_locations) == 0:
        return

    for location in open_locations:
        child = gs.create_child(location, player)
        # status is set for terminal game states. do not generate past a terminal state.
        if child.status == Status.UNDECIDED:
            grow_tree(child, player.opposite(), depth + 1)

    return


# after the tree has been constructed then outcome values must be assigned to each node. the evaluations start from the
## leaves and proceed towards the root.
def assign_outcome(gs: GameState) -> Outcome:
    # if the game state outcome has not been calculated then calculate it
    if gs.outcome == Outcome.NONE:

        # calculate the outcome for each child that has not been calculated by recursive call
        for child in gs.children.values():
            if child.outcome == Outcome.NONE:
                assign_outcome(child)

            # the best option assuming the other player makes the optimal choice
            gs = minimax(gs, child)

        # this players outcome is the opposite of that for the other player.
        gs.outcome = gs.outcome.reverse()

        # the range is the union of child outcomes
        gs.range = Outcome.NONE  # safety, should already be true
        for child in gs.children.values():
            gs = calc_range(gs, child)

        # this players outcome is the opposite of that for the other player.
        gs.range = gs.range.reverse()

    return gs.outcome


# calculate the range of possibilities from this state
def calc_range(gs: GameState, child: GameState) -> GameState:
    if gs.range == Outcome.NONE:
        gs.range = child.outcome
    else:
        gs.range = Outcome.union(gs.range, child.outcome)

    return gs


# calculate the best option assuming the other player will choose optimally
def minimax(gs: GameState, child: GameState) -> GameState:
    if gs.outcome == Outcome.NONE:
        gs.outcome = child.outcome
    elif Outcome.is_better(gs.outcome, child.outcome):
        gs.outcome = child.outcome

    return gs


# debugging. prints out the solution space for visual inspection.
if __name__ == '__main__':
    Outcome.define_singletons()

    # create the solution space
    root_gs = GameState()
    grow_tree(root_gs, Player.X, 0)
    assign_outcome(root_gs)

    print_tree(root_gs)
